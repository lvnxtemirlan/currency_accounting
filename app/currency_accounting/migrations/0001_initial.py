# Generated by Django 3.1.3 on 2020-11-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_currency', models.FloatField(default=0, max_length=20, null=True)),
                ('market_currency', models.FloatField(default=0, max_length=20, null=True)),
                ('value', models.FloatField(default=0, max_length=255, null=True)),
            ],
        ),
    ]
