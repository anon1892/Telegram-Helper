#!/usr/bin/env python
# This program is dedicated to the public domain under the CC0 license.

from telegram import *

def pc():
    text = """
    *Libérer mon PC*

    La meilleure manière de libérer un ordinateur personnel (PC) est d'installer une distribution Linux à la place de Windows.
    Certaines distributions Linux ressemblent fortement à Windows, et la plupart des applications disponibles sur Windows le sont également sous Linux. Si elles ne le sont pas, vous trouverez certainement une alternative qui offre des fonctionnalités très similaires.
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
    return text,InlineKeyboardMarkup(keyboard)

def pc_linux():
    text = """
    *Libérer mon PC → Déjà sous Linux*

    Beau travail ! 🎉
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
    return text,InlineKeyboardMarkup(keyboard)

def pc_linux_install():
    text = """
    *Libérer mon PC → Installer Linux*

    Bravo. Vous souhaitez installer Linux sur votre PC, mais un problème se pose : quelle distribution choisir ?
    En effet, il existe pléthore de distributions, avec chacune ses spécificités. Voici une sélection :
    """
    keyboard = [
        [
            InlineKeyboardButton("Pour débutants", callback_data='PC_LINUX_INSTALL_DEBUTANT'),
            InlineKeyboardButton("Pour initiés", callback_data='PC_LINUX_INSTALL_INITIE'),
            InlineKeyboardButton("Pour confirmés", callback_data='PC_LINUX_INSTALL_CONFIRME'),
        ],
        [
            InlineKeyboardButton("Sécurité/anonymat", callback_data='PC_LINUX_INSTALL_SECURITE'),
            InlineKeyboardButton("Article du wiki", callback_data='TEASER'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='PC'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def pc_linux_install_debutant():
    text = """
    *Libérer mon PC → Installer Linux → Débutant*

    Pour les débutants, nous vous conseillons Zorin OS et Ubuntu, des distributions très faciles à utiliser au quotidien. Ubuntu possède une grande communauté francophone, qui saura vous aider en cas de pépin. Fedora, avec l'environnement Gnome ressemble beaucoup à Ubuntu, et est de plus en plus conseillé à la place d'Ubuntu.
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
    return text,InlineKeyboardMarkup(keyboard)

def pc_linux_install_initie():
    text = """
    *Libérer mon PC → Installer Linux → Initiés*

    Nombreux sont les initiés qui utilisent quotidiennement les distributions présentées pour les débutants (Zorin, Ubuntu et Fedora Workstation). Mais pour ceux qui veulent découvrir de nouvelles distributions :
    - Linux Mint - Distribution basée sur Ubuntu, se veut élégante et confortable, à la fois puissante et facile d'utilisation.
    - Pop! OS - Elle aussi basée sur Ubuntu, est développée par l'entreprise Américaine System76 pour ses ordinateurs, mais peut être installée sur un grand nombre d'autres.
    - Elementary OS - Basée sur Ubuntu, se veut simple d'utilisation avec peu de besoins d'accèder à la console, et graphiquement proche de Mac OS, avec une cohérence entre les applications.
    - Manjaro - Basée sur Arch Linux, se veut simple d'utilisation et est en rolling release", la publication est continue.
    """
    keyboard = [
        [
            InlineKeyboardButton("Linux Mint", url='https://linuxmint.com/'),
            InlineKeyboardButton("Pop! OS", url='https://pop.system76.com/'),
            InlineKeyboardButton("Elementary OS", url='https://elementary.io/'),
        ],
        [
            InlineKeyboardButton("Manjaro", url='https://manjaro.org/'),
            InlineKeyboardButton("Retour", callback_data='PC_LINUX_INSTALL'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def pc_linux_install_confirme():
    text = """
    *Libérer mon PC → Installer Linux → Confirmé*

    Nombreux sont les utilisateurs confirmés qui utilisent quotidiennement les distributions présentées pour les débutants et initiés. Mais pour ceux qui veulent découvrir de nouvelles distributions :
    - Debian - Distribution très stable à la base de nombreuses autres (dont Ubuntu) et très personnalisable. Possède une grande communauté. Distribution de premier choix pour les serveurs : Très stable, et les logiciels, même s'ils ne sont pas forcément dans leur dernière version, ont rapidement les patchs de sécurité.
    - Fedora Silverblue - Une version de Fedora spécifiquement créée pour les conteneurs : le système est immuuable, ce qui renforce la sécurité.
    - Arch Linux - Distribution très appréciée des barbus, car permet d'être extrèmement customisable : elle ne contient que ce que vous y installez.
    - Red Hat - Aussi connue sous l'acronyme RHEL pour RedHat Entreprise Linux, est à la base de Fedora et est orientée vers le marché commercial et les serveurs d'entreprise.
    - MX Linux et antiX - Basées sur Debian, sont optimisées pour les vieux ordinateurs. Distributions conseillées pour donner une seconde vie à du vieux matériel !
    - openSUSE, Garuda Linux... La liste est longue, car la voie est libre ;)
    """
    keyboard = [
        [
            InlineKeyboardButton("Debian", url='https://www.debian.org/'),
            InlineKeyboardButton("Fedora Silverblue", url='https://silverblue.fedoraproject.org/'),
            InlineKeyboardButton("Arch Linux", url='https://archlinux.org/'),
        ],
        [
            InlineKeyboardButton("Red Hat", url='http://www.redhat.com/rhel'),
            InlineKeyboardButton("MX Linux", url='https://mxlinux.org/'),
            InlineKeyboardButton("antiX", url='https://antixlinux.com/'),
        ],
        [
            InlineKeyboardButton("DistroWatch", url='https://distrowatch.com/'),
            InlineKeyboardButton("Retour", callback_data='PC_LINUX_INSTALL'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)

def pc_linux_install_securite():
    text = """
    *Libérer mon PC → Installer Linux → Sécurtié*

    Voici les distributions Linux avec un maximum de sécurité :
    - Qubes OS est destiné aux utilisateurs avancés, avec une sécurité maximale. Son principe repose sur la virtualisation et la contenairisation.
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
    return text,InlineKeyboardMarkup(keyboard)

def pc_windows():
    text = """
    *Libérer mon PC → Rester sur Windows*

    Windows, est le système propriétaire le plus connu et développé par un GAFAM, qui s'emploie donc à pister ses utilisateurs et est devenu une proie de choix pour les attaquants...
    Pourquoi ne pas franchir le pas vers Linux ?

    Si malgré tout, vous souhaitez rester sur Windows, voici quelques astuces :
    - Utilisez au maximum les logiciels libres : ils ne vous pistent pas, et sont tous disponibles sous Linux, si vous prévoyez de tenter l'expérience.
    - Utilisez Windows sans compte Microsoft
    - Utilisez au minimum les applications et services de Microsoft
    - Installez un bloqueur de tracking, et paramétrez les extensions de votre navigateur avec Ublock et AdGuard au minimum
    - Paramétrez vos DNS privés
    """
    keyboard = [
        [
            InlineKeyboardButton("Logiciels libres", callback_data='LOGICIELS'),
        ],
        [
            InlineKeyboardButton("Retour", callback_data='PC'),
        ],
    ]
    return text,InlineKeyboardMarkup(keyboard)
