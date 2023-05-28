from vkbottle import User
from app.config import api, labeler, lw
from app.handlers import labelers
import time
from loguru import logger
import sys


logger.remove()
logger.add(sys.stderr, level="INFO")
bot = User(api=api, labeler=labeler, loop_wrapper=lw)


for labeler in labelers:
    bot.labeler.load(labeler)


if __name__ == "__main__":
    start_ini = time.time()
    # logger.add("game_log.log", rotation='10 mb', level="INFO", retention='3 day')
    bot.run_forever()
