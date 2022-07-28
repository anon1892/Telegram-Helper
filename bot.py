#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
 Basé sur https://git.io/JOmFw.
"""

import logging
import os

from telegram import *
from telegram.ext import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def android(query) -> None:
    text = """
    *Libérer son smarphone Android*

    En fonction de quel critère voulez-vous obtenir des informations ?
    """
    keyboard = [
        [
            InlineKeyboardButton("Niveau de connaissances", callback_data='ANDROID_NIVEAU'),
        ],
        [
            InlineKeyboardButton("Modèle de menaces", callback_data='ANDROID_MENACES'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def android_niveau(query) -> None:
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
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def android_niveau_zero(query) -> None:
    text = """
    *Libérer son smarphone Android → Par niveau → Débutant*

    Dans ce cas, préférez acheter un téléphone déjà configuré, ou demandez à une personne de confiance ayant le niveau pour configurer votre téléphone à votre place.

    Dans le cas où vous souhaitez acheter un téléphone déjà configuré, nous vous suggerons deux systèmes libres :
    - /e/, pour un téléphone dé-googlisé, respectueux de la vie privée et Français.
    - GrapheneOS, pour un téléphone avec une vie privée et une sécurité maximale.
    """
    keyboard = [
        [
            InlineKeyboardButton("Site de /e/", url='https://e.foundation'),
        ],
        [
            InlineKeyboardButton("Site de GrapheneOS", url='https://grapheneos.org/'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID_NIVEAU'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def android_niveau_un(query) -> None:
    text = """
    *Libérer son smarphone Android → Par niveau → Intermédiaire*

    Certains systèmes peuvent être installés en deux ou trois clics. Parmis eux :

    - GrapheneOS, avec un installateur en ligne, mais compatible uniquement avec les Pixels.
    - /e/, avec leur outil "Easy installer", disponible pour un nombre limité de téléphones.
    """
    keyboard = [
        [
            InlineKeyboardButton("Quel système choisir ?", callback_data='QUELLE_ROM'),
        ],
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
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def android_niveau_deux(query) -> None:
    text = """
    *Libérer son smarphone Android → Par niveau → Confirmé*

    Selon votre modèle de smartphone, certains systèmes alternatifs, les "customs ROM" ne seront pas disponibles pour votre téléphone.
    Nous vous conseillons trois systèmes : GrapheneOS, CalyxOS et /e/. Les deux premiers ne supportent à quelques exceptions près que les Pixel de Google. /e/ supporte plus de 270 téléphones.
    Cette opération peut "briquer" votre téléphone, le rendre inutilisable. Soyez attentifs, une ou deux mauvaises commandes suffisent. Pensez à toujours sauvegarder vos données.
    """
    keyboard = [
        [
            InlineKeyboardButton("Quel système choisir ?", callback_data='QUELLE_ROM'),
        ],
        [
            InlineKeyboardButton("Modèles supportés par GrapheneOS", url='https://grapheneos.org/faq#supported-devices'),
        ],
        [
            InlineKeyboardButton("Modèles supportés par CalyxOS", url='https://calyxos.org/install/'),
        ],
        [
            InlineKeyboardButton("Modèles supportés par /e/", url='https://doc.e.foundation/devices'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID_NIVEAU'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def android_menaces(query) -> None:
    text = """
    *Libérer son smarphone Android → Par menace*

    Votre modèle de menaces est-il élevé ?

    Attention, il faut trouver le bon équilibre entre comodité et sécurité : Plus un système est sécurisé, moins il est pratique.
    """
    keyboard = [
        [
            InlineKeyboardButton("Oui", callback_data='ANDROID_MENACES_OUI'),
        ],
        [
            InlineKeyboardButton("Non", callback_data='ANDROID_MENACES_NON'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def android_menaces_oui(query) -> None:
    text = """
    *Libérer son smarphone Android → Menaces → Élevées*

    GrapheneOS est le système d'exploitation basé sur Android le plus sécurisé à l'heure actuelle : Renforcement des sécurités, sandboxing, lootloader re-verouillable, chiffrement du stockage, reglage plus fin des permissions...
    """
    keyboard = [
        [
            InlineKeyboardButton("Aller sur leur site", url='https://grapheneos.org/'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID_MENACES'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def android_menaces_non(query) -> None:
    text = """
    *Libérer son smarphone Android → Menaces → Modérées*

    Quelques points auquels faire attention :
    - SeLinux doit être en mode "enforcing".
    - Le système doit être régulièrement mis à jour, pour inclure les patchs de sécurité récents.
    - Si possible, le bootloader doit être re-verouillable (faites la manipulation seulement s'il est avéré qu'elle fonctionne avec votre appareil. Si ce n'est pas le cas, vous pouvez le briquer !).
    - Ne pas rooter votre appareil.
    - Si possible, le téléphone doit être encore supporté et mis à jour par la marque.

    Niveau de sécurité, dans l'ordre décroissant : GrapheneOS, CalyxOS, DivestOS, /e/ ...
    """
    keyboard = [
        [
            InlineKeyboardButton("Quel système choisir ?", callback_data='QUELLE_ROM'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID_MENACES'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def quelle_rom(query) -> None:
    text = """
    *Libérer son smarphone Android → Quel OS choisir ?*

    Il existe énormément de custom ROM, avec chacunes ses avantages et inconvénients. Nous vous en conseillons quatres :
    - GrapheneOS, pour un téléphone avec une vie privée et une sécurité maximale. Pixels uniquement.
    - /e/, simple à utiliser, pour un téléphone dé-googlisé, respectueux de la vie privée et Français. +270 appareils.
    - CalyxOS, à mi-chemin entre les deux, se veut simple d'utilisation tout en reprennant de nombreuses fonctionnalités de GrapheneOS pour la sécurité. Pixels uniquement.
    - DivestOS, basé sur LineageOS pour supporter de nombreux appareils, axé vie privée et sécurité, en reprennant des fonctionnalités de Graphene. Pour utilisateur averti.
    """
    keyboard = [
        [
            InlineKeyboardButton("Site de GrapheneOS", url='https://grapheneos.org'),
        ],
        [
            InlineKeyboardButton("Site de /e/", url='https://e.foundation'),
        ],
        [
            InlineKeyboardButton("Site de CalyxOS", url='https://calyxos.org'),
        ],
        [
            InlineKeyboardButton("Site de DivestOS", url='https://divestos.org'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='ANDROID'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def ios(query) -> None:
    text = """
    *Libérer son iPhone*

    Malheureusement, Apple ne permet pas de libérer son iPhone. iOS est un système propriétaire, mais Apple pousse le bouchon encore plus loin : C'est directement au niveau matériel qu'Apple crée un réseau Wifi maillé qui en permanance, borne et communique avec les autres appareils Apple qu'il rencontre. Niveau vie privée, difficile de faire pire. De plus, Apple verouille le système avec le kit de développement imposé aux developpeurs et rend les iPhones impossibles à utiliser sans Apple ID.

    Nous vous conseillons d'aquérir un smartphone sous un système Android dé-googlisé, qui vous coutera par ailleurs bien moins cher qu'un iPhone.
    """
    keyboard = [
        [
            InlineKeyboardButton("Libérer un smartphone Android", callback_data='ANDROID_NIVEAU'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def mac(query) -> None:
    text = """
    *Libérer son Mac*

    Mac OS est un système propriétaire, et Apple fait tout pour fermer son système. Deux options s'offrent à vous : Installer une distribution Linux ou rester sous Mac OS et le configurer.
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
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def mac_linux(query) -> None:
    text = """
    *Libérer son Mac → Installer Linux*

    Depuis quelques années, avec leur nouvelle gamme de processeurs, Apple rend de plus en plus difficile le passage à Linux. Pour faire simple, la manipulation pour installer Linux sur les Mac d'avant 2016 est simple, mais après cette date, cela demande des connaissances poussées : Certaines fonctionnalités sont manquantes, notamment la Touchbar qui possède sa propre puce, elle aussi propriétaire et donc difficile à étudier et libérer. Certains projets sont en cours de développement, mais encore trop jeunes pour être utilisés par le grand public.

    Plus d'informations concernant l'installation de Linux sur les Mac d'avant 2016 sont à venir :)
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='MAC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def mac_rester(query) -> None:
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
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def pc(query) -> None:
    text = """
    *Libérer mon PC*

    La meilleure manière de libérer un PC est d'installer une distribution Linux à la place de Windows. Certaines distributions Linux ressemblent fortement à Windows, et la plupart des applications sont également disponibles sous Linux, ou une alternative libre.

    """
    keyboard = [
        [
            InlineKeyboardButton("Je suis déjà sous Linux", callback_data='PC_LINUX'),
        ],
        [
            InlineKeyboardButton("Je souhaite installer Linux", callback_data='PC_LINUX_INSTALL'),
        ],
        [
            InlineKeyboardButton("Je veux rester sous Windows", callback_data='PC_WINDOWS'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def pc_linux(query) -> None:
    text = """
    *Libérer mon PC → Déjà sous Linux*

    Bon travail ! 🎉
    Nous ajouterons certainement des informations ici. En attendant, nous vous proposons une sélection de logiciels libres.
    """
    keyboard = [
        [
            InlineKeyboardButton("Liste de logiciels libres", callback_data='LOGICIELS'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='PC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def pc_linux_install(query) -> None:
    text = """
    *Libérer mon PC → Installer Linux*

    Bien. Vous souhaitez installer Linux sur votre PC, mais un problème se pose : Quelle distribution choisir ?
    En effet, il en existe pléthore de distributions, avec chacune ses spécificités. Voici nos sélections :
    """
    keyboard = [
        [
            InlineKeyboardButton("Pour les débutants", callback_data='PC_LINUX_INSTALL_DEBUTANT'),
            InlineKeyboardButton("Pour les initiés", callback_data='PC_LINUX_INSTALL_INITIE'),
        ],
        [
            InlineKeyboardButton("Sécurité/anonymat", callback_data='PC_LINUX_INSTALL_SECURITE'),
            InlineKeyboardButton("Article du wiki", callback_data='TEASER'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='PC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def pc_linux_install_debutant(query) -> None:
    text = """
    *Libérer mon PC → Installer Linux → Débutant*

    Pour les débutants, nous vous conseillons Zorin OS et Ubuntu, des distributions très faciles à utiliser au quotidien. Ubuntu possède une grande communauté francophone, qui saura vous aider en cas de pépin. Fedora, avec l'environnement Gnome ressemble beaucoup à Ubuntu, et est régulièrement conseillé à la place d'Ubuntu.
    """
    keyboard = [
        [
            InlineKeyboardButton("Zorin OS", url='https://zorin.com/os/'),
            InlineKeyboardButton("Ubuntu", url='https://www.ubuntu-fr.org/'),
            InlineKeyboardButton("Fedora", url='https://getfedora.org/fr/workstation/'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='PC_LINUX_INSTALL'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def pc_linux_install_initie(query) -> None:
    text = """
    *Libérer mon PC → Installer Linux → Initié*

    Nombreux sont les initiés qui utilisent quotidiennement les distributions présentées pour les débutants (Zorin, Ubuntu et Fedora Workstation). Mais pour ceux qui veulent découvrir de nouvelles distributions :
    - Fedora Silverblue : Une version de Fedora spécifiquement créée pour les conteneurs : Le système est immuuable, ce qui renforce la sécurité.
    - Arch Linux : Distribution très appréciée des barbus, car permet d'être extrèmement customisable : Elle ne contient que ce que vous y installez.
    """
    keyboard = [
        [
            InlineKeyboardButton("Fedora Silverblue", url='https://silverblue.fedoraproject.org/'),
            InlineKeyboardButton("Arch Linux", url='https://archlinux.org/'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='PC_LINUX_INSTALL'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def pc_linux_install_securite(query) -> None:
    text = """
    *Libérer mon PC → Installer Linux → Sécurtié*

    Voici les distributions Linux avec un maximum de sécurité :
    - Qubes OS est destiné aux utilisateurs avancés, avec une sécurité maximale.
    - Tails est une distribution imumuable, qui revient à l'identique à chaque redémarrage. Toutes les connexions passent par le réseau Tor.
    - Whonix est un système d'exploitation étanche qui fonctionne par dessus celui que vous utilisez.
    """
    keyboard = [
        [
            InlineKeyboardButton("Qubes OS", url='https://www.qubes-os.org/'),
            InlineKeyboardButton("Tails", url='https://tails.boum.org/'),
            InlineKeyboardButton("Whonix", url='https://www.whonix.org/'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='PC_LINUX_INSTALL'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def pc_windows(query) -> None:
    text = """
    *Libérer mon PC → Rester sur Windows*

    Windows, système propriétaire dévellopé par un GAFAM, qui piste ses utilisateurs et en proie à de nombreux virus... Pourquoi ne pas franchir le pas vers Linux ?

    Si malgré tout, vous souhaitez rester sous Windows, voici quelques astuces :
    - Utilisez au maximum les logiciels libres : Ils ne vous pistent pas, et sont tous disponibles sous Linux, si vous prévoyez de tenter l'expérience.
    - Utilisez Windows sans compte Micro$oft
    - Utilisez au minimum les applications et services de Microsoft
    - Installez un bloqueur de tracking
    """
    keyboard = [
        [
            InlineKeyboardButton("Logiciels libres", callback_data='LOGICIELS'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='PC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels(query) -> None:
    text = """
    *Logiciels libres*

    Les logiciels libres sont gratuits et peuvent être utilisés, modifiés, audités, partagés par quiconque. Leur code source étant disponible, des développeurs du monde entier peuvent vérifier qu'ils ne contiennent pas de virus, trackers et failles de sécurité, quis sont généralement corrigées plus vite que sur les logiciels propriétaires !

    Sélectionnez une catégorie pour plus d'informations et notre sélection.
    """
    keyboard = [
        [
            InlineKeyboardButton("Navigateur web", callback_data='LOGICIELS_WEB'),
            InlineKeyboardButton("Mails", callback_data='LOGICIELS_MAIL'),
        ],
        [
            InlineKeyboardButton("VPN", callback_data='LOGICIELS_VPN'),
            InlineKeyboardButton("Services Cloud", callback_data='LOGICIELS_CLOUD'),
        ],
        [
            InlineKeyboardButton("Messageries instantanées", callback_data='LOGICIELS_MESSAGERIES'),
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels_web(query) -> None:
    text = """
    *Logiciels libres → Navigateur web*

    Les navigateurs web font partie des logiciels que nous utilisons le plus au quotidien. Il est donc primordial de bien le choisir et bien le configurer : Les mauvais navigateurs pistent tous vos faits et gestes sur internet pour revendre ces informations à des régies publicitaires.

    Voici notre sélection :
    - Firefox : Disponible sur toutes les plateformes, c'est le navigateur libre et respectueux de la vie privée le plus utilisé. De nombreuses extensions (même sur mobile) vous permettent de le rendre encore plus privé et sécurisé.
    - Tor Browser : Disponible sur toutes les plateformes et basé sur Firefox, il pousse le niveau de sécurité et de vie privée encore plus loin, et vous permet d'accèder au réseau homonyme.
    - Sur Android, citons également Mull et Bromite, respectivement basés sur Firefox et Chromium (libre, basé sur Chrome).

    Les navigateurs à banir :
    - Chrome, Safari, Edge : Propriétaires, appartiennent aux GAFAM.
    """
    keyboard = [
        [
            InlineKeyboardButton("Firefox", url='https://firefox.com/'),
            InlineKeyboardButton("Tor Browsr", url='https://www.torproject.org/download/'),
        ],
        [
            InlineKeyboardButton("Mull", url='https://f-droid.org/en/packages/us.spotco.fennec_dos/'),
            InlineKeyboardButton("Bromite", url='https://github.com/bromite/bromite'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='LOGICIELS'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels_mail(query) -> None:
    text = """
    *Logiciels libres → Mails*

    Rappelez-vous : Les protocoles mails ont été créés avant l'Internet actuel, et l'accent n'a pas été mis sur la sécurité et la vie privée. Il est donc important d'utiliser autant que possible le chiffrement PGP. Malgré ces précautions, un nombre important de métadonnées sont reliées au message, et même si ce dernier ne peut être lu, elles donnent un grand nombre d'informations à son sujet. Pour des conversations plus privées et sécurisées, tournez-vous vers des messageries instantanées chiffrées de bout en bout.
    """
    keyboard = [
        [
            InlineKeyboardButton("Fournisseurs de mails", callback_data='LOGICIELS_MAIL_PROVIDERS'),
            InlineKeyboardButton("Clients mails", callback_data='LOGICIELS_MAIL_CLIENTS'),
        ],
        [
            InlineKeyboardButton("Messageries instantanées", callback_data='LOGICIELS_MESSAGERIES'),
        ],
        [
            InlineKeyboardButton("Chiffrement PGP", callback_data='LOGICIELS_MAIL_PGP'),
            InlineKeyboardButton("Retour", callback_data='LOGICIELS'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels_mail_providers(query) -> None:
    text = """
    *Logiciels libres → Mails → Fournisseurs*

    Voici une sélection de fournisseurs mail sécurisés et respectueux de la vie privée :
    - Proton Mail : Tous niveaux, offres gratuites et payantes. Ne permet pas l'utilisation de clients mails autres que les leurs dans la version gratuite. Chiffrement automatique entre utilisateurs Proton uniquement Basé en Suisse.
    - Tutanota : Concurrent à Proton Mail, basé en Allemagne.
    - Disroot : Association proposant un compte mail gratuit. Utilisable avec tous les clients mail, le chiffrement PGP doit être configuré et utilisé manuellement par l'utilisateur.
    """
    keyboard = [
        [
            InlineKeyboardButton("Proton Mail", url='https://proton.me/'),
            InlineKeyboardButton("Tutanota", url='https://tutanota.com/'),
            InlineKeyboardButton("Disroot", url='https://disroot.org/fr'),
        ],
        [
            InlineKeyboardButton("Chiffrement PGP", callback_data='LOGICIELS_MAIL_PGP'),
            InlineKeyboardButton("Retour", callback_data='LOGICIELS_MAIL'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels_mail_clients(query) -> None:
    text = """
    *Logiciels libres → Mails → Clients*

    Il existe de nombreux clients mails. Pour vous aider à choisir, voici notre sélection :
    - Thunderbird : Développé par la fondation Mozilla, est devenu incontournable et disponible sur Linux, Mac et Windows (bientot Android).
    - K9-Mail, FairEmail : Deux clients libres pour Android. Le premier va devenir "Thunderbird mobile".
    """
    keyboard = [
        [
            InlineKeyboardButton("Thunderbird", url='https://www.thunderbird.net/'),
            InlineKeyboardButton("K9-Mail", url='https://k9mail.app/'),
            InlineKeyboardButton("FairEmail", url='https://email.faircode.eu/'),
        ],
        [
            InlineKeyboardButton("Chiffrement PGP", callback_data='LOGICIELS_MAIL_PGP'),
            InlineKeyboardButton("Retour", callback_data='LOGICIELS_MAIL'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels_mail_pgp(query) -> None:
    text = """
    *Logiciels libres → Mails → PGP*

    Cette section est encore vide. Si vous en avez les capacités, merci de contribuer :)
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='LOGICIELS'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels_messageries(query) -> None:
    text = """
    *Logiciels libres → Messageries instantanées*

    Voici une liste succincte, que nous détaillerons ultérieurement.
    Une infographie détaille quelles données sont collectées par les principales applications de messagerie instantanées.
    """
    keyboard = [
        [
            InlineKeyboardButton("Session", url='https://getsession.org/'),
            InlineKeyboardButton("Signal", url='https://signal.org/'),
            InlineKeyboardButton("Matrix", url='https://element.io/'),
            InlineKeyboardButton("XMPP", url='https://xmpp.org/'),
        ],
        [
            InlineKeyboardButton("Données collectées", callback_data='PHOTO_MESSAGERIES'),
            InlineKeyboardButton("Retour", callback_data='LOGICIELS'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels_vpn(query) -> None:
    text = """
    *Logiciels libres → VPN*

    Depuis quelques temps, on entend parler partout de VPN, censés nous rendre invulnérables fasses aux menaces et complètement anonymes. Oui et non.

    Un VPN fait transiter toutes les connexions de votre appareil par un serveur distant, et chiffre les flux entre les deux. Cela permet de masquer son adresse IP, contourner la censure, obtenir plus de sécurité sur un réseau WiFi public (non chiffrés). En revanche, il faut avoir entière confiance au fournisseur de VPN : Toutes les connexions de votre appareil passent par leurs serveurs, et peuvent donc vous surveiller. La plupart des VPN le font pour faire du profit, et parce qu'elles y sont contraites légalement ! Évitez les VPN basés dans un des pays des "14 eyes".

    Nous vous recommandons :
    - Proton VPN : Basé en Suisse, propose une offre gratuite (illimité, 3 pays) et plusieurs offres payantes.
    - Mullvad : Propose uniquement une offre payante. Basé en Suède (14 eyes), mais ne demande aucune information personnelle, et déclare ne pas en collecter.
    Même si ce n'est pas un VPN à proprement parler, le réseau Tor peut être une bonne alternative.
    """
    keyboard = [
        [
            InlineKeyboardButton("Proton VPN", url='https://protonvpn.com/'),
            InlineKeyboardButton("Mullvad", url='https://mullvad.net/'),
            InlineKeyboardButton("Tor", url='https://www.torproject.org/'),
        ],
        [
            InlineKeyboardButton("14 eyes", callback_data='FOURTEEN_EYES'),
            InlineKeyboardButton("Retour", callback_data='LOGICIELS'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def fourteen_eyes(query) -> None:
    text = """
    *14 eyes*

    Les 5, 6, 9 et 14 eyes sont une même alliance de renseignements faisant coopérer les pays membres pour assurer la collecte de renseignements électromagnétiques. Edward Snowden la décrit comme "une agence de renseignement supranationale qui ne répond pas aux lois de ses propres pays membres".

    Initialement, 5 pays, les 5 eyes :
    Australie, Canada, Nouvelle Zélande, Angleterre et États-Unis.

    Viennent se rajouter 4 pays pour former les 9 eyes :
    Danemark, Pays-Bas, France et Norvège

    Et les 1' eyes sont formés avec en plus :
    Belgique, Allemagne, Italie, Espagne et Suède

    Pays collaborant avec l'alliance mais n'en faisant pas partie officiellement :
    Japon, Israel, Corée du Sud, Singapour
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='LOGICIELS_VPN'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def logiciels_cloud(query) -> None:
    text = """
    *Logiciels libres → Services Cloud*

    Vous souhaitez vous libérer de l'emprise des GAFAM sur vos données dans le Cloud sans perdre les avantages de ce dernier ? Plusieurs solutions existent.

    1. Vous pouvez migrer vos données vers un hébergeur plus vertueux, ne revendant pas vos données et utilisant des logiciels libres. Parmis eux :
    - Disroot, basé sur Nextcloud et hébergé par une association aux Pays-Bas (14 eyes)
    - Murena, basé sur Nextcloud, hébergé en France (9 eyes) par l'entreprise homonyme, qui développe le système /e/ pour Android.

    2. Si vous voulez apprendre à héberger vos données vous même (self hosting en anglais), nous vous conseillons :
    - Nextcloud, libre et très complet, une multitude de modules sont disponibles pour le paramètrer à votre guise.
    - Yunohost permet de héberger sois-même de nombreux services, dont Nextcloud, sans avoir besoin de connaissances particulières.
    """
    keyboard = [
        [
            InlineKeyboardButton("Disroot", url='https://disroot.org/fr/#services'),
            InlineKeyboardButton("Murena", url='https://murena.com/cloud/'),
        ],
        [
            InlineKeyboardButton("Nextcloud", url='https://disroot.org/fr/#services'),
            InlineKeyboardButton("Yunohost", url='https://yunohost.org/#/index_fr'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='LOGICIELS'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def teaser(query) -> None:
    text = """
    *Article du wiki*

    Le wiki "Wikilibriste" est encore en phase bêta. Un peu de patience, il sera bientot prêt !
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

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
            InlineKeyboardButton("Libérer mon mac", callback_data='MAC'),
        ],
        [
            InlineKeyboardButton("Logiciels libres", callback_data='LOGICIELS'),
            InlineKeyboardButton("Quitter", callback_data='EXIT'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return text, reply_markup

def restart(query) -> None:
    text, reply_markup = start_data()
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def start(update: Update, context: CallbackContext) -> None:
    text, reply_markup = start_data()
    update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def photo(update, context):
    if update.callback_query.data[6:] == "MESSAGERIES":
        photo = "messageries.jpg"
    else:
        photo = "CPT.png"
    keyboard = [[InlineKeyboardButton("Fermer", callback_data='FERMER'),],]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_message.chat_id, photo=open(photo, 'rb'), reply_markup=reply_markup)

def erreur(query) -> None:
    text = """
    *Mais pas si vite !*

    Désolé, cette partie n'a pas encore été créée. N'hésitez pas à nous faire part de vos commentaires et contribuer si vous le pouvez !
    """
    keyboard = [
        [
            InlineKeyboardButton("Retour", callback_data='START'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    if query.data == 'ANDROID':
        android(query)
    elif query.data == 'ANDROID_NIVEAU':
        android_niveau(query)
    elif query.data == 'ANDROID_NIVEAU_0':
        android_niveau_zero(query)
    elif query.data == 'ANDROID_NIVEAU_1':
        android_niveau_un(query)
    elif query.data == 'ANDROID_NIVEAU_2':
        android_niveau_deux(query)
    elif query.data == 'ANDROID_MENACES':
        android_menaces(query)
    elif query.data == 'ANDROID_MENACES_OUI':
        android_menaces_oui(query)
    elif query.data == 'ANDROID_MENACES_NON':
        android_menaces_non(query)
    elif query.data == 'QUELLE_ROM':
        quelle_rom(query)
    elif query.data == 'IOS':
        ios(query)
    elif query.data == 'PC':
        pc(query)
    elif query.data == 'PC_LINUX':
        pc_linux(query)
    elif query.data == 'PC_LINUX_INSTALL':
        pc_linux_install(query)
    elif query.data == 'PC_LINUX_INSTALL_DEBUTANT':
        pc_linux_install_debutant(query)
    elif query.data == 'PC_LINUX_INSTALL_INITIE':
        pc_linux_install_initie(query)
    elif query.data == 'PC_LINUX_INSTALL_SECURITE':
        pc_linux_install_securite(query)
    elif query.data == 'PC_WINDOWS':
        pc_windows(query)
    elif query.data == 'MAC':
        mac(query)
    elif query.data == 'MAC_LINUX':
        mac_linux(query)
    elif query.data == 'MAC_RESTER':
        mac_rester(query)
    elif query.data == 'LOGICIELS':
        logiciels(query)
    elif query.data == 'LOGICIELS_WEB':
        logiciels_web(query)
    elif query.data == 'LOGICIELS_MAIL':
        logiciels_mail(query)
    elif query.data == 'LOGICIELS_MAIL_CLIENTS':
        logiciels_mail_clients(query)
    elif query.data == 'LOGICIELS_MAIL_PROVIDERS':
        logiciels_mail_providers(query)
    elif query.data == 'LOGICIELS_MAIL_PGP':
        logiciels_mail_pgp(query)
    elif query.data == 'LOGICIELS_MESSAGERIES':
        logiciels_messageries(query)
    elif query.data == 'LOGICIELS_VPN':
        logiciels_vpn(query)
    elif query.data == 'FOURTEEN_EYES':
        fourteen_eyes(query)
    elif query.data == 'LOGICIELS_CLOUD':
        logiciels_cloud(query)
    elif query.data == 'TEASER':
        teaser(query)
    elif query.data[:5] == 'PHOTO':
        photo(update, context)
    elif query.data == 'START':
        restart(query)
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
