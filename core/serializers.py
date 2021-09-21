from django.db.models import fields, query_utils
from rest_framework import serializers

from core.models import Category, Currency, Transaction


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


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
    currency = serializers.SlugRelatedField(
        slug_field="code", queryset=Currency.objects.all()
    )

    class Meta:
        model = Transaction
        fields = ("amount", "currency", "date", "description", "category")


class ReadTransactionSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = ("id", "amount", "currency", "date", "description", "category")
        read_only_fields = fields
