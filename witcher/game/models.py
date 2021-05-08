from django.db import models


class Achievement:
    def __init__(self):
        self.note = False
        self.troll_side = False
        self.troll_dead = False

    def __str__(self):
        return f'Записка найдена: {self.note} Принял(а) сторону тролля: {self.troll_side} Тролль мёртв: {self.troll_dead}'


class Profile(models.Model):
    external_id = models.IntegerField(verbose_name='ID в Telegram', unique=True)
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    experience = models.IntegerField(verbose_name="Опыт", default=0)
    karma = models.IntegerField(verbose_name="Карма", default=50)
    level = models.IntegerField(verbose_name="Уровень игрока", default=1)
    total = models.IntegerField(verbose_name="Очки", default=0)
    position = models.IntegerField(verbose_name="Позиция", default=1)

    state = models.CharField(max_length=255, verbose_name='Состояние', default='not_started')

    achievement = Achievement()

    def __str__(self):
        return f'#{self.name} Имя: {self.name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-total', 'name']