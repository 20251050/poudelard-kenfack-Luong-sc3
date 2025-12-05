def demander_texte(message) :
    nom_valide = False
    while nom_valide == False :
        nom = input("Entrez le nom de votre personnage : ")
        nom = nom.strip()
        if nom == "" or nom == float:
            nom_valide = False
            print("Veuillez entre un nom de personnage correct")
        else:
            nom_valide = True
    return nom

nom = demander_texte("Entrez le nom de votre personnage : ")

def demander_nombre(message) :
    courage_valide = False
    while courage_valide == False :
        courage = int(input("Niveau de courage (1-10) : "))
        if courage < 1 or courage > 10 or courage == str:
            courage_valide = False
            print("Veuillez entre un nombre 1 et 10")
        else:
            courage_valide = True
    return courage

courage = demander_nombre("Niveau de courage (1-10) : ")

def demander_choix(message, option) :
    choix_valide = False
    while choix_valide == False :
        choix = input("Voulez-vous continuer ?\n 1. Oui\n 2. Non\n Votre choix : ")
        if choix == "Oui" or choix == "Non" or choix == "oui" or choix == "non" or choix == 1 or choix == 2:
            choix_valide = True
        else:
            choix_valide = False
    return choix

choix = demander_choix("Voulez-vous continuer ?", ["Oui", "Non"])