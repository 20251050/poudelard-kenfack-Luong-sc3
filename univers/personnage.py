def initialiser_personnage(nom,prenom,attributs):
    D = {}
    D["Nom"] = nom
    D["Prenom"] = prenom
    D["Argent"] = 100
    D["Inventaire"] = []
    D["Sortilèges"] = []
    D["Attributs"] = attributs
    return D

def afficher_personnage(joueur):
    print ("profil du personnage : ")
    print ("Nom : ",joueur["Nom"])
    print ("Prenom :",joueur["Prenom"])
    print ("Argent : ",joueur["Argent"])
    print ("Inventaire : ",", ".join(str(x) for x in joueur["Inventaire"]))
    print ("Sortilèges : ",", ".join(str(y) for y in joueur["Sortilèges"]))
    print ("Attributs : ")
    for (a,b) in joueur["Attributs"].items():
        print(" -{} : {}".format(a,b))

def modifier_argent (joueur,montant) :
    joueur["Argent"] += montant

def ajouter_objet (joueur,cle,objet):
    joueur[cle].append (str(objet))






