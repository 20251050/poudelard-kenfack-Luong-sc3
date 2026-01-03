Projet Poudelard : L'Art de Coder comme un Sorcier

Présentation Générale

Titre du Projet
Poudelard - Jeu d'aventure interactif inspiré de l'univers Harry Potter


Poudelard est un jeu d'aventure textuel développé en Python qui plonge le joueur dans l'univers magique de Harry Potter. Le joueur crée son propre personnage, reçoit sa lettre d'admission à Poudlard, achète ses fournitures sur le Chemin de Traverse, est réparti dans une maison par le Choixpeau magique, apprend des sorts, et participe à un match de Quidditch épique.

Ce projet met en œuvre les concepts fondamentaux de la programmation Python : fonctions, structures de données (dictionnaires, listes), gestion de fichiers JSON, et interactions utilisateur.

Contributeurs
- Luong Kevin
- Thérésine Kenfack
- Groupe : SC3

Installation

Prérequis
- Aucune bibliothèque externe n'est requise (le projet utilise uniquement les modules : random et json)

Cloner le dépôt

git clone https://github.com/20251050/pourdelard-kenfack-Luong-sc3.git
cd pourdelard-kenfack-Luong-sc3


Configuration
Aucune configuration supplémentaire n'est nécessaire. Assurez-vous simplement que tous les fichiers JSON sont présents dans le dossier `data/`.

Utilisation

Lancer le jeu
Pour démarrer l'aventure, exécutez le fichier main.py :

python main.py


Ou depuis votre IDE préféré (PyCharm, VS Code, etc.) :
- Ouvrez le projet
- Exécutez main.py (bouton Run)

Navigation dans le jeu
- Suivez les instructions affichées à l'écran
- Saisissez vos réponses lorsque demandé
- Note importante : Si appuyer sur Entrée ne fait rien, appuyez une deuxième fois pour continuer

Déroulement
1. Chapitre 1 : Création de votre personnage, réception de la lettre de Poudlard, rencontre avec Hagrid, achat des fournitures
2. Chapitre 2 : Voyage dans le Poudlard Express, rencontres avec Ron, Hermione et Drago, cérémonie de répartition
3. Chapitre 3 : Apprentissage de sorts magiques et quiz de connaissances
4. Chapitre 4 : Match de Quidditch opposant votre maison à une maison adverse

Fonctionnalités Principales

Système de jeu
- Création de personnage avec attributs personnalisables (courage, intelligence, loyauté, ambition)
- Gestion d'inventaire et d'argent (galions)
- Système de points pour les maisons de Poudlard

Chapitres narratifs
- Chapitre 1 : Introduction au monde magique et achats sur le Chemin de Traverse
- Chapitre 2 : Voyage vers Poudlard et répartition dans les maisons
- Chapitre 3 : Cours de magie avec apprentissage de 5 sorts et quiz interactif
- Chapitre 4 : Match de Quidditch avec système de combat dynamique

Mécaniques de jeu
- Système de répartition des maisons basé sur les attributs et les réponses du joueur
- Gestion aléatoire des sorts appris (1 offensif, 1 défensif, 3 utilitaires)
- Quiz de magie avec questions aléatoires
- Simulation de match de Quidditch avec :
  - Tentatives de marquer des buts
  - Apparition aléatoire du Vif d'Or
  - Statistiques de match (buts marqués, attaques stoppées)
  - Attribution de points aux maisons

Gestion des données
- Chargement des données depuis fichiers JSON (sorts, maisons, équipes, inventaire, quiz)
- Validation robuste des saisies utilisateur
- Gestion des erreurs et cas limites


Journal de Bord

Chronologie du Projet

Semaine 1 : Fondations et Chapitre 1 (9-15 décembre 2025)
- Objectifs : Mise en place de la structure du projet, création des modules utilitaires et du premier chapitre
- Réalisations :
  - Configuration du dépôt GitHub et mise en place de l'arborescence
  - Implémentation de utils/input_utils.py avec les fonctions de validation des saisies
  - Développement de univers/personnage.py pour la gestion du personnage
  - Création complète du Chapitre 1 (introduction, création personnage, lettre, Hagrid, achats)
- Difficultés rencontrées :
  - Premiers problèmes avec Git (commits, push, pull)
  - Apprentissage de la collaboration via GitHub
  - Désaccords sur la structure et l'implémentation de certaines fonctions

Semaine 2 : Module Maison et Chapitre 2 (16-22 décembre 2025)
- Objectifs : Développement du système de maisons et du deuxième chapitre
- Réalisations :
  - Implémentation de univers/maison.py avec la logique de répartition
  - Création du Chapitre 2 (rencontres dans le train, répartition, installation)
  - Développement de menu.py et main.py
- Difficultés rencontrées :
  - Complexité de l'algorithme de répartition des maisons
  - Gestion des attributs modifiés lors des rencontres
  - Coordination des tâches entre les membres du binôme

Semaine 3 : Chapitre 3 et Dépôt Intermédiaire (23-29 décembre 2025)
- Objectifs : Finalisation du Chapitre 3 et préparation du dépôt intermédiaire
- Réalisations :
  - Implémentation complète du Chapitre 3 (apprentissage des sorts, quiz)
  - Mise à jour du menu principal
  - Dépôt intermédiaire : 21 décembre 2025 - Tous les modules fonctionnels
- Difficultés rencontrées :
  - Gestion de l'aléatoire pour la sélection des sorts
  - Éviter les doublons dans le quiz
  - Tests approfondis de l'intégration des chapitres

Semaine 4 : Chapitre 4 et Dépôt Final (30 décembre 2025 - 3 janvier 2026)
- Objectifs : Développement du match de Quidditch et finalisation
- Réalisations:
  - Implémentation complète du Chapitre 4 (scénario Quidditch)
  - Optimisations du code (remplacement de multiples print() par \n)
  - Amélioration de la lisibilité générale du code
  - Tests finaux et corrections de bugs
  - Dépôt final : 3 janvier 2026
- Optimisations :
  - Réduction des appels print() répétitifs
  - Amélioration de la présentation des messages
  - Affinage des probabilités dans le match de Quidditch

Décisions de Conception

Lisibilité du code
Décision principale : Privilégier la lisibilité et la maintenabilité du code
- Noms de variables explicites
- Fonctions courtes et ciblées
- Organisation modulaire claire
- Commentaires supprimés pour la version finale (conformément aux consignes)

Structure modulaire
- Séparation claire entre logique métier (univers), déroulement narratif (chapitres) et utilitaires (utils)
- Utilisation de fichiers JSON pour toutes les données externes
- Fonctions réutilisables et génériques

Gestion des interactions
- Validation systématique des saisies utilisateur
- Messages d'erreur clairs et informatifs
- Expérience utilisateur fluide avec pauses narratives


Contrôle, Tests et Validation

Gestion des Entrées et Erreurs

Système de validation robuste
Le module `utils/input_utils.py` assure la validation de toutes les saisies utilisateur :

1. demander_texte(message)
   - Vérifie que la saisie n'est pas vide
   - Supprime les espaces superflus avec `strip()`
   - Redemande en cas de saisie invalide

2. demander_nombre(message, min_val, max_val)
   - Vérifie que la saisie est un nombre entier valide
   - Gère les nombres négatifs (signe `-`)
   - Contrôle que le nombre est dans l'intervalle spécifié
   - Conversion manuelle caractère par caractère sans utiliser `int()`

3. demander_choix(message, options)
   - Affiche un menu numéroté
   - Utilise `demander_nombre()` pour garantir un choix valide
   - Retourne directement la valeur choisie

Évolution des fonctions
Les fonctions de validation ont été remaniées plusieurs fois au cours du projet pour s'adapter à tous les cas d'utilisation rencontrés dans les différents chapitres. Cette approche itérative a permis d'obtenir des fonctions très robustes.

Gestion des cas limites
- Budget insuffisant : Vérification avant chaque achat, fin de partie si le joueur ne peut pas acheter les objets obligatoires
- Valeurs négatives : Contrôle de l'argent pour éviter les montants négatifs

Bugs Connus
Aucun bug majeur connu à ce jour. Le jeu a été testé de manière exhaustive et fonctionne correctement dans tous les scénarios prévus.

Stratégies de Test

Approche de test
Méthodologie : Tests unitaires continus pendant le développement
- Chaque fonction testée immédiatement après sa création
- Pas d'attente de la fin du chapitre pour tester
- Correction des bugs au fur et à mesure

Tests fonctionnels effectués

Chapitre 1
- Création de personnage avec différentes combinaisons d'attributs
- Refus de la lettre de Poudlard (fin du jeu)
- Achat avec budget suffisant
- Achat avec budget insuffisant (échec et fin de partie)
- Oubli d'un objet obligatoire
- Vérification que l'argent ne devient jamais négatif

Chapitre 2
- Différentes combinaisons de réponses lors des rencontres
- Modification correcte des attributs
- Répartition dans toutes les maisons possibles
- Affichage correct des informations de maison

Chapitre 3
- Apprentissage de 5 sorts (1 offensif, 1 défensif, 3 utilitaires)
- Pas de doublons dans les sorts appris
- Quiz avec 4 questions aléatoires différentes
- Réponses correctes et incorrectes
- Attribution correcte des points aux maisons

Chapitre 4 - Quidditch
- Création des équipes avec le joueur comme Attrapeur
- Sélection aléatoire de l'adversaire
- Tentatives de marquer (réussies et échouées)
- Apparition du Vif d'Or
- Capture du Vif d'Or (par les deux équipes)
- Match sans Vif d'Or (20 tours complets)
- Attribution des 500 points bonus à la maison gagnante
- Calcul correct du score final et désignation du vainqueur

Tests d'intégration
- Parcours complet du jeu du début à la fin
- Persistance des données du personnage entre les chapitres
- Accumulation correcte des points de maison
- Navigation dans le menu principal

Cas limites testés
- Saisies vides ou avec espaces uniquement
- Nombres hors limites
- Choix invalides dans les menus
- Budget exactement égal au coût d'un objet
- Réponses au quiz avec casse différente


Structure du Projet

```
pourdelard-kenfack-Luong-sc3/
│
├── main.py                      # Point d'entrée du jeu
├── menu.py                      # Gestion du menu principal
├── README.md                    # Ce fichier
│
├── univers/                     # Modules de gestion de l'univers
│   ├── personnage.py            # Gestion du personnage joueur
│   └── maison.py                # Gestion des maisons et répartition
│
├── chapitres/                   # Modules des chapitres narratifs
│   ├── chapitre_1.py            # L'arrivée dans le monde magique
│   ├── chapitre_2.py            # Voyage vers Poudlard
│   ├── chapitre_3.py            # Apprentissage et quiz
│   └── chapitre_4.py            # Match de Quidditch
│
├── utils/                       # Utilitaires
│   └── input_utils.py           # Validation des saisies et lecture JSON
│
└── data/                        # Fichiers de données JSON
    ├── maisons.json             # Informations sur les maisons
    ├── equipes_quidditch.json   # Composition des équipes
    ├── sorts.json               # Liste des sorts disponibles
    ├── quiz_magie.json          # Questions du quiz
    └── inventaire.json          # Objets disponibles à l'achat
```


Technologies Utilisées

- Langage : Python
- Modules :
  - random : Génération de nombres aléatoires et sélections aléatoires
  - json : Chargement des données depuis fichiers JSON
- Gestion de version : Git & GitHub


Améliorations Futures (Non implémentées)

- Chapitre 5 : Extension avec un scénario insp D     un autre film
- Système de sauvegarde de la progression
- Interface graphique 
- Système de combat plus complexe 
- Plus de sorts et d'objets magiques



