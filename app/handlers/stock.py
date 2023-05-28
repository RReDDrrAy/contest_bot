from vkbottle.bot import BotLabeler, Message, rules
from app.config import library_peer, api
from app.sql_worker import *
from .Users import User



class OnlyThisPeerRule(rules.ABCRule[Message]):
    async def check(self, message: Message):
        if message.peer_id == library_peer:
            return True


chat_labeler = BotLabeler()
chat_labeler.auto_rules = [rules.PeerRule(from_chat=True), OnlyThisPeerRule()]


@chat_labeler.message(command='рег')
async def registration(message: Message):
    sql = f'SELECT * FROM users WHERE user_id={message.from_id}'
    res = await sql_fetchall_col_name(sql=sql)
    if not res:
        user_info = (await api.users.get(user_ids=message.from_id))[0]
        first_name = user_info.first_name
        last_name = user_info.last_name
        sql = 'INSERT INTO users(user_id, first_name, last_name) VALUES(?,?,?)'
        args = [message.from_id, first_name, last_name]
        await sql_execute_safe(sql=sql, args=args)
        await message.answer('Вы были успешно зарегистрированы.')
    else:
        await message.answer('Вы уже зарегистрированы')


@chat_labeler.message(command='инфо')
async def get_info(message: Message):
    sql = f'SELECT * FROM users WHERE user_id={message.from_id}'
    res = await sql_fetchone_col_name(sql=sql)
    if not res:
        await message.answer('Сначала нужно зарегистрироваться(командка "!рег")!')
    else:
        user = User(**res)
        msg = f'Пользователь: {user.first_name}{user.last_name}\n' \
              f'{user.goods}'
        await message.answer(msg)


@chat_labeler.message(text='+ <book_name>')
async def update_goods(message: Message, book_name):
    sql = f'SELECT * FROM users WHERE user_id={message.from_id}'
    res = await sql_fetchone_col_name(sql=sql)
    if not res:
        await message.answer('Сначала нужно зарегистрироваться(командка "!рег")!')
    else:
        user = User(**res)
        print(user)
        # if user.count_slots == user.total_slots:
        #     await message.answer('У вас нет свободных ячеек для записи')
        # else:
            # sql = f"""UPDATE users
            #         SET
            #         first_good = CASE WHEN first_good IS NULL AND second_good IS NOT NULL AND third_good IS NOT NULL THEN '{book_name}' ELSE first_good END,
            #         second_good = CASE WHEN first_good IS NOT NULL AND second_good IS NULL AND third_good IS NOT NULL THEN '{book_name}' ELSE second_good END,
            #         third_good = CASE WHEN first_good IS NOT NULL AND second_good IS NOT NULL AND third_good IS NULL THEN '{book_name}' ELSE third_good END
            #         WHERE user_id = {message.from_id}"""
            # await sql_executescript(sql)


