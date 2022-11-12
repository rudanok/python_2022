from telegram import Update
from telegram.ext import ContextTypes
import datetime


async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open(r'Test_10\log.csv', 'a', 1, encoding='utf-8')
    file.write(f'{datetime.datetime.now()}, {update.effective_user.id}, {update.effective_user.first_name}, {update.message.text}\n')
    file.close()