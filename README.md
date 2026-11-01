# Reignib — Projet étudiant de développement logiciel

Reignib est un projet étudiant réalisé en équipe autour d’un jeu de cartes en Python. Le jeu sert de support à l’exploration de plusieurs dimensions du développement logiciel : programmation orientée objet, réalisation d’une application de bout en bout, gestion de contenus multimédias et organisation d’un projet avec GitLab.

L’objectif de ce dépôt est de présenter cette démarche et les choix techniques du projet, plutôt que de proposer une page destinée aux joueurs.

## Axes d’apprentissage

### Programmation orientée objet

Le code est organisé en classes qui représentent les principaux éléments de l’application : cartes (`Card`, `EventCard`, `NarrativeCard`), menus, statistiques et fils de cartes (`Thread`, `RandomThread`, `NarrativeThread`). Ce découpage a permis de travailler sur la responsabilité des objets, l’héritage et les interactions entre composants.

### Développement de l’application de bout en bout

Le projet couvre plusieurs couches d’une application desktop : interface et événements avec Pyglet, logique de jeu, chargement des contenus, lecture audio et sauvegarde locale. Ici, « full-stack » désigne le développement de ces couches dans une application de bureau, et non une architecture web client-serveur.

### Gestion des données et des ressources

Les contenus sont séparés du code autant que possible :

- les cartes et leurs effets sont décrits dans `src/utils/cards_data.csv` ;
- les illustrations, icônes, arrière-plans et polices sont rangés dans `src/png/` et `src/font/` ;
- les sons et musiques sont regroupés dans `src/sounds/` ;
- `src/cardlib.py` charge les ressources utilisées par l’application ;
- `src/save.py` sérialise l’état de jeu dans un fichier JSON local.

Cette organisation facilite l’édition des cartes et le remplacement des ressources sans modifier directement le rendu de l’application.

### Gestion de projet et CI/CD

La gestion du projet avec GitLab fait partie des apprentissages : organisation du travail collaboratif, versionnement et découverte d’une démarche CI/CD. Le dépôt GitHub présenté ici ne contient pas de fichier `.gitlab-ci.yml` ; il ne décrit donc pas de pipeline GitLab exécutable ni de jobs automatisés.

Les documents de conception et de planification conservés dans le dépôt témoignent également de cette démarche : [présentation UML](UML/REIGNIB_presentation.pdf) et [planning Gantt](UML/gantt.png). Un [historique GitLab du projet](https://git.enib.fr/y0lagadi/CPO_02_Groupe2) est également disponible.

## Choix techniques

- **Python** pour la logique de l’application.
- **Pyglet** pour la fenêtre, le rendu graphique, les interactions et l’audio.
- **NumPy** pour certaines opérations de sélection.
- **CSV** pour séparer les données des cartes du code de l’interface.
- **JSON** pour la sauvegarde locale.

Le prototype s’appuie sur un module de configuration partagé pour rendre l’état accessible entre composants. Ce choix facilite les échanges dans une première version, mais crée aussi du couplage ; le projet permet ainsi d’aborder les compromis entre rapidité de développement et maintenabilité.

## Organisation du dépôt

| Chemin | Contenu |
| --- | --- |
| `src/main.py` | Point d’entrée et initialisation de l’application |
| `src/obj/` | Classes des cartes, menus, statistiques et fils narratifs |
| `src/utils/` | Configuration, chargement des données et utilitaires |
| `src/png/`, `src/sounds/`, `src/font/` | Ressources graphiques, audio et typographiques |
| `UML/` | Documents de conception et de planification |

## Équipe

- MADEC Maël
- COLLET Guillaume
- LE CORFF Louis
- LAGADIC Youenn

## Licence

Ce projet est distribué sous licence [MIT](LICENSE).
