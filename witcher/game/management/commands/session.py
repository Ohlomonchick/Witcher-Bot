import asyncio

from asgiref.sync import sync_to_async
from django.core.management import BaseCommand

from game.management.commands.game_data import rpg_data
from game.models import Profile


class Session:
    rpg_data = rpg_data

    def __init__(self, profile, new=False):
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

        self.messages = 0

    async def scheduled(self):
        while True:
            await asyncio.sleep(60)
            if self.messages == 0:
                await sync_to_async(self.profile.save)()
            messages = 0

    def message_process(self, message):
        self.messages += 1
        text, image, sticker, kb = '', None, None, None

        return text, image, sticker, kb


# class Command(BaseCommand):
#     help = 'Бот'
#
#     def handle(self, *args, **kwargs):
#         s = Session(Profile.objects.get(external_id=737145534))
#         print(s.rpg_data[0]['message'])
