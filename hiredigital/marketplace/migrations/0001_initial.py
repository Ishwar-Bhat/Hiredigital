# Generated by Django 3.2.4 on 2021-07-04 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.CharField(max_length=255, null=True)),
                ('product_stock', models.IntegerField(default=0)),
                ('product_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('created_date', models.DateField(auto_now=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.productcategory')),
            ],
        ),
    ]