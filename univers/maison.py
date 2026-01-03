from utils.input_utils import demander_choix
def actualiser_points_maison(maisons,nom_maison,points):
    if nom_maison in maisons.keys() :
        maisons[nom_maison]+= points
        print("le nouveau score de la maison {} est {}".format(nom_maison,maisons[nom_maison]))
    else:
        print ("la maison est introuvable")

def afficher_maison_gagnante(maisons):
    premiere = True

    for cle in maisons:
        if premiere:
            gagnant = cle
            maximum = maisons[cle]
            premiere = False
        elif maisons[cle] > maximum:
            maximum = maisons[cle]
            gagnant = cle
    return gagnant


def repartition_maison (joueur,questions) :
    score = {"Gryffondor":0, "Serpentard":0, "Poufsouffle":0, "Serdaigle":0}
    L = joueur ["Attributs"]
    score["Gryffondor"] = 2 * L["courage"]
    score["Serpentard"] = 2 * L["ambition"]
    score["Poufsouffle"] = 2 * L["loyauté"]
    score["Serdaigle"] = 2 * L["intelligence"]
    for question,reponse,maison in questions :
        print ("")
        choix = demander_choix (question,reponse)
        c = choix - 1
        s = list(score.keys())
        i = s[c]
        score[i] += 3
    print ("Résumé des scores : ")
    for a,b in score.items() :
        print("{} : {}".format (a,b))
    p = afficher_maison_gagnante(score)
    return p
