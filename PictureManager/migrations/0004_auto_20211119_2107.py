# Generated by Django 3.2.9 on 2021-11-19 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PictureManager', '0003_auto_20211119_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='caption',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='continent',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
