# Generated by Django 4.0.3 on 2022-03-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_discount_ratio'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default="", max_length=128),
            preserve_default=False,
        ),
    ]