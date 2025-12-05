def demander_nom(message) :
    nom_valide = False
    while nom_valide == False :
        nom = input("Entrez le nom de votre personnage : ")
        nom = nom.strip()
        if nom == "" :
            nom_valide = False
            print("Veuillez entre un nom de personnage correct")
        else:
            nom_valide = True
    return nom

def demander_courage(message) :
    courage_valide = False
    while courage_valide == False :
        courage = int(input("Niveau de courage (1-10) : "))
        if courage < 1 or courage > 10 :
            courage_valide = False
            print("Veuillez entre un nombre 1 et 10")
        else:
            courage_valide = True
    return courage

def demander_choix(message, option) :
    choix_valide = False
    while choix_valide == False :
        choix = input("Voulez-vous continuer ?\n 1. Oui\n 2. Non\n Votre choix : ")
        if choix != "Oui" or choix != "Non" :
            choix_valide = False
        else :
            choix_valide = True
    return choix

