# Generated by Django 5.2 on 2025-08-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_alter_stock_buying_price_each'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100, unique=True)),
                ('qty', models.IntegerField()),
                ('selling_price_each', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('profits_each', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('item', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('total_buying_price', models.IntegerField()),
                ('buying_price_each', models.IntegerField()),
                ('selling_price_each', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('profits_each', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('total_selling_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('total_profits', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
