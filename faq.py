#!/usr/bin/env python
# This program is dedicated to the public domain under the CC0 license.

from telegram import *

def faq():
    text = """
    *Foire aux questions*

    Cetaines questions reviennent régulièrement sur le groupe. Cette section a pour but de regrouper les réponses.
    """
    keyboard = [
        [
            InlineKeyboardButton("Pourquoi les Google Pixel ?", callback_data='FAQ_PIXEL'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def faq_pixel():
    text = """
    *Pourquoi les Google Pixel*

    Ça s'explique par le modèle du Pixel, pour lequel on n'a pas besoin de changer le recovery pour accéder au chargeur d'amorçage (bootloader). Tous les autres fabricants verrouillent le bootloader en mettant leur propre recovery. D'où le fait d'installer TWRP - Team Win Recovery Project -, pour changer le système sur les marques tierces, et ne pas nécessairement pouvoir re-verrouiller le bootloader.
    Exception faite pour les téléphones sous Android One, comme ça avait été le cas pour le Xiaomi MIA2.
    De plus, la puce Titan a son intérêt : le chiffrement fait en local et implémente un mécanisme anti-forensics (plus on fait des tentatives erronées d'intrusion, plus le téléphone est verrouillé longtemps)
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='FAQ'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)
