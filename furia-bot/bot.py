from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from commands import (
    noticias, resultados, redes, proxima_partida, simulador_torcida,
    live_status, contato_inteligente, gritar, vaiar, cantar, aleatoriedades
)
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📰 Notícias", callback_data="noticias"),
         InlineKeyboardButton("🏆 Resultados", callback_data="resultados")],
        [InlineKeyboardButton("📅 Próximo Jogo", callback_data="proximajogo"),
         InlineKeyboardButton("🎤 Simular Torcida", callback_data="torcida")],
        [InlineKeyboardButton("📡 Live Status", callback_data="livestatus"),
         InlineKeyboardButton("🎯 Aleatoriedades", callback_data="aleatoriedades")],
        [InlineKeyboardButton("📱 Redes Sociais", callback_data="redes"),
         InlineKeyboardButton("📲 Contato Inteligente", callback_data="contato_inteligente")],
        [InlineKeyboardButton("🛒 Loja FURIA", url="https://furia.gg")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎮 *Bem-vindo ao Bot da FURIA!*\n"
        "Aqui você encontra as últimas notícias, resultados, e muito mais sobre o nosso time!\n\n"
        "👇 *Escolha uma opção:*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# /menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📰 Notícias", callback_data='noticias'),
         InlineKeyboardButton("🏆 Últimos Resultados", callback_data='resultados')],
        [InlineKeyboardButton("📅 Próxima Partida", callback_data='proximajogo'),
         InlineKeyboardButton("🎤 Simular Torcida", callback_data='torcida')],
        [InlineKeyboardButton("📡 Live Status", callback_data="livestatus"),
         InlineKeyboardButton("🎯 Aleatoriedades", callback_data="aleatoriedades")],
        [InlineKeyboardButton("📱 Redes Sociais", callback_data="redes"),
         InlineKeyboardButton("📲 Contato Inteligente", callback_data="contato_inteligente")],
        [InlineKeyboardButton("🛒 Loja FURIA", url="https://furia.gg")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)

# Handler de botões
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'noticias':
        await noticias(query, context)
    elif query.data == 'resultados':
        await resultados(query, context)
    elif query.data == 'redes':
        await redes(query, context)
    elif query.data == 'proximajogo':
        await proxima_partida(query, context)
    elif query.data == 'torcida':
        await simulador_torcida(query, context)
    elif query.data == 'livestatus':
        await live_status(query, context)
    elif query.data == 'contato_inteligente':
        await contato_inteligente(query, context)
    elif query.data == "gritar":
        await gritar(query, context)
    elif query.data == "vaiar":
        await vaiar(query, context)
    elif query.data == "cantar":
        await cantar(query, context)
    elif query.data == "aleatoriedades":
        await aleatoriedades(query, context)

# Iniciar o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Bot iniciado!")
    app.run_polling()
