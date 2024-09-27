from turtle import update
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logg import logging

app = ApplicationBuilder().token("").build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info(f"start {update.effective_user.first_name}")
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! ' +  
        'Я твой мини-калькулятор.\n Выбери:\n /help - для получения помощи.\n' +  
        '/calc - для начала работы с калькулятором.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('''Я - маленький калькулятор,
     который поможет вам выполнять простые действия между двумя числами.
     Пожалуйста, следуйте инструкции и у вас обязательно всё получится.
     /start - для выхода в главное меню,
     /calc - запуск калькулятора
     ''')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('''Какое действие вы хотите выполнить?
    /sum - сложение (введите команду и два числа через пробел. Например: "/sum 3 56"
    /sub - вычитание
    /multi - умножение
    /div1 - деление с остатком
    /div2 - целочисленное деление
    /div3 - остаток от деления
    /pow - возведение в степень
    ''')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    items = message.split()
    x = float(items[1])
    y = float(items[2])
    op = items[0]
    if op == "/sum":
        txt = f'{x} + {y} = {x + y}'
    elif op == "/sub":
        txt = f'{x} - {y} = {x - y}'
    elif op ==  "/multi":
        txt = f'{x} * {y} = {x * y}'
    elif op == "/div1":
        txt = f'{x} / {y} = {x / y}'
    elif op == "/div2":
        txt = f'{x} / {y} = {x // y}'
    elif op == "/div3":
        txt = f'Остаток от {x} при делении на {y} равен {x % y}'
    elif op == "/pow":
            txt = f'{x} ^ {y} = {x ** y}'
    logging.info(f'{txt}')
    await update.message.reply_text(txt)


app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("help", help))

app.add_handler(CommandHandler("calc", calc))

app.add_handler(CommandHandler("sum", menu))
app.add_handler(CommandHandler("sub", menu))
app.add_handler(CommandHandler("multi", menu))
app.add_handler(CommandHandler("div1", menu))
app.add_handler(CommandHandler("div2", menu))
app.add_handler(CommandHandler("div3", menu))
app.add_handler(CommandHandler("pow", menu))

print("бот обновлён")

app.run_polling()
