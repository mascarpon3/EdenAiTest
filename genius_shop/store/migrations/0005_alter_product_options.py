# Generated by Django 4.0.3 on 2022-03-16 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
    ]
