from utils.input_utils import *

from Chapitres.chapitre_1 import creer_personnage

def rencontre_ami(joueur):

    print("Vous rentrez à bord du Poudelard Express. Le traind émarre lentement en direction du Nord...\nUn garçon roux entre dans votre compartiment, l'air amical.\n- Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?\n")
    choix_ron = demander_choix("Que répondez-vous ?", ["Bien sûr, assieds-toi", "Désolé, je préfère voyager seul."])
    if choix_ron == 1:
        print("Ron sourit : - Géniel ! Tu verras, Poudelard, c'est incroyable !\n")
        loyauté+=1
    if choix_ron == 2:
        print("Il est pas content.\n")
    print("Une fille entre ensuitre, portant déjà une pile de livres.\n- Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?\n")
    choix_Hermione = demander_choix("Que répondez-vous ?", ["Oui, j'adore apprendre de nouvelles choses !", "Euh... non, je préfère les aventures aux bouquins."])
    if choix_Hermione == 1:
        print("...")
        ambition+=1
    if choix_Hermione == 2:
        print("hermione fronce les sourcils : - Il faudrait pourtant s'y mettre un jour !")
    print("Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choix_Drago = demander_choix("Comment réagissez-vous ?", ["Je lui serres la main poliment.", ["Je l'ignore complétement"], ["Je lui réponds avec arrogance."])
    if choix_Drago == 1:
        print("ok")
        ambition+=1
    elif choix_Drago == 2:
        print("Drago fronce les sourcils, vexé. - Tu le regretteras !")
        loyauté+=1
    elif choix_Drago == 3:
        print("d'accord")
        courage+=1
print("Le train continue sa route. Le château de Poudlard se profile à l'horizon...\n Tes choix semblent déjà en dire long sur ta personnalité !\n \n Tes attributs mis à jour : {'courage':", courage", 'intelligence':", intelligence", 'loyauté':", loyauté", 'ambition':", ambition"}")
