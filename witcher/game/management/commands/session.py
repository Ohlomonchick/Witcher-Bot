import asyncio
import copy

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asgiref.sync import sync_to_async
from django.core.management import BaseCommand

from game.management.commands.game_data import rpg_data
from game.models import Profile


class Session:

    def __init__(self, profile, new=False, data=None):
        self.rpg_data = copy.deepcopy(rpg_data) if not data else data
        self.profile = profile
        self.action_data = self.rpg_data[profile.position - 1] if not new else self.rpg_data[0]

        if new:
            self.profile.experience = 0
            self.profile.karma = 50

        self.action = self.action_data['name']
        self.chosen_action = None
        self.available_actions = None
        self.message = ''
        self.correct = False

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
                await sync_to_async(self.profile.save, thread_sensitive=False)()
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
            if 'answer' not in self.action_data.keys() and not self.correct:
                data = self.action_data['actions'][self.available_actions[self.chosen_action - 1]]
                if len(data) >= 3 and data[2]:
                    self.profile.achievement[data[2]] = True
                    print('Получено достижение {}')
                if len(data) >= 4 and data[3]:
                    self.profile.karma += data[3]
                    await self._reckon()
                if len(data) >= 5:
                    pass

            if self.available_actions and self.chosen_action != len(self.available_actions) + 1:
                self.action = self.available_actions[self.chosen_action - 1]
                self.action_data = self.rpg_data[
                    self.action_data['actions'][self.available_actions[self.chosen_action - 1]][0]]
                self.profile.position = int(self.action_data['name'])


        self.correct = False

        # if 'achievement' in self.action_data.keys():
        #     self.profile[self.action_data['achievement']] = True

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
                kb.add(InlineKeyboardButton(f'{i + 1}.{action}',
                                            callback_data=f'btn_{self.action_data["name"]}_{i + 1}'))
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
        self.appeals += 1
        self.can_be_deleted = False
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
            answer_text += '-' * 20 + '\n'
            if 'reward' in self.answer.keys():
                reward = self.answer['reward']
                self.profile.experience = self.profile.experience + reward
                answer_text += f'Вы получили {reward} опыта в награду\n\n'
                await self._reckon()
            answer_text += self.answer['after']
            self.action_data.pop('answer')
            self.answer = None
            self.correct = True
            return self.chosen_action, answer_text

        except Exception as exc:
            if self.received_answer:
                await self.received_answer.answer('Вы ввели неправильный ответ')
            self.profile.state = 'wrong_answer'

    async def _reckon(self):
        self.profile.total = round(self.profile.experience * (self.profile.karma / 100))
        await sync_to_async(self.profile.save, thread_sensitive=False)()


# class Command(BaseCommand):
#     help = 'Бот'
#
#     def handle(self, *args, **kwargs):
#         s = Session(Profile.objects.get(external_id=737145534))
#         print(s.rpg_data[0]['message'])
