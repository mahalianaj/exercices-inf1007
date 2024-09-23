#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    # TODO completer la fonction ici
    diff = abs(ord("A")-ord("a"))
    nouv_mot = ""
    for letter in mot:
        nouv_mot += chr(ord(letter) - diff)
    
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
