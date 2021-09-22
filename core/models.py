# from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Currency(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="currencies"
    )  # # user.transactions.all() # 잘못 만듬 . column 삭제 할려고 했으나, dbsqlite는 힘듬
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="categories"
    )  # # user.transactions.all()
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )  # # user.transactions.all()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, related_name="transactions"
    )
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transactions",
    )

    def __str__(self):
        return f"{self.amount} {self.currency.code} {self.date}"
