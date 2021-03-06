# Generated by Django 3.1.4 on 2021-05-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210517_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='street',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
