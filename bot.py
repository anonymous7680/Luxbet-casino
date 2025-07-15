import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurer le logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Remplace par ton token obtenu via BotFather
TOKEN = '7652460240:AAFoiQE_VgCvL1omsb2qa3eO8bk7fzBwqnk'

# URL de ta mini-app hébergée (doit être HTTPS)
MINI_APP_URL = 'https://your-hosted-mini-app-url.com'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envoie un message de bienvenue avec un bouton pour ouvrir la mini-app."""
    keyboard = [
        [InlineKeyboardButton("Ouvrir la Mini-App", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Bienvenue ! Clique sur le bouton ci-dessous pour ouvrir la mini-app :",
        reply_markup=reply_markup
    )

def main() -> None:
    """Lance le bot."""
    # Créer l'application avec le token
    application = Application.builder().token(TOKEN).build()

    # Ajouter les handlers de commande
    application.add_handler(CommandHandler("start", start))

    # Lancer le bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
