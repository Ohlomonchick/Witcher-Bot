# Generated by Django 3.2.2 on 2021-05-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_profile_external_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='not_started', max_length=255, verbose_name='Состояние'),
        ),
    ]