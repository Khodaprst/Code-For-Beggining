# Generated by Django 3.2.7 on 2021-10-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_auto_20210924_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]