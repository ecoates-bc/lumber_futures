from django.db import models


class FuturesDay(models.Model):
    Date = models.DateField(default=None, null=True)
    Open = models.FloatField(default=0, null=True)
    High = models.FloatField(default=0, null=True)
    Low = models.FloatField(default=0, null=True)
    Close = models.FloatField(default=0, null=True)
    Adj_Close = models.FloatField(default=0, null=True)
    Volume = models.PositiveIntegerField(default=0, null=True)
