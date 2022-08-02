#!/usr/bin/env python
# This program is dedicated to the public domain under the CC0 license.

from telegram import *

def android():
    text = """
    *Libérer son smarphone Android*

    En fonction de quel critère voulez-vous obtenir des informations ?
    """
    keyboard = [
        [
            InlineKeyboardButton("Niveau de connaissances", callback_data='ANDROID_NIVEAU'),
        ],
        [
            InlineKeyboardButton("100% libre", callback_data='ANDROID_LIBRE'),
            InlineKeyboardButton("Simple d'utilisation", callback_data='ANDROID_SIMPLE'),
        ],
        [
            InlineKeyboardButton("Axé vie privée", callback_data='ANDROID_PRIVACY'),
            InlineKeyboardButton("Axé sécurité", callback_data='ANDROID_SECURITE'),
        ],
        [
            InlineKeyboardButton("Article du Wiki", callback_data='TEASER'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_niveau():
    text = """
    *Libérer son smarphone Android → Par niveau*

    Êtes vous à l'aise à l'idée de déverouiller et installer un autre système vous-même sur votre téléphone ?
    """
    keyboard = [
        [
            InlineKeyboardButton("Pas du tout", callback_data='ANDROID_NIVEAU_0'),
        ],
        [
            InlineKeyboardButton("Oui si la manipulation est simple", callback_data='ANDROID_NIVEAU_1'),
        ],
        [
            InlineKeyboardButton("Oui, je suis à l'aise avec un terminal", callback_data='ANDROID_NIVEAU_2'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_niveau_zero():
    text = """
    *Libérer son smarphone Android → Par niveau → Débutant*

    Dans ce cas, préférez acheter un téléphone déjà configuré, ou demandez à une personne de confiance ayant le niveau pour configurer votre téléphone à votre place.

    Dans le cas où vous souhaitez acheter un téléphone déjà pré-configuré, nous vous suggérons ces systèmes libres :
    - /e/ OS, pour un téléphone dé-googlisé, respectueux de la vie privée et Français.
    - iodé OS, pour un téléphone dépourvu de traceurs, avec de nombreuses sécurités, également Français.

    + liste revendeurs de marmotte ( https://t.me/c/1781507019/291 )
    """
    keyboard = [
        [
            InlineKeyboardButton("Site de /e/OS", url='https://e.foundation'),
            InlineKeyboardButton("Site de iodéOS", url='https://iode.tech'),
        ],
        [
            InlineKeyboardButton("Site de GrapheneOS", url='https://grapheneos.org'),
            InlineKeyboardButton("Retour", callback_data='ANDROID_NIVEAU'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_niveau_un():
    text = """
    *Libérer son smarphone Android → Par niveau → Intermédiaire*

    Certains systèmes peuvent être installés en deux ou trois clics. Parmis eux :

    - Graphene OS, avec un installateur en ligne dans un navigateur, mais compatible uniquement pour les Google Pixel.
    - /e/ OS, avec leur outil "Easy installer", disponible pour un nombre limité de téléphones (certains Samsung, FairPhone, Pixel...).
    """
    keyboard = [
        [
            InlineKeyboardButton("Installer GrapheneOS", url='https://grapheneos.org/install/'),
        ],
        [
            InlineKeyboardButton("Easy Installer de /e/", url='https://doc.e.foundation/easy-installer'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID_NIVEAU'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_niveau_deux():
    text = """
    *Libérer son smarphone Android → Par niveau → Confirmé*

    Félicitations ! Vous allez pouvoir installer toutes les ROM. Rendez vous sur le Wikilibriste pour plus d'informations.
    Selon votre modèle de smartphone, certains systèmes alternatifs, les "customs ROM", ne seront pas disponibles pour votre téléphone.

    Cette opération peut "bricker" votre téléphone, le rendre inutilisable. Soyez attentifs, une ou deux mauvaises commandes suffisent.
    **Pensez à toujours sauvegarder vos données**
    """
    keyboard = [
        [
            InlineKeyboardButton("Article du Wiki", callback_data='TEASER'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID_NIVEAU'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_libre():
    text = """
    *Libérer son smarphone Android → 100% libre*

    La grande majorité des custom ROM sont libres. Mais certaines parties logicielles restent propriétaires, telles que la partition `vendor` et le firmware, qui permettent de faire la jonction entre le materiel et le système d'exploitation. Cela demande du travail supplémentaire, mais certains projets ont pour but de libérer complètement les téléphones.

    Attention, certains systèmes présentés ici sont des distributions Linux, et peuvent ne pas être compatibles avec les applications Android.
    """
    keyboard = [
        [
            InlineKeyboardButton("Replicant", url='https://www.replicant.us'),
            InlineKeyboardButton("Postmarket OS", url='https://postmarketos.org/'),
        ],
        [
            InlineKeyboardButton("Plasma Mobile", url='https://plasma-mobile.org/'),
            InlineKeyboardButton("Retour", callback_data='ANDROID'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_simple():
    text = """
    *Libérer son smarphone Android → Simple d'utilisation*

    Les distributions alternatives sont souvent développées par et pour les utilisateurs d'un niveau avancé. Heureusement, il en existe aussi pour les utilisateurs n'ayant pas de compétences particulières dans le domaine et souhaitant libérer son smartphone sans avoir besoin de changer ses habitudes. Voici notre sélection :
    """
    keyboard = [
        [
            InlineKeyboardButton("/e/ OS", url='https://e.foundation/'),
            InlineKeyboardButton("iodé OS", url='https://iode.tech/'),
        ],
        [
            InlineKeyboardButton("Calyx OS", url='https://calyxos.org/'),
            InlineKeyboardButton("Retour", callback_data='ANDROID'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_privacy():
    text = """
    *Libérer son smarphone Android → Vie privée*

    Les systèmes installés dans les téléphones du commerce sont remplis d'applications des GAFAM et BATX, invasives, remplies de traqueurs et de publicités... Le concept de vie privée semble inexistant. Heureusement, des distributions alternatives font de la vie privée de leurs utilisateurs une priorité. Voici notre sélection :
    """
    keyboard = [
        [
            InlineKeyboardButton("/e/ OS", url='https://e.foundation/'),
            InlineKeyboardButton("Graphene OS", url='https://grapheneos.org/'),
            InlineKeyboardButton("iodé OS", url='https://iode.tech/'),
        ],
        [
            InlineKeyboardButton("Calyx OS", url='https://calyxos.org/'),
            InlineKeyboardButton("Retour", callback_data='ANDROID'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_securite():
    text = """
    *Libérer son smarphone Android → Sécurité*

    Android est à la base, assez sécurisé, mais selon votre modèle de menace, vous pouvez avoir besoin de plus de sécurité.

    Trouvez le bon équilibre entre comodité et sécurité : plus un système est sécurisé, moins il est pratique et plus il est contraignant.

    Et si vous choisissez une autre distribution que celles mentionnées ici, regardez nos quelques conseils pour choisir une ROM qui ne fait pas impasse sur la sécurité.
    """
    keyboard = [
        [
            InlineKeyboardButton("Graphene OS", url='https://grapheneos.org/'),
            InlineKeyboardButton("Calyx OS", url='https://calyxos.org/'),
            InlineKeyboardButton("Replicant", url='https://www.replicant.us/'),
        ],
        [
            InlineKeyboardButton("Conseils", callback_data='ANDROID_SECURITE_CONSEILS'),
            InlineKeyboardButton("Retour", callback_data='ANDROID'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def android_securite_conseils():
    text = """
    *Libérer son smarphone Android → Sécurité → Conseils*

    Quelques points auxquels faire attention :
    - SeLinux doit être en mode "enforcing".
    - Le système doit être régulièrement mis à jour, pour inclure les patchs de sécurité récents.
    - Si possible, le bootloader doit être re-verrouillable (faites la manipulation seulement s'il est avéré qu'elle fonctionne avec votre appareil. Si ce n'est pas le cas, il y a un risque de blocage matériel du téléphone !).
    - Ne pas rooter votre appareil : c'est une porte ouverte aux virus !
    - Si possible, le téléphone doit être encore supporté et mis à jour par la marque.
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID_SECURITE'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)
