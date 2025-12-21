def demander_texte (message) :
    texte = input(message).strip()
    while texte == "":
        texte = input(message).strip()
    return texte

def demander_nombre(message, min_val=None, max_val=None):
    saisie = input(message)
    if not saisie:
        print("Veuillez entrer un nombre.".format(min_val, max_val))
        return demander_nombre(message, min_val, max_val)
    index = 0
    signe = 1
    est_valide = True
    resultat = 0
    if saisie[0] == '-':
        signe = -1
        index = 1
    if len(saisie) == index:
        est_valide = False
    else:
        for i in range(index, len(saisie)):
            if not ('0' <= saisie[i] <= '9'):
                est_valide = False
            resultat = resultat * 10 + (ord(saisie[i]) - ord('0'))
    if not est_valide:
        return demander_nombre(message, min_val, max_val)
    nombre = resultat * signe
    if min_val is not None and nombre < min_val:
        print("Veuillez entrer un nombre entre {} et {}.".format(min_val, max_val))
        return demander_nombre(message, min_val, max_val)
    if max_val is not None and nombre > max_val:
        print("Veuillez entrer un nombre entre {} et {}.".format(min_val, max_val))
        return demander_nombre(message, min_val, max_val)
    return nombre

def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(i+1,'. ',options[i],)
    choix = demander_nombre("Votre choix : ", 1, len(options))
    return choix

import json

def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    return donnees