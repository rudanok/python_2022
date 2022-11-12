from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open(r'Test_9\log.csv', 'a', 1, encoding='utf-8')
    file.write(f'{update.effective_user.id}, {update.effective_user.first_name}, {update.message.text}\n')
    file.close()