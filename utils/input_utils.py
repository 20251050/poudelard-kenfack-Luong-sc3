def demander_texte (message) :
    texte = input(message).strip()
    while texte == "":
        texte = input(message).strip()
    return texte

def demander_nombre(message, min_val=None, max_val=None):
    valide = False
    nombre = None
    while not valide:
        saisie = input(message).strip()
        if saisie == "":
            print("Veuillez entrer un nombre.")
            continue
        negatif = False
        i = 0
        if saisie[0] == '-':
            negatif = True
            i = 1
        est_valide = True
        for c in saisie[i:]:
            if c < '0' or c > '9':
                est_valide = False
        if not est_valide:
            print("Entrée invalide. Veuillez saisir un nombre entier.")
            continue
        nombre = 0
        for c in saisie[i:]:
            nombre = nombre * 10 + (ord(c) - ord('0'))
        if negatif:
            nombre = -nombre
        if min_val is not None and nombre < min_val:
            print(f"Le nombre doit être au moins {min_val}.")
        elif max_val is not None and nombre > max_val:
            print(f"Le nombre doit être au maximum {max_val}.")
        else:
            valide = True
    return nombre

def demander_choix(message, options) :
    print(message)
    for i in range(len(options)) :
        a = int(len (options))
        print(i+1,". ", options[i])
        choix = demander_nombre("Votre choix : ",1,int(a))
    return choix

import json

def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    return donnees