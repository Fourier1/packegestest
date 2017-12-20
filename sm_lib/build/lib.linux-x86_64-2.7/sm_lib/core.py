#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implémentation de la proclamation de la bonne parole.
    Usage:
    from sm_lib import proclamer
    proclamer()
"""
from datetime import datetime

# __all__ contient les noms de tour ce qu'on autorise a importer depuis ce module
__all__ = ['proclamer']


def proclamer():
    """
    ecriture d'un pacquet en python
    celle fonction affiche une proclamation
    :return: 
    """
    print(
        "[%s] Fourier & Sam & Max, C\'est bien notre premier test de creation de packeges en pythhon " % datetime.now())


if __name__ == '__main__':
    proclamer()
