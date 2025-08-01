from django.db import models

class Status(models.Model):
    available_cash = models.IntegerField(default = 0)
    stock_amount = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    profits = models.IntegerField(default = 0)
    development = models.IntegerField(default = 0)