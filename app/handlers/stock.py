from vkbottle.bot import BotLabeler, Message, rules
from app.config import library_peer


class OnlyThisPeerRule(rules.ABCRule[Message]):
    async def check(self, message: Message):
        if message.peer_id == library_peer:
            return True


chat_labeler = BotLabeler()
chat_labeler.auto_rules = [rules.PeerRule(from_chat=True), OnlyThisPeerRule()]


@chat_labeler.message(text='!сервис')
async def service_generator(message: Message):
    if message.from_id == 15887656:
        await message.answer('Так вот:\n'
                             f'only_this_peer = {message.peer_id}')