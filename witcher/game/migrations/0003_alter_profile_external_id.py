# Generated by Django 3.2.2 on 2021-05-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210507_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.IntegerField(unique=True, verbose_name='ID в Telegram'),
        ),
    ]
