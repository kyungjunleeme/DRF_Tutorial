# DRF_Tutorial

https://www.youtube.com/watch?v=HbD9dcQeS8Y&list=PLLxk3TkuAYnrO32ABtQyw2hLRWt1BUrhj&index=3

해당 튜토리얼을 따라하고 있습니다.

https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

추석 연휴 기간동안 완강하고, 한국어로 정리해서 다시 공유하도록 하겠습니다.



```python
class Currency(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="currencies"
    )  # # user.transactions.all() # 잘못 만듬 . column 삭제 할려고 했으나, dbsqlite는 힘듬
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

```

Currency 모델에서는 user column을 만들 필요가 없습니다. 참고하시기 바랍니다