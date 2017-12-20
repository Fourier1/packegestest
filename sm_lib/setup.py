#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Lefichier setup contient les fonctions qui vonx installer votre pacquet
    
"""
from setuptools import setup, find_packages
import sm_lib

setup(
    # le nome de la bibliotheque tel qu'il apparaitra sur pipy
    name='sm_lib',
    # la version du pacquet
    version=sm_lib.__version__,
    # liste tous les pacquet a insérer des dans la diistribution
    # au lieu de la faire a la main on utilise la fonction (find_packages())
    # qui se fera recursivement dans le dossier courant
    packages=find_packages(),
    # nom de l'auteur
    author="Saint Fourier",
    # votre email sachant qu'il sera publier et public et visible pas tous le monde
    # avec les risque que ça implique
    author_email="fouriersaint@gmail.com",
    # coute description
    description="Proclamer la parole de Sam & Max",
    # long description sera affichier pour presenté la lib générale
    long_description=open('README.md').read(),
    # actoiver la prise en compte du fichier MENIFEST.in
    include_package_data=True,
    # une url qui pointe vers la page officiel de votre lib
    url="https://github.com/Fourier1/packegestest.git",
    # spécifier des regles pour le contenu
    classifiers=[
        "Programming Language :: Python",
        "Developpement Status :: 1 - Plannig",
        "Licence :: OSI Approved",
        "Natural Language :: Frensh",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communication",
    ],

    # Pour creer un system de plugin
    # Pour creer une commande comme "django-admin"
    # Dans notre cas si on veu creer une commande tel que "proclame-sm"
    # on a qu' a faire pointer ce nom vers la fonction proclame()
    # la syntaxe est la suivante : "nom-de-la-commande-a-creer = packeges.module.fonction"
    entry_points={
        'console_scripts': [
            'proclam-sm = sm_lib.core:proclamer',
        ],
    },

    # A fournir uniquement si votre licence n'est pas listée dans "classivier"
    licence="WTFPL",

)
