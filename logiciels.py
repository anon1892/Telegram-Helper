#!/usr/bin/env python
# This program is dedicated to the public domain under the CC0 license.

from telegram import *

def logiciels():
    text = """
    *Logiciels libres*

    Les logiciels libres sont gratuits et peuvent être utilisés, modifiés, audités, partagés par quiconque.
    Leur code source étant disponible, des développeurs du monde entier peuvent vérifier qu'ils ne contiennent pas de code suspect, de trackers ou de failles de sécurité, qui sont généralement corrigées plus vite que sur les logiciels propriétaires !

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
    return text,InlineKeyboardMarkup(keyboard)

def logiciels_web():
    text = """
    *Logiciels libres → Navigateur web*

    Les navigateurs web font partie des logiciels que nous utilisons le plus au quotidien. Il est donc primordial de bien le choisir et bien le configurer : les mauvais navigateurs pistent tous vos faits et gestes sur internet pour revendre ces informations à des régies publicitaires.

    Voici notre sélection :
    - Firefox : Disponible sur toutes les plateformes, c'est le navigateur libre et respectueux de la vie privée le plus utilisé. De nombreuses extensions (même sur mobile) vous permettent de le rendre encore plus privé et sécurisé.
    - Librewolf : Basé sur Firefox, renforcé au niveau sécurité et vie privée.
    - Tor Browser : Disponible sur toutes les plateformes et basé sur Firefox, il pousse le niveau de sécurité et de vie privée encore plus loin, et vous permet d'accèder au réseau homonyme.

    Sur Android : citons Mull et Bromite, respectivement basés sur Firefox et Chromium (libre, basé sur Chrome).

    Les navigateurs à banir :
    - Chrome, Safari, IE, Edge : Propriétaires, ouvert au tracking de toutes sortes, en lien avec les GAFAM.
    - Brave dans une moindre mesure.
    """
    keyboard = [
        [
            InlineKeyboardButton("Firefox", url='https://firefox.com/'),
            InlineKeyboardButton("Librewolf", url='https://librewolf.net/'),
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
    return text,InlineKeyboardMarkup(keyboard)

def logiciels_mail():
    text = """
    *Logiciels libres → Mails*

    Rappelez-vous : Les protocoles mails ont été créés avant l'Internet actuel, et l'accent n'a pas été mis sur la sécurité et la vie privée : un nombre important de métadonnées sont reliées au message, et même si ce dernier ne peut être lu, elles donnent un grand nombre d'informations à son sujet.
    Pour des conversations plus privées et sécurisées, tournez-vous vers des messageries instantanées chiffrées de bout en bout.
    """
    keyboard = [
        [
            InlineKeyboardButton("Fournisseurs de mails", callback_data='LOGICIELS_MAIL_PROVIDERS'),
            InlineKeyboardButton("Clients mails", callback_data='LOGICIELS_MAIL_CLIENTS'),
        ],
        [
            InlineKeyboardButton("Messageries instantanées", callback_data='LOGICIELS_MESSAGERIES'),
            InlineKeyboardButton("Retour", callback_data='LOGICIELS'),

        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def logiciels_mail_providers():
    text = """
    *Logiciels libres → Mails → Fournisseurs*

    Voici une sélection de fournisseurs mail sécurisés et respectueux de la vie privée :
    - Proton Mail : Tous niveaux, offres gratuites et payantes. Ne permet pas l'utilisation de clients mails autres que les leurs dans la version gratuite. Chiffrement automatique entre utilisateurs Proton uniquement basés en Suisse.
    - Tutanota : Concurrent à Proton Mail, basé en Allemagne. Permet le chiffrement systématique des mails.
    - Disroot : Association proposant un compte mail gratuit. Utilisable avec tous les clients mails (Thunderbird...), le chiffrement PGP doit être configuré et utilisé manuellement par l'utilisateur.
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
    return text,InlineKeyboardMarkup(keyboard)

def logiciels_mail_clients():
    text = """
    *Logiciels libres → Mails → Clients*

    Il existe de nombreux clients mails. Pour vous aider à choisir, voici notre sélection :
    - Thunderbird : Développé par la fondation Mozilla, il est devenu incontournable et disponible sur Linux en natif, Mac et Windows (bientot Android).
    - K9-Mail, FairEmail : Deux clients libres pour Android. Le premier deviendra "Thunderbird mobile".
    """
    keyboard = [
        [
            InlineKeyboardButton("Thunderbird", url='https://www.thunderbird.net/'),
            InlineKeyboardButton("K9-Mail", url='https://k9mail.app/'),
        ],
        [
            InlineKeyboardButton("FairEmail", url='https://email.faircode.eu/'),
            InlineKeyboardButton("Retour", callback_data='LOGICIELS_MAIL'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def logiciels_messageries():
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
    return text,InlineKeyboardMarkup(keyboard)

def logiciels_vpn():
    text = """
    *Logiciels libres → VPN*

    Depuis quelques temps, on entend parler partout de VPN, censés nous rendre invulnérables fasses aux menaces et complètement anonymes. Oui et non.

    Un VPN fait transiter toutes les connexions de votre appareil par un serveur distant, et chiffre les flux entre les deux. Cela permet de masquer son adresse IP, contourner la censure, obtenir plus de sécurité sur un réseau WiFi public (non chiffrés). En revanche, il faut avoir entière confiance au fournisseur de VPN : Toutes les connexions de votre appareil passent par leurs serveurs, et peuvent donc vous surveiller. La plupart des VPN le font pour faire du profit, et parce qu'elles y sont contraites légalement ! Évitez les VPN basés dans un des pays des "14 eyes".

    Nous vous recommandons :
    - Proton VPN : Basé en Suisse, propose une offre gratuite (illimité, 3 pays) et plusieurs offres payantes.
    - Mullvad : Propose uniquement une offre payante. Basé en Suède (14 eyes), mais ne demande aucune information personnelle, et déclare ne pas en collecter.
    Note : les autres solutions de VPN (NordVPN, Cyberghost...) sont toutes à plus ou moins grande échelle suspectés de collecter les logs. Il n'est donc plus recommandé de souscrire à ces offres. En effet, ces sociétés sont rachetées les unes les autres par des grands groupes dont les intérêts sont à priori obscures.

    Même si ce n'est pas un VPN à proprement parler, le réseau Tor peut être une bonne alternative, même si ses mécanismes rendent les performances de navigation grandement dégradées.
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
    return text,InlineKeyboardMarkup(keyboard)

def logiciels_cloud():
    text = """
    *Logiciels libres → Services Cloud*

    Vous souhaitez vous libérer de l'emprise des GAFAM sur vos données dans le Cloud sans perdre les avantages de ce dernier ?
    Plusieurs solutions existent :
    1. Vous pouvez migrer vos données vers un hébergeur plus vertueux, ne revendant pas vos données et utilisant des logiciels libres. Parmis eux :
    - Disroot, basé sur Nextcloud et hébergé par une association aux Pays-Bas (14 eyes)
    - Murena, basé sur Nextcloud, hébergé en France (9 eyes) par l'entreprise homonyme, qui développe le système /e/ pour Android.

    2. Si vous voulez apprendre à héberger vos données vous même (self hosting en anglais), nous vous conseillons :
    - Nextcloud, libre et très complet, une multitude de modules sont disponibles pour le paramètrer à votre guise.
    - Yunohost permet d'héberger soi même de nombreux services, dont Nextcloud, sans avoir besoin de connaissances particulières.
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
    return text,InlineKeyboardMarkup(keyboard)
