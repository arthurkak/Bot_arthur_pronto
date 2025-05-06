
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

def get_tabela():
    return """
@arthur.vendas01 - Tabela do Arthurzin

Golds com world sale:
- 10k: R$1,50
- 20k: R$2,50
- 30k: R$3,50

Golds sem world sale:
- 90k: R$3,65
- 100k: R$4,00
- 150k: R$4,25
- 200k: R$4,50
- 250k: R$4,75
- 300k: R$5,00
- 350k: R$5,25
- 400k: R$5,50
- 450k: R$5,75
- 500k: R$6,00

Money:
- 10M: R$1,00
- 20M: R$2,00
- 30M: R$3,00
- 40M: R$4,00
- 50M: R$5,00

Desbloqueios:
- W16: R$4,00
- Fumaça: R$3,50
- Todos os carros pagos: R$3,50
- Todos os carros de gold: R$2,00
- Casa paga: R$4,00
- Buzinas pagas: R$5,00
- Sirene em todos os carros: R$4,00
- King: R$3,50
- Nome RGB: R$2,00
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bem-vindo ao bot de vendas do Arthurzin!")
    await update.message.reply_text(get_tabela())

async def comprar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Golds", callback_data='gold')],
        [InlineKeyboardButton("Money", callback_data='money')],
        [InlineKeyboardButton("Desbloqueios", callback_data='desbloqueios')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Escolha o que deseja comprar:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'gold':
        await query.edit_message_text("Para comprar gold, envie: /pedido gold 100k")
    elif query.data == 'money':
        await query.edit_message_text("Para comprar money, envie: /pedido money 50M")
    elif query.data == 'desbloqueios':
        await query.edit_message_text("Para desbloquear algo, envie: /pedido desbloquear W16")

ADMIN_ID = 7763795103

async def pedido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = ' '.join(context.args)
    await update.message.reply_text(f"Seu pedido foi registrado: {texto}
Um vendedor entrará em contato em breve!")
    if ADMIN_ID:
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"Novo pedido de @{update.effective_user.username or 'usuário'}: {texto}")

app = ApplicationBuilder().token("7574937721:AAH8uxU-T95ChxUy2_fLiOmkHtDjXlKCzHw").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("comprar", comprar))
app.add_handler(CommandHandler("pedido", pedido))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
