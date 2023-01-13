from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from processor import *

app = ApplicationBuilder().token("5791856739:AAFaNPsCtWrGyESOEGshIAAG5g_fFUYmcss").build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'''Привет, {update.effective_user.first_name}!  
Хотите поиграть с другом в крестики-нолики?
Выбери:
/help - для получения помощи. 
/play - для начала игры''')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('''Игра рассчитана на дових людей. 
Первый игрок - крестики,
второй игрок - нолики. Игру начинают крестики.
/start - для выхода в главное меню,
/play - запуск игры''')

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('''Первыми ходят крестики, 
далее ход автоматически переходит к ноликам и так до конца игры. Выберите клеточку для хода.
''', reply_markup = choice)
     

app.add_handler(CommandHandler('start', start))

app.add_handler(CommandHandler('help', help))

app.add_handler(CommandHandler('play', play))


print('бот обновлён')

app.run_polling()