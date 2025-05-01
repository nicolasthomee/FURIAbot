from telegram import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
import random

# 📰 Notícias
async def noticias(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_photo(
        photo="https://i.imgur.com/4M34hi2.jpeg",
        caption="📰 Última notícia: FURIA revela novo uniforme!"
    )

# 🏆 Resultados
async def resultados(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_text(
        "🏆 Últimos 3 jogos:\n- FURIA 2x1 NAVI\n- FURIA 0x2 Vitality\n- FURIA 2x0 MIBR"
    )

# 📱 Redes Sociais
async def redes(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_text(
        "📱 Siga a FURIA:\n"
        "- Instagram: https://instagram.com/furiagg\n"
        "- Twitter: https://twitter.com/FURIA\n"
        "- YouTube: https://youtube.com/@FURIAgg\n"
        "- Twitch: https://twitch.tv/team/furia\n"
        "- TikTok: https://tiktok.com/@furiagg"
    )

# 📅 Próxima Partida
async def proxima_partida(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_text(
        "📅 A próxima partida da FURIA será contra a NAVI no dia 28/04 às 18h! 🔥"
    )

# 🎤 Simulador de Torcida
async def simulador_torcida(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🙌 FURIAAAA!", callback_data="gritar"),
            InlineKeyboardButton("😤 UUUUHHHH!", callback_data="vaiar"),
            InlineKeyboardButton("🎶 ÔÔÔÔÔ, FURIA!", callback_data="cantar")
        ]
    ])
    await query.message.reply_text(
        "🎤 Simulador de Torcida ativado!\nEscolha uma reação:",
        reply_markup=keyboard
    )

# 📡 Live Status (fictício)
async def live_status(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_text(
        "📡 Status ao vivo:\n"
        "FURIA 1 x 0 NAVI\n"
        "Rodada 12/30 – Em andamento...\n\n"
        "🔫 KSCERATO está destruindo! 😎"
    )

# 📲 Contato Inteligente (WhatsApp)
async def contato_inteligente(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_text(
        "📲 Para falar com o atendimento inteligente da FURIA:\n"
        "👉 https://wa.me/5511993404466"
    )

# Reações do Simulador
async def gritar(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_text("🙌 FUUUUURIAAAA! 🔥🔥🔥")

async def vaiar(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_text("😤 UUUUUUHHHHHHHH!!! 👎👎")

async def cantar(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    await query.message.reply_text("🎶 ÔÔÔÔÔÔ, FURIA! ÔÔÔÔÔÔ! 🎵")

# 🎯 Aleatoriedades (Curiosidades + Frases)
async def aleatoriedades(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    curiosidades = [
        "A FURIA foi fundada em 2017 por Jaime Pádua e André Akkari.",
        "O nome 'FURIA' representa a garra e agressividade dos jogadores.",
        "A organização já participou de majors importantes do CS:GO.",
        "O estilo de jogo agressivo da FURIA é reconhecido mundialmente."
    ]

    frases = [
        "“Aqui é FURIA, irmão!” 🔥",
        "“Respeita a camisa!” 😤",
        "“Foco, força e FURIA!” 💪",
        "“Só a bala educa.” 💥",
        "“Vamo que vamo, com sangue nos olhos!” 🧠"
    ]

    todas = curiosidades + frases
    escolha = random.choice(todas)

    await query.message.reply_text(f"🎯 *Aleatoriedade do dia:*\n\n_{escolha}_", parse_mode="Markdown")
