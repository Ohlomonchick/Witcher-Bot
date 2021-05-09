import asyncio
import copy

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asgiref.sync import sync_to_async
from django.core.management import BaseCommand

from game.management.commands.game_data import rpg_data
from game.models import Profile


class Session:

    def __init__(self, profile, new=False):
        self.rpg_data = copy.deepcopy(rpg_data)
        # global rpg_data
        self.profile = profile
        self.action_data = self.rpg_data[profile.position - 1] if not new else self.rpg_data[0]
        self.action = self.action_data['name']
        self.chosen_action = None
        self.available_actions = None
        self.message = ''

        self.text = ''
        self.answer = None
        self.state = None

        self.received_answer = None

        self.appeals = 0
        self.can_be_deleted = False

    async def scheduled(self):
        while True:
            await asyncio.sleep(20)
            if self.appeals == 0 and not self.can_be_deleted:
                await sync_to_async(self.profile.save)()
                self.can_be_deleted = True
                print('Автосохранение прошло успешно')
            self.appeals = 0

    async def action_process(self, message=None):
        self.appeals += 1
        self.can_be_deleted = False
        text, image, sticker, kb = '', None, None, None
        if message and not self.answer and message.text != '':
            return text, image, sticker, kb

        self.received_answer = message

        if int(self.action_data['name']) == 1:
            self.rpg_data = copy.deepcopy(rpg_data)

        if self.chosen_action:
            if self.available_actions and self.chosen_action != len(self.available_actions) + 1:
                self.action = self.available_actions[self.chosen_action - 1]
                self.action_data = self.rpg_data[
                    self.action_data['actions'][self.available_actions[self.chosen_action - 1]][0]]
                self.profile.position = int(self.action_data['name'])

        if 'achievement' in self.action_data.keys():
            self.profile[self.action_data['achievement']] = True

        if 'answer' in self.action_data.keys():
            self.answer = self.action_data['answer']
        else:
            self.available_actions = [context for context, i in self.action_data['actions'].items()
                                      if (i[1] is None or self.profile.achievement[i[1]])]

        text = self.action_data['message']
        if self.profile.position != 1 and type(self.action) != int and not self.action.isdigit():
            if len(self.action) < 40:
                text += f'\nВы выбрали действие [{self.action}]'
            else:
                text += f'\nВы выбрали действие [{self.action[:40]}...]'

        kb = InlineKeyboardMarkup()
        if self.answer:
            before = self.answer['before']
            text += f'\n\n{before} или выберите одно из доступных действий:'
            self.available_actions = []
        else:
            text += '\n\nВыберите действие:'

            bigger = False

            for i, action in zip(range(len(self.available_actions)), self.available_actions):
                if len(action) >= 50:
                    bigger = True
                kb.add(InlineKeyboardButton(f'{i + 1}.{action}', callback_data=f'btn{i + 1}'))
            if bigger:
                text += '\n'
                for i, action in zip(range(len(self.available_actions)), self.available_actions):
                    text += f'\n{i + 1}.{action}'

        last = len(self.available_actions) + 1
        kb.add(InlineKeyboardButton(f'{last}.Сохранить и выйти', callback_data=f'quit_game'))

        # TODO получить ответ
        if self.answer:
            self.profile.state = 'wrong_answer'
            # self.chosen_action, answer_text = await self._answer_check()
            # text += answer_text

        return text, image, sticker, kb

    async def _answer_check(self, message=None):
        self.received_answer = message
        try:
            if type(self.answer['answ']) == str:
                output = self.received_answer.text
                if output.lower() != self.answer['answ']:
                    raise ValueError('Неккоректный ввод!')
            else:
                output = int(self.received_answer.text)
                if output != self.answer['answ']:
                    raise ValueError('Неккоректный ввод!')

            self.profile.state = 'started'
            answer_text = 'ВЕРНО!\n'
            answer_text += '-' * 20 + '\n\n'
            answer_text += self.answer['after']
            self.action_data.pop('answer')
            self.answer = None
            return self.chosen_action, answer_text

        except Exception as exc:
            if self.received_answer:
                await self.received_answer.answer('Вы ввели неправильный ответ')
            self.profile.state = 'wrong_answer'


# class Command(BaseCommand):
#     help = 'Бот'
#
#     def handle(self, *args, **kwargs):
#         s = Session(Profile.objects.get(external_id=737145534))
#         print(s.rpg_data[0]['message'])
