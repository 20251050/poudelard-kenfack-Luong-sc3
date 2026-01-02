from univers.personnage import initialiser_personnage, afficher_personnage
from utils.input_utils import demander_texte,demander_nombre,load_fichier,demander_choix

def introduction():
    print ("BIENVENUE A L'ECOLE DES SORCIERS, QUE L'AVENTURE COMMENCE ! ")
    input("Appuyez sur Entrée pour continuer")

def creer_personnage ():
    nom = demander_texte ("Entrez le nom de votre personnage : ")
    prenom = demander_texte ("Entrez le prénom de votre personnage : ")
    attributs = { "courage":0, "intelligence":0, "loyauté":0, "ambition":0}
    print ("Choisissez vos attributs : ")

    for cle in attributs.keys ():
       attributs[cle] = demander_nombre("Niveau de {} (1-10) : ".format(cle) ,1 ,10 )
    joueur = initialiser_personnage(nom,prenom,attributs)
    afficher_personnage(joueur)
    return joueur


def recevoir_lettre ():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scelléedu sceau de Poudlard...\n «Cher élève,\n Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard !»\n")
    demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?", ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."])
    if demander_choix == 2:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie :\n EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison !\n Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit(0)
    else:
        print("Vous avez accepté la lettre !\n La magie vous attend… Votre aventure à Poudlard commence maintenant !")


def rencontrer_hagrid(personnage):
    print("Hagrid : 'Salut {} ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.".format (personnage))
    demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if demander_choix == 1:
        print("Vous acceptez de suivre Hagrid. Il sourit et vous dit :\n 'Bonne décision ! Le Chemin de Traverse t'attend.'")
    else:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")


def acheter_fournitures(personnage):
    catalogue = load_fichier("data/inventaire.json")
    obligatoires= ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    restants = obligatoires[:]
    inventaire = personnage["Inventaire"]
    argent = 100
    print("Bienvenue sur le Chemin de Traverse !\n \nCatalogue des objets disponibles :")
    for num, (nom, prix) in catalogue.items():
        print(f"{num}. {nom} - {prix} galions")
    print(f"Vous avez {argent} galions.")
    while restants:
        print("\nObjets obligatoires restant à acheter :", ", ".join(restants))
        choix = input("Entrez le numéro de l'objet à acheter : ")
        if choix not in catalogue:
            print("Numéro invalide, réessayez.")
        else:
            item, prix = catalogue[choix]
            if prix > argent:
                print("Vous n’avez pas assez d’argent... Vous perdez la partie.")
                return None
            argent -= prix
            inventaire.append(item)
            print(f"Vous avez acheté : {item} (-{prix} galions).")
            print(f"Il vous reste {argent} galions.")
        if item in restants:
           index = restants.index(item)
           del restants[index]
    print("\nTous les objets obligatoires ont été achetés !\n Il est temps de choisir votre animal de compagnie !")
    print(f"Vous avez {argent} galions.")
    animaux = {"1": ("Chouette", 20),"2": ("Chat", 15),"3": ("Rat", 10),"4": ("Crapaud", 5)}
    print("Voici les animaux disponibles :")
    for num, (nom, prix) in animaux.items():
        print(f"{num}. {nom} - {prix} galions")
    choix_animal = input("Quel animal voulez-vous ? Votre choix : ")
    while choix_animal not in animaux:
        print("Choix invalide. Entrez un numéro entre 1 et 4.")
        choix_animal = input("Votre choix : ")
    animal, prix_animal = animaux[choix_animal]
    if prix_animal > argent:
        print("Vous n’avez pas assez d’argent pour cet animal. Vous perdez la partie.")
        exit(0)
    argent -= prix_animal
    inventaire.append(animal)
    print(f"Vous avez choisi : {animal} (-{prix_animal} galions).")
    personnage["Inventaire"] = inventaire
    personnage["Argent"] = argent
    return afficher_personnage(personnage)


def lancer_chapitre_1():
    introduction()
    joueur =creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur["Nom"])
    acheter_fournitures(joueur)
    print("\nFin du Chapitre 1 ! Votre aventure commence à Poudlard...\n")
    return joueur