import random
from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison,afficher_maison_gagnante
from univers.personnage import afficher_personnage

def creer_equipe(maison,equipe_data, est_joueur=False, joueur=None):
    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor': False,
        'joueurs': list(equipe_data)
    }
    if est_joueur and joueur is not None:
        nouveaux_joueurs = []
        joueur_nom = f"{joueur['Prenom']} {joueur['Nom']} (Attrapeur)"
        nouveaux_joueurs.append(joueur_nom)
        for j in equipe["joueurs"]:
            if joueur["Prenom"] not in j and joueur["Nom"] not in j:
                nouveaux_joueurs.append(j)
        equipe["joueurs"] = nouveaux_joueurs

    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])

        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1

        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l’attaque !")

def apparition_vifdor():
    return random.randint(1, 6) == 6

def attraper_vifdor(e1, e2):
    gagnant = random.choice([e1, e2])
    gagnant["score"] += 150
    gagnant["attrape_vifdor"] = True
    print(f"Le Vif d’Or a été attrapé par {gagnant['nom']} ! (+150 points)")
    return gagnant

def afficher_score(e1, e2):
    print("\nScore actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")

def afficher_equipe(maison, equipe):
    print(f"\nÉquipe de {maison} :")
    for joueur in equipe["joueurs"]:
        print(f"- {joueur}")

def match_quidditch(joueur, maisons):
    equipes =load_fichier("data/equipes_quidditch.json")
    maison_joueur = joueur["Maison"]
    maisons_disponibles = list(equipes.keys())
    index_maison_joueur = maisons_disponibles.index(maison_joueur)
    del maisons_disponibles[index_maison_joueur]
    maison_adverse = random.choice(maisons_disponibles)
    equipe_joueur = creer_equipe(maison_joueur,equipes[maison_joueur]["joueurs"],est_joueur=True,joueur=joueur)
    equipe_adverse = creer_equipe(maison_adverse,equipes[maison_adverse]["joueurs"])
    print(f"\nMatch de Quidditch : {maison_joueur} vs {maison_adverse} !")
    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)
    print(f"\nTu joues pour {maison_joueur} en tant qu’Attrapeur")
    for tour in range(1, 21):
        print(f"\n _Tour {tour} _")
        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        tentative_marque(equipe_adverse, equipe_joueur)
        afficher_score(equipe_joueur, equipe_adverse)
        if apparition_vifdor():
            gagnant = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("\nFin du match !")
            afficher_score(equipe_joueur, equipe_adverse)
            actualiser_points_maison(maisons,maisons[gagnant["nom"]],150)
            print(f"+500 points pour {gagnant['nom']} !")
            actualiser_points_maison(maisons, maisons[gagnant["nom"]], 500)
            return
        input("Appuyez sur Entrée pour continuer")
    print("\nFin du match (20 tours atteints)")
    afficher_score(equipe_joueur, equipe_adverse)
    if equipe_joueur["score"] > equipe_adverse["score"]:
        gagnant = equipe_joueur
    elif equipe_adverse["score"] > equipe_joueur["score"]:
        gagnant = equipe_adverse
    else:
        print("Match nul !")
        return
    print(f"{gagnant['nom']} remporte le match ! (+500 points)")
    actualiser_points_maison(maisons, maisons[gagnant["nom"]], 500)

def lancer_chapitre4_quidditch(joueur, maisons):
    print("\n CHAPITRE 4 — ÉPREUVE DE QUIDDITCH ")
    match_quidditch(joueur, maisons)
    print("\nFin du Chapitre 4 — Quelle performance incroyable sur le terrain !")
    g = afficher_maison_gagnante(maisons)
    print ("La maison qui remporte le championnat est ",g)
    afficher_personnage(joueur)