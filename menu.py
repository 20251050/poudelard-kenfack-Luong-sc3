from Chapitres.chapitre_1 import *
from Chapitres.chapitre_2 import *
from Chapitres.chapitre_3 import *
from Chapitres.chapitre_4 import lancer_chapitre4_quidditch
from utils.input_utils import *

def afficher_menu_principal():
    print ("MENU PRINCIPAL")
    choix = demander_choix("Votre choix : ",["Lancer le Chapitre 1 – L'arrivée dans le monde magique","Quitter le jeu"])
    return choix

def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
    continuer = True
    while continuer:
        choix = afficher_menu_principal()
        if str(choix) == "1":
          personnage = lancer_chapitre_1()
          lancer_chapitre_2(personnage)
          lancer_chapitre_3(personnage,maisons)
          lancer_chapitre4_quidditch(personnage, maisons)
        elif str(choix) == "2":
            print("Merci d'avoir joué. À bientôt dans le monde magique ")
            continuer = False
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")