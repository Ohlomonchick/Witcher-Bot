# Generated by Django 3.2.2 on 2021-05-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-total', 'name'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.IntegerField(default=1, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='karma',
            field=models.IntegerField(default=50, verbose_name='Карма'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total',
            field=models.IntegerField(default=0, verbose_name='Очки'),
        ),
    ]