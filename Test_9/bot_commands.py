from telegram import Update
from telegram.ext import ContextTypes
import datetime
from log import * 


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)
    await update.message.reply_text('/hi\n/time\n/help\n/calc')    

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    z = items[2]
    y = int(items[3])
    if z == '+':
        await update.message.reply_text(f'{x} + {y} = {x + y}')
    elif z == '-':
        await update.message.reply_text(f'{x} - {y} = {x - y}')
    elif z == '*':
        await update.message.reply_text(f'{x} * {y} = {x * y}')
    elif z == '/':
        if y == 0:
            await update.message.reply_text(f'Нельзя делить на ноль!')
        else:
            await update.message.reply_text(f'{x} / {y} = {x / y}')        