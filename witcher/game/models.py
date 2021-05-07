from django.db import models


class Profile(models.Model):
    external_id = models.IntegerField(verbose_name='ID в Telegram', unique=True)
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    experience = models.IntegerField(verbose_name="Опыт", default=0)
    karma = models.IntegerField(verbose_name="Карма", default=50)
    level = models.IntegerField(verbose_name="Уровень игрока", default=1)
    total = models.IntegerField(verbose_name="Очки", default=0)
    position = models.IntegerField(verbose_name="Позиция", default=1)

    def __str__(self):
        return f'#{self.name} Имя: {self.name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-total', 'name']