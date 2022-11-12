from telegram import Update, ReplyKeyboardMarkup
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
    await update.message.reply_text('/hi\n/time\n/help\n/calc_complex')    

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)

    # пока не знаю, как выяснить, какую кнопку нажал пользователь
    reply_keyboard = [['Операция с рациональными числами'], ['Операция с комплесными числами'], ['Завершить работу']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True)
    await update.message.reply_text('Выберите вид операции', reply_markup = markup_key)
    # код выше добавлен для тестирования работы кнопок

    msg = update.message.text
    items = msg.split()

    if len(items) == 4:
        x = float(items[1])
        z = items[2]
        y = float(items[3])
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
    else:
        await update.message.reply_text(f'После /calc нужно ввести два числа, разделённых знаком операции.')

async def calc_complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)

    msg = update.message.text # пример: -5+3j + 4+2j = (-1+5j)
    items = msg.split()

    if len(items) == 4:
        x = complex(items[1])
        z = items[2]
        y = complex(items[3])
        if z == '+':
            await update.message.reply_text(f'{x} + {y} = {x + y}')
        elif z == '-':
            await update.message.reply_text(f'{x} - {y} = {x - y}')
        elif z == '*':
            await update.message.reply_text(f'{x} * {y} = {x * y}')
        elif z == '/':
            await update.message.reply_text(f'{x} / {y} = {x / y}')   
    else:
        await update.message.reply_text(f'После /calc_complex нужно ввести два комлексных числа, разделённых знаком операции.')        