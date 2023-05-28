from vkbottle import API, LoopWrapper
from vkbottle.user import UserLabeler
from pathlib import Path
from dotenv import dotenv_values


TOKEN = dotenv_values("app/.env").get('TOKEN')
print(TOKEN)

my_id = 15887656
library_peer = 145
contest_peer = int()

db_path = Path('./app/db/auc.db')
api = API(TOKEN)
labeler = UserLabeler()
lw = LoopWrapper()
labeler.message_view.replace_mention = True

