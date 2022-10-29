from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *


# https://python-telegram-bot.org/
# name: ru_python_bot
# username: ru_my_python_bot

app = ApplicationBuilder().token("5726903819:AAFOFc7ampkKQ81ECUTCXcXbSkANSQEhHSs").build()

print('Server start')

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))

app.run_polling()