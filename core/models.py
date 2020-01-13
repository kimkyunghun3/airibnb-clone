from django.db import models


class TimeStampedModel(models.Model):

    """"Time Stamped Model"""

    created = models.DateField()
    updated = models.DateField()

    class Meta:
        abstract = True
