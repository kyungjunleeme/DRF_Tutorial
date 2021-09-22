from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import request, serializers
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    AllowAny,
    DjangoModelPermissions,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)


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
    permission_classes = (IsAuthenticated,)
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


# class TransactionModelViewset(ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer


class TransactionModelViewset(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    # queryset = Transaction.objects.select_related("currency", "category", "user")
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("description",)
    ordering_fields = ("amount", "date")
    filterset_fields = ("currency__code",)

    def get_queryset(self):
        return Transaction.objects.select_related(
            "currency", "category", "user"
        ).filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
