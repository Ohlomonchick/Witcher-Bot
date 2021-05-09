from django.db import models


class Achievement:
    def __init__(self):
        self.note = False
        self.troll_side = False
        self.troll_dead = False

    def __str__(self):
        return f'Записка: {self.note} Принял(а) сторону тролля: {self.troll_side} Тролль мёртв: {self.troll_dead}'

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == 'note':
            return self.note
        elif item == 'troll_side':
            return self.troll_side
        elif item == 'troll_dead':
            return self.troll_dead

    def __setitem__(self, item, value):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if not isinstance(value, bool):
            raise ValueError("Значение должно быть булиевым")

        if item == 'note':
            self.note = value
        elif item == 'troll_side':
            self.troll_side = value
        elif item == 'troll_dead':
            self.troll_dead = value


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