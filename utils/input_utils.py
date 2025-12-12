def demander_texte(message) :
    nom_valide = False
    while nom_valide == False :
        nom = input(message)
        nom = nom.strip()
        if nom == "" or nom == float:
            nom_valide = False
            print(message)
        else:
            nom_valide = True
    return nom


def demander_nombre(message, min_val=None, max_val=None):
    saisie = input(message)
    if not saisie:
        print("Veuillez entrer un nombre.".format(min_val, max_val))
        return demander_nombre(message, min_val, max_val)
    index = 0
    signe = 1
    est_valide = True
    resultat = 0
    if saisie[0] == '-':
        signe = -1
        index = 1
    if len(saisie) == index:
        est_valide = False
    else:
        for i in range(index, len(saisie)):
            if not ('0' <= saisie[i] <= '9'):
                est_valide = False
            resultat = resultat * 10 + (ord(saisie[i]) - ord('0'))
    if not est_valide:
        return demander_nombre(message, min_val, max_val)
    nombre = resultat * signe
    if min_val is not None and nombre < min_val:
        print("Veuillez entrer un nombre entre {} et {}.".format(min_val, max_val))
        return demander_nombre(message, min_val, max_val)
    if max_val is not None and nombre > max_val:
        print("Veuillez entrer un nombre entre {} et {}.".format(min_val, max_val))
        return demander_nombre(message, min_val, max_val)
    return nombre


def demander_choix(message, option) :
    print(message)
    for i in range(len(option)) :
        print(i+1,". ", option[i])
    choix_valide = False
    while choix_valide == False :
        choix = demander_nombre("Votre choix : ")
        for i in range(len(option)) :
            if choix == i:
                choix_valide = True
            else:
                choix_valide = False
    return choix
