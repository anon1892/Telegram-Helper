#!/usr/bin/env python
# This program is dedicated to the public domain under the CC0 license.

from telegram import *

def start_data():
    text = """
    Bonjour, à quel sujet voulez-vous des renseignements ?
    """
    keyboard = [
        [
            InlineKeyboardButton("Libérer mon Android", callback_data='ANDROID'),
            InlineKeyboardButton("Libérer mon iPhone", callback_data='IOS'),
        ],
        [
            InlineKeyboardButton("Libérer mon PC", callback_data='PC'),
            InlineKeyboardButton("Libérer mon Mac", callback_data='MAC'),
        ],
        [
            InlineKeyboardButton("Logiciels libres", callback_data='LOGICIELS'),
            InlineKeyboardButton("Foire aux questions", callback_data='FAQ'),
        ],
        [
            InlineKeyboardButton("Quitter", callback_data='EXIT'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def fourteen_eyes():
    text = """
    *14 eyes*

    Les 5, 9 et 14 eyes sont une même alliance de renseignements faisant coopérer les pays membres pour assurer la collecte de renseignements électromagnétiques. Edward Snowden la décrit comme "une agence de renseignement supra-nationale qui ne répond pas aux lois de ses propres pays membres".

    Initialement, 5 pays, les 5 eyes :
    Australie, Canada, Nouvelle Zélande, Angleterre et États-Unis.

    Viennent se rajouter 4 pays pour former les 9 eyes :
    Danemark, Pays-Bas, France et Norvège

    Et les 14 eyes sont formés avec en plus :
    Belgique, Allemagne, Italie, Espagne et Suède

    Pays collaborant avec l'alliance mais n'en faisant pas partie officiellement :
    Japon, Israel, Corée du Sud, Singapour
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='LOGICIELS_VPN'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def teaser():
    text = """
    *Article du wiki*

    Le wiki "Wikilibriste" est encore en phase bêta. Un peu de patience, il sera bientot prêt !
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def erreur():
    text = """
    *Mais pas si vite !*

    Désolé, cette partie n'a pas encore été créée. N'hésitez pas à nous faire part de vos commentaires et contribuer si vous le pouvez !
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)
