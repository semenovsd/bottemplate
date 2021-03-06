import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TGBOT_TOKEN

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)

storage = MemoryStorage()

bot = Bot(token=TGBOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
