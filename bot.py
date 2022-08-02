#!/usr/bin/env python
# This program is dedicated to the public domain under the CC0 license.

"""
 Basé sur https://git.io/JOmFw.
"""

import logging
import os

from telegram import *
from telegram.ext import *

from android import *
from apple import *
from pc import *
from logiciels import *
from misc import *
from faq import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    text, reply_markup = start_data()
    update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def text(query, content):
    query.edit_message_text(content[0], reply_markup=content[1], parse_mode="Markdown")

def photo(update, context):
    if update.callback_query.data[6:] == "MESSAGERIES":
        photo = "messageries.jpg"
    else:
        photo = "CPT.png"
    keyboard = [[InlineKeyboardButton("Fermer", callback_data='FERMER'),],]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_message.chat_id, photo=open(photo, 'rb'), reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    if query.data == 'ANDROID':
        text(query, android())
    elif query.data == 'ANDROID_NIVEAU':
        text(query, android_niveau())
    elif query.data == 'ANDROID_NIVEAU_0':
        text(query, android_niveau_zero())
    elif query.data == 'ANDROID_NIVEAU_1':
        text(query, android_niveau_un())
    elif query.data == 'ANDROID_NIVEAU_2':
        text(query, android_niveau_deux())
    elif query.data == 'ANDROID_LIBRE':
        text(query, android_libre())
    elif query.data == 'ANDROID_SIMPLE':
        text(query, android_simple())
    elif query.data == 'ANDROID_PRIVACY':
        text(query, android_privacy())
    elif query.data == 'ANDROID_SECURITE':
        text(query, android_securite())
    elif query.data == 'ANDROID_SECURITE_CONSEILS':
        text(query, android_securite_conseils())
    elif query.data == 'IOS':
        text(query, ios())
    elif query.data == 'MAC':
        text(query, mac())
    elif query.data == 'MAC_LINUX':
        text(query, mac_linux())
    elif query.data == 'MAC_RESTER':
        text(query, mac_rester())
    elif query.data == 'PC':
        text(query, pc())
    elif query.data == 'PC_LINUX':
        text(query, pc_linux())
    elif query.data == 'PC_LINUX_INSTALL':
        text(query, pc_linux_install())
    elif query.data == 'PC_LINUX_INSTALL_DEBUTANT':
        text(query, pc_linux_install_debutant())
    elif query.data == 'PC_LINUX_INSTALL_INITIE':
        text(query, pc_linux_install_initie())
    elif query.data == 'PC_LINUX_INSTALL_CONFIRME':
        text(query, pc_linux_install_confirme())
    elif query.data == 'PC_LINUX_INSTALL_SECURITE':
        text(query, pc_linux_install_securite())
    elif query.data == 'PC_WINDOWS':
        text(query, pc_windows())
    elif query.data == 'LOGICIELS':
        text(query, logiciels())
    elif query.data == 'LOGICIELS_WEB':
        text(query, logiciels_web())
    elif query.data == 'LOGICIELS_MAIL':
        text(query, logiciels_mail())
    elif query.data == 'LOGICIELS_MAIL_CLIENTS':
        text(query, logiciels_mail_clients())
    elif query.data == 'LOGICIELS_MAIL_PROVIDERS':
        text(query, logiciels_mail_providers())
    elif query.data == 'LOGICIELS_MESSAGERIES':
        text(query, logiciels_messageries())
    elif query.data == 'LOGICIELS_VPN':
        text(query, logiciels_vpn())
    elif query.data == 'FOURTEEN_EYES':
        text(query, fourteen_eyes())
    elif query.data == 'LOGICIELS_CLOUD':
        text(query, logiciels_cloud())
    elif query.data == 'FAQ':
        text(query, faq())
    elif query.data == 'FAQ_PIXEL':
        text(query, faq_pixel())
    elif query.data == 'TEASER':
        text(query, teaser())
    elif query.data[:5] == 'PHOTO':
        photo(update, context)
    elif query.data == 'START':
        text(query, start_data())
    elif query.data == 'EXIT':
        query.edit_message_text("À bientot !")
    elif query.data == 'FERMER':
        query.delete_message();
    else:
        erreur(query)

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Pour lancer une conversation, entrez /aide")

def main() -> None:
    """Run the bot."""

    updater = Updater("TOKEN")

    updater.dispatcher.add_handler(CommandHandler('aide', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('start', help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
