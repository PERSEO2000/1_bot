import logging,random
from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackQueryHandler,ContextTypes,CommandHandler,filters,MessageHandler,CallbackQueryHandler
from telegram.ext._utils.types import UD


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
keyBoard = ReplyKeyboardMarkup([["DISNEY","NETFLIX","HBO"]],resize_keyboard=True)
teclado = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("SI",callback_data="si"),InlineKeyboardButton("NO",callback_data="no")]
    ]
)

async def callbacks(update: Update,context:CallbackQueryHandler):
    if update.callback_query.data == "si":
        await update.callback_query.edit_message_text(text="Los usuario sabran que esta cuenta funciona")
    elif update.callback_query.data == "no":
        await update.callback_query.edit_message_text(text="los usuario sabran que esta cuenta no funciona")
async def disney(update: Update,context: ContextTypes.DEFAULT_TYPE):
    with open("./cuentas.txt","r") as cuenta:
        cuentas = cuenta.read().split("\n")
        cuenta_disney = cuentas[random.randint(0,len(cuentas) - 1)].split(":")
        await context.bot.send_message(chat_id=update.effective_chat.id,text=f"Si esta cuenta te piede verificar correo electronico o la contraseña no es la misma tienes que solicitar una cuenta nueva a GenTO las veces que quieras hasta que encuentres una cuenta valida\n\nemail: {cuenta_disney[0]}\npassword: {cuenta_disney[1]}\n\nPorfavor selecciona [ SI ] si esta cuenta te a funcionado de lo contrario selecciona [ NO ]",reply_markup=teclado)
async def netflix(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="PROXIMAMENTE")
async def start(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text=f"{update.effective_user.name} Ahora puedes elegir tu cuenta",reply_markup=keyBoard)
    await context.bot.send_message(chat_id=6562888035,text=f"El usuario { update.effective_user.name } a interactuado conmigo su ID es {update.effective_chat.id}")

if __name__ == "__main__":
    app = ApplicationBuilder().token("6657215547:AAFDES9CqkuhcNsK1-_yiM94vGFDWgpqUrk").build()
    disney_handler = MessageHandler(callback=disney,filters=filters.Text("DISNEY"))
    netflix_handler = MessageHandler(callback=netflix,filters=filters.Text("NETFLIX"))
    commands = CommandHandler("start",start)
    app.add_handler(commands)
    app.add_handler(disney_handler)
    app.add_handler(netflix_handler)
    app.add_handler(CallbackQueryHandler(callbacks))
    app.run_polling()
