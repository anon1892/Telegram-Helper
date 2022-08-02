#!/usr/bin/env python
# This program is dedicated to the public domain under the CC0 license.

from telegram import *

def ios():
    text = """
    *Libérer son iPhone*

    Malheureusement, Apple ne permet pas de libérer son iPhone. iOS est un système propriétaire, mais Apple pousse le bouchon encore plus loin : c'est directement au niveau matériel qu'Apple crée un réseau Wifi maillé qui en permanance, borne et communique avec les autres appareils Apple qu'il rencontre. Niveau vie privée, difficile de faire pire. De plus, Apple verrouille le système avec le kit de développement imposé aux developpeurs et rend les iPhones impossibles à utiliser sans Apple ID.

    Nous vous conseillons d'acquérir un smartphone avec un système Android dé-googlisé, qui vous coutera par ailleurs bien moins cher qu'un iPhone.
    """
    keyboard = [
        [
            InlineKeyboardButton("Libérer un smartphone Android", callback_data='ANDROID_NIVEAU'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def mac():
    text = """
    *Libérer son Mac*

    Mac OS est un système propriétaire, et Apple fait tout pour fermer son système. Deux options s'offrent à vous : Installer une distribution Linux ou rester sous Mac OS et le configurer afin d'appliquer une politique sécurité optimale.
    """
    keyboard = [
        [
            InlineKeyboardButton("Installer Linux", callback_data='MAC_LINUX'),
        ],
        [
            InlineKeyboardButton("Configurer Mac OS", callback_data='MAC_RESTER'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def mac_linux():
    text = """
    *Libérer son Mac → Installer Linux*

    Depuis quelques années, avec leur nouvelle gamme de processeurs, Apple rend de plus en plus difficile le passage à Linux. Pour faire simple, la manipulation pour installer Linux sur les Mac d'avant 2016 est simple, mais après cette date, cela demande des connaissances poussées : certaines fonctionnalités sont manquantes, notamment la Touchbar qui possède sa propre puce, elle aussi propriétaire et donc difficile à étudier et libérer. Certains projets sont en cours de développement, mais encore trop jeunes pour être utilisés par le grand public.

    Plus d'informations concernant l'installation de Linux sur les Mac d'avant 2016 sont à venir :)
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='MAC'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def mac_rester():
    text = """
    *Libérer son Mac → Rester sous Mac OS*

    Si vous voulez rester sur Mac OS, ou ne pouvez pas installer Linux à cause d'un matériel trop récent (>2016), voici quelques pistes pour améliorer votre vie privée :
    - Ne configurez jamais l'Apple ID.
    - Installez uniquement des applications au format DMG, et de préférence des logiciels libres.
    - Pour limiter la remontée de données, installez le pare-feu Lulu.
    """
    keyboard = [
        [
            InlineKeyboardButton("Logiciels libres", callback_data='LOGICIELS'),
            InlineKeyboardButton("Pare-feu Lulu", url='https://github.com/objective-see/LuLu'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='MAC'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)
