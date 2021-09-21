from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from core.models import Currency, Category, Transaction
from core.serializers import (
    CurrencySerializer,
    CategorySerializer,
    ReadTransactionSerializer,
    # TransactionSerializer,
    WriteTransactionSerializer,
)


# Create your views here.


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # pagination_class = PageNumberPagination
    pagination_class = None


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class TransactionModelViewset(ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer


class TransactionModelViewset(ModelViewSet):
    queryset = Transaction.objects.select_related("currency", "category")
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("description",)
    ordering_fields = ("amount", "date")
    fiterset_class = ("currency__code",)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
