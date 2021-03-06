# Generated by Django 4.0.3 on 2022-03-15 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_many_bought', models.IntegerField(default=1)),
                ('how_many_offered', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField(default=0)),
                ('department', models.CharField(max_length=128)),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.discount')),
            ],
        ),
    ]
