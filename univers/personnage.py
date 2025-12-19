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
        print("Profil du personnage :")
        for cle, valeur in joueur.items():
            if type(valeur) == dict:
                print(f"{cle} :")
                for sous_cle, sous_valeur in valeur.items():
                    print(f"- {sous_cle} : {sous_valeur}")
            elif type(valeur) == list:
                print(f"{cle} :")
                if len(valeur) != 0:
                    print(", ".join(str(element) for element in valeur))
            else:
                print(f"{cle} : {valeur}")

def modifier_argent (joueur,montant) :
    joueur["Argent"] += montant

def ajouter_objet (joueur,cle,objet):
    joueur[cle].append (str(objet))






