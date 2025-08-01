from django.db import models

class Users(models.Model):
    username = models.CharField(max_length = 100, unique=True)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)



class ItemList(models.Model):
    item = models.CharField(max_length=20, unique=True)


class StockHistory(models.Model):
    date = models.DateField(auto_now_add=True)
    item = models.CharField(max_length=100)
    qty = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    total_buying_price = models.IntegerField()
    buying_price_each = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    selling_price_each = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    profits_each = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    total_selling_price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    total_profits = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)

class AvailableStock(models.Model):
    item = models.CharField(max_length=100, unique=True)
    qty = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    buying_price_each = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    selling_price_each = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    profits_each = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)


class Sales(models.Model):
    date = models.DateField(auto_now_add=True)
    item = models.CharField(max_length = 100)
    quantity = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    profits = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    

class Status(models.Model):
    available_cash = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    stock_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)#cash+stock
    profits = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)#cash(updated after sale)
    development = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)#since first date of system use

class Expenditure(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    reason = models.CharField(max_length = 100)

