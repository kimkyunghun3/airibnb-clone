from django.db import models


class TimeStampedModel(models.Model):

    """"Time Stamped Model"""

    created = models.DateField(
        auto_now_add=True
    )  # auto_now_add =True을 하면 admin에 내가 생성한 시간과 날짜를 기록해준다
    updated = models.DateField(auto_now=True)  # auto_now = True 을 새로운 날짜로 업데이트 해준다

    class Meta:
        abstract = True

