from vkbottle import API, LoopWrapper
from vkbottle.user import UserLabeler
from pathlib import Path
from dotenv import dotenv_values


TOKEN = dotenv_values("app/.env").get('TOKEN')
my_id = 15887656
library_id = 145
contest_id = int()
library_peer = library_id + 2000000000
contest_peer = contest_id + 2000000000

db_path = Path('./app/db/main.db')
api = API(TOKEN)
labeler = UserLabeler()
lw = LoopWrapper()
labeler.message_view.replace_mention = True

