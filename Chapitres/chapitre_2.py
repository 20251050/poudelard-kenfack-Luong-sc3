import json

from univers.personnage import afficher_personnage
from utils.input_utils import demander_nombre
from univers.maison import repartition_maison
def rencontrer_amis (joueur):
    D = joueur["Attributs"]
    avant = {}
    for cle in D:
        avant[cle] = D[cle]
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...\n")
    input()
    print("Un garçon roux entre dans votre compartiment, l’air amical.\n — Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?\n Que répondez-vous ?\n 1. Bien sûr, assieds-toi !\n 2. Désolé, je préfère voyager seul.")
    choix = demander_nombre("Votre choix : ", 1, 2)
    if choix == 1:
        D["loyauté"] += 1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
    else:
        D["ambition"] += 1
    input()
    print("\nUne fille entre ensuite, portant déjà une pile de livres.\n — Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?\n 1. Oui, j’adore apprendre de nouvelles choses !\n 2. Euh… non, je préfère les aventures aux bouquins.")
    choix = demander_nombre("Votre choix : ", 1, 2)
    if choix == 1:
        D["intelligence"] += 1
    else:
        D["courage"] += 1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour !")
    input()
    print("\nPuis un garçon blond entre avec un air arrogant.\n — Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès départ, tu ne crois pas ?\n Comment réagissez-vous ?\n 1. Je lui serre la main poliment.\n 2. Je l’ignore complètement.\n 3. Je lui réponds avec arrogance.")
    choix = demander_nombre("Votre choix : ", 1, 3)
    if choix == 1:
        D["ambition"] += 1
    elif choix == 2:
        D["loyauté"] += 1
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
    else:
        D["courage"] += 1
    print("\nLe train continue sa route. Le château de Poudlard se profile à l’horizon...\n Tes choix semblent déjà en dire long sur ta personnalité !")
    attributs_modifies = {}
    for cle in D.keys () :
        if D[cle] != avant[cle]:
            attributs_modifies[cle] = D[cle]
    print("Tes attributs mis à jour :", attributs_modifies)

def mot_de_bienvenue():
    print("— Bienvenue à Poudlard. Que cette année soit riche en découvertes.\n — Que le festin commence !")
    input()

def ceremonie_repartition(joueur):
    print("La cérémonie de répartition commence dans la Grande Salle...\n Le Choixpeau magique t’observe longuement avant de poser ses questions :\n")
    questions = [("Tu vois un ami en danger. Que fais-tu ?",["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]),
                ("Quel trait te décrit le mieux ?",["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]),
                ("Face à un défi difficile, tu...",["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"])]

    maison = repartition_maison(joueur, questions)
    joueur["Maison"] = maison
    print(f"\nLe Choixpeau s’exclame : {maison} !!!")
    print(f"Tu rejoins les élèves de {maison} sous les acclamations !")

def installation_salle_commune(joueur):
    print("Vous suivez les préfets à travers les couloirs du château...\n")

    with open("data/maisons.json", "r", encoding="utf-8") as fichier:
        maisons = json.load(fichier)
    maison_joueur = joueur["Maison"]
    infos_maison = maisons[maison_joueur]
    emoji = infos_maison["emoji"]
    description = infos_maison["description"]
    message = infos_maison["message_installation"]
    couleurs = infos_maison["couleurs"]
    print(emoji, description)
    print(message)
    print("Les couleurs de votre maison :", ", ".join(couleurs))
def lancer_chapitre_2(personnage):
    rencontrer_amis(personnage)
    mot_de_bienvenue()
    ceremonie_repartition(personnage)
    installation_salle_commune(personnage)
    afficher_personnage(personnage)
    print("c'est la fin! Bientôt les cours commencent à Poudlard")