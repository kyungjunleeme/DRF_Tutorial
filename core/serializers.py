# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import fields, query_utils
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from core.models import Category, Currency, Transaction

# User = get_user_model()


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")
        read_only_fields = fields


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "name")


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ("id", "name", "user")


# class TransactionSerializer(serializers.ModelSerializer):
#     # (slug_field=None, **kwargs) -> None
#     # A read-write field that represents the target of the relationship by a unique 'slug' attribute.
#     currency = serializers.SlugRelatedField(
#         slug_field="code", queryset=Currency.objects.all()
#     )

#     class Meta:
#         model = Transaction
#         fields = ("id", "amount", "currency", "date", "description", "category")


class WriteTransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    currency = serializers.SlugRelatedField(
        slug_field="code", queryset=Currency.objects.all()
    )

    class Meta:
        model = Transaction
        fields = (
            "user",
            "amount",
            "currency",
            "date",
            "description",
            "category",
        )  # delete user and override perform_create

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        # self.fields["category"].queryset = Category.objects.filter(user=user)
        self.fields["category"].queryset = user.categories.all()  # related_name 사용하기


class ReadTransactionSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "currency",
            "date",
            "description",
            "category",
            "user",
        )
        read_only_fields = fields


# User Info
# id / user.username
# 1 ,kyungjunlee
# 2 ,jiyoung
# 3 ,maria
