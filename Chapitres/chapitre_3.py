import random
from utils.input_utils import demander_texte,load_fichier
from univers.maison import actualiser_points_maison,afficher_maison_gagnante
from univers.personnage import afficher_personnage
def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    print("Tu commences tes cours de magie à Poudlard...")
    liste_sorts =load_fichier(chemin_fichier)
    offensifs = [s for s in liste_sorts if s["type"] == "Offensif"]
    defensifs = [s for s in liste_sorts if s["type"] == "Défensif"]
    utilitaires = [s for s in liste_sorts if s["type"] == "Utilitaire"]
    a_apprendre = []
    sort_off = random.choice(offensifs)
    a_apprendre.append(sort_off)
    sort_def = random.choice(defensifs)
    a_apprendre.append(sort_def)
    utilitaires_temp = utilitaires[:]
    for i in range(3):
        choisi = random.choice(utilitaires_temp)
        a_apprendre.append(choisi)
        del utilitaires_temp[utilitaires_temp.index(choisi)]
    for sort in a_apprendre:
        joueur["Sortilèges"].append(sort)
        print(f"Tu viens d'apprendre le sortilège : {sort['nom']} ({sort['type']})")
        input("Appuie sur Entrée pour continuer...")
    print("\nTu as terminé ton apprentissage de base à Poudlard !\n Voici les sortilèges que tu maîtrises désormais :")
    for sort in a_apprendre:
        print(f"- {sort['nom']} ({sort['type']}) : {sort['description']}.")

def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    print("Bienvenue au quiz de magie de Poudlard !\n Réponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")
    questions = load_fichier(chemin_fichier)
    questions_tirees = []
    while len(questions_tirees) < 4:
        q = random.choice(questions)
        if q not in questions_tirees:
            questions_tirees.append(q)
    score_quiz = 0
    numero_question = 1
    for q in questions_tirees:
        print(f"{numero_question}. {q['question']}")
        reponse_joueur = demander_texte ("Votre réponse : ")
        if reponse_joueur.lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.\n")
            score_quiz += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']}\n")
        numero_question += 1
    print(f"Score obtenu : {score_quiz} points")
    return score_quiz
def lancer_chapitre_3 (personnage, maisons):
     apprendre_sorts (personnage,chemin_fichier="../data/sorts.json")
     score = quiz_magie(personnage,chemin_fichier="../data/quiz_magie.json")
     actualiser_points_maison(maisons,personnage["maison"],score)
     afficher_maison_gagnante(maisons)
     afficher_personnage (personnage)