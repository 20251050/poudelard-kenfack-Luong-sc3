import random
from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison, afficher_maison_gagnante

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor': False,
        'joueurs': []
    }
    if est_joueur and joueur:
        nouvelle_liste = []
        nom_complet = joueur['Prenom'] + " " + joueur['Nom']
        nouvelle_liste.append(nom_complet + " (Attrapeur)")
        for j in equipe_data:
            if nom_complet not in j:
                nouvelle_liste.append(j)
        equipe['joueurs'] = nouvelle_liste
    else:
        for j in equipe_data:
            equipe['joueurs'].append(j)
    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)
    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque['joueurs'][0]
        else:
            buteur = random.choice(equipe_attaque['joueurs'])
        equipe_attaque['score'] += 10
        equipe_attaque['a_marque'] += 1
        print(buteur + " marque un but pour " + equipe_attaque['nom'] + " ! (+10 points)")
    else:
        equipe_defense['a_stoppe'] += 1
        print(equipe_defense['nom'] + " bloque l'attaque !")

def apparition_vifdor():
    nombre = random.randint(1, 6)
    return nombre == 6

def attraper_vifdor(e1, e2):
    equipe_gagnante = random.choice([e1, e2])
    equipe_gagnante['score'] += 150
    equipe_gagnante['attrape_vifdor'] = True
    return equipe_gagnante

def afficher_score(e1, e2):
    print("\nScore actuel :\n→ " + e1['nom'] + " : " + str(e1['score']) + " points\n→ " + e2['nom'] + " : " + str(
        e2['score']) + " points")

def afficher_equipe(maison, equipe):
    print("\nÉquipe de " + maison + " :")
    for joueur in equipe:
        print("- " + joueur)

def match_quidditch(joueur, maisons):
    equipes_data = load_fichier("data/equipes_quidditch.json")
    maison_joueur = joueur['Maison']
    maisons_disponibles = []
    for m in equipes_data:
        if m != maison_joueur:
            maisons_disponibles.append(m)
    maison_adverse = random.choice(maisons_disponibles)
    equipe_joueur = creer_equipe(maison_joueur, equipes_data[maison_joueur]['joueurs'], True, joueur)
    equipe_adverse = creer_equipe(maison_adverse, equipes_data[maison_adverse]['joueurs'], False)
    print("\nMatch de Quidditch : " + maison_joueur + " vs " + maison_adverse + " !")
    afficher_equipe(maison_joueur, equipe_joueur['joueurs'])
    afficher_equipe(maison_adverse, equipe_adverse['joueurs'])
    print("\nTu joues pour " + maison_joueur + " en tant qu'Attrapeur")
    tour = 1
    match_termine = False
    while tour <= 20 and not match_termine:
        print("\n━━━ Tour " + str(tour) + " ━━━")
        tentative_marque(equipe_joueur, equipe_adverse, True)
        tentative_marque(equipe_adverse, equipe_joueur, False)
        afficher_score(equipe_joueur, equipe_adverse)
        if apparition_vifdor():
            print("\n✨ Le Vif d'Or apparaît ! ✨")
            equipe_qui_attrape = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("Le Vif d'Or a été attrapé par " + equipe_qui_attrape['nom'] + " ! (+150 points)")
            match_termine = True
        if not match_termine:
            input("\nAppuyez sur Entrée pour continuer")
        tour += 1
    print("\nFin du match !")
    afficher_score(equipe_joueur, equipe_adverse)
    print("\nRésultat final :")
    if equipe_joueur['attrape_vifdor']:
        print("Le Vif d'Or a été attrapé par " + maison_joueur + " !\n+150 points pour " + maison_joueur + " ! Total : " + str(equipe_joueur['score']) + " points.")
    elif equipe_adverse['attrape_vifdor']:
        print("Le Vif d'Or a été attrapé par " + maison_adverse + " !\n+150 points pour " + maison_adverse + " ! Total : " + str(equipe_adverse['score']) + " points.")
    if equipe_joueur['score'] > equipe_adverse['score']:
        print("\n🏆 " + maison_joueur + " remporte le match ! 🏆\n+500 points pour " + maison_joueur + " !")
        actualiser_points_maison(maisons, maison_joueur, 500)
    elif equipe_adverse['score'] > equipe_joueur['score']:
        print("\n" + maison_adverse + " remporte le match...\n+500 points pour " + maison_adverse + " !")
        actualiser_points_maison(maisons, maison_adverse, 500)
    else:
        print("\nMatch nul ! Aucun point bonus n'est attribué.")

def lancer_chapitre4_quidditch(joueur, maisons):
    print("\n" + "=" * 60 + "\nCHAPITRE 4 : L'ÉPREUVE DE QUIDDITCH\n" + "=" * 60)
    print("\nLe grand jour est arrivé ! Le match de Quidditch décisif\nva déterminer quelle maison remportera la Coupe des Quatre Maisons.")
    input("\nAppuyez sur Entrée pour commencer le match...")
    match_quidditch(joueur, maisons)
    print("\n" + "=" * 60 + "\nFin du Chapitre 4 — Quelle performance incroyable sur le terrain !\n" + "=" * 60)
    print("\n ANNONCE DE LA COUPE DES QUATRE MAISONS ")
    afficher_maison_gagnante(maisons)
    from univers.personnage import afficher_personnage
    print("\n" + "=" * 60 + "\nTON AVENTURE À POUDLARD\n" + "=" * 60)
    afficher_personnage(joueur)
    print("\n Félicitations pour avoir terminé ton année à Poudlard ! ")