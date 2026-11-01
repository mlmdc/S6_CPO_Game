# Reignib

 **🇬🇧 EN** - A student software project exploring object-oriented and full-stack development, multimedia data management and collaborative workflows.
 **🇫🇷 FR** - Un projet étudiant explorant la programmation orientée objet, le développement full-stack, la gestion de données multimédias et le travail collaboratif.

![Reignib project artwork](src/png/main_paysage.png)

**Python · Pyglet · Student software project**

[← Back to portfolio](https://mlmdc.github.io/mlmdc_portfolio/) · [Contents / Sommaire](#table-of-contents-sommaire)

<a id="table-of-contents-sommaire"></a>
## Table of contents / Sommaire

- [Overview / Présentation](#overview-presentation)
- [Problem & approach / Problématique et approche](#problem-approach)
- [Technical decisions / Choix techniques](#technical-decisions)
- [Results & learnings / Résultats et apprentissages](#results-learnings)
- [Getting started](#getting-started)
- [Project resources / Ressources du projet](#project-resources)
- [License / Licence](#license)

<a id="overview-presentation"></a>
## Overview / Présentation

**🇬🇧 EN** Reignib is a team-based student project developed in Python. Its card-game prototype provided a practical setting to explore object-oriented programming, application development across multiple layers, multimedia resource management and collaborative project practices. This repository documents the technical and organizational work behind the prototype, not just a game to try.

<br>

**🇫🇷 FR** Reignib est un projet étudiant réalisé en équipe et développé en Python. Son prototype de jeu de cartes a servi de support pour explorer la programmation orientée objet, le développement d’une application à plusieurs couches, la gestion de ressources multimédias et les pratiques de travail collaboratif. Ce dépôt présente le travail technique et organisationnel réalisé autour du prototype, et pas seulement un jeu à essayer.

### Learning areas / Axes d’apprentissage

**🇬🇧 EN**
- Model game concepts with classes for cards, menus, statistics and narrative threads.
- Build a desktop application combining interface, events, game logic, audio and local saves.
- Keep card data and visual and audio assets separate from application code.
- Explore team coordination, project planning, version control and CI/CD practices with GitLab.

**🇫🇷 FR**
- Modéliser les éléments du jeu avec des classes de cartes, menus, statistiques et fils narratifs.
- Construire une application de bureau réunissant interface, événements, logique de jeu, audio et sauvegarde locale.
- Séparer les données des cartes et les ressources visuelles et audio du code applicatif.
- Explorer la coordination d’équipe, la planification, le versionnement et les pratiques CI/CD avec GitLab.

<a id="problem-approach"></a>
## Problem & approach / Problématique et approche

**🇬🇧 EN**
The project brief combined the design of a card-based game with the application of software engineering concepts in a team setting. The team organized the prototype into Python modules and classes, connected a Pyglet interface to game data, and prepared UML and planning documents to support design and coordination. The project also provided an opportunity to study how a collaborative GitLab workflow can support development and CI/CD.

<br>

**🇫🇷 FR**
Le projet associait la conception d’un jeu de cartes à la mise en pratique de notions de génie logiciel dans un travail d’équipe. Le prototype a été organisé en modules et classes Python, avec une interface Pyglet reliée aux données du jeu. Des documents UML et de planification ont accompagné la conception et la coordination. Le projet a également permis d’étudier comment un flux de travail collaboratif avec GitLab peut soutenir le développement et une démarche CI/CD.

<a id="technical-decisions"></a>
## Technical decisions / Choix techniques

**🇬🇧 EN**
Python and Pyglet handle the desktop window, rendering, input and audio. The code defines classes for cards, menus, statistics and narrative threads, while CSV keeps card descriptions and effects separate from rendering code. Images, fonts and sounds are organized as application assets, and JSON is used for a local save. A shared configuration module made state accessible across components during prototyping, with the trade-off of tighter coupling.

GitLab is part of the project's collaborative development and CI/CD learning objectives. This GitHub mirror does not contain a `.gitlab-ci.yml` file, so it does not represent an executable GitLab pipeline.

<br>

**🇫🇷 FR**
Python et Pyglet gèrent la fenêtre de bureau, le rendu, les entrées et l’audio. Le code définit des classes pour les cartes, les menus, les statistiques et les fils narratifs ; le CSV sépare les descriptions et effets des cartes du code de rendu. Les images, polices et sons sont organisés comme ressources de l’application, et la sauvegarde locale utilise JSON. Un module de configuration partagé a rendu l’état accessible entre composants pendant le prototypage, au prix d’un couplage plus important.

GitLab fait partie des objectifs d’apprentissage liés au développement collaboratif et au CI/CD. Ce miroir GitHub ne contient pas de fichier `.gitlab-ci.yml` et ne correspond donc pas à un pipeline GitLab exécutable.

<a id="results-learnings"></a>
## Results & learnings / Résultats et apprentissages

**🇬🇧 EN**
- The repository brings together a Python/Pyglet desktop prototype and its design and planning documents.
- Separating card data and multimedia assets from application code supports content updates without rewriting the interface.
- The class and module structure provided practical experience with object-oriented design and component interactions.
- Shared configuration helped prototype coordination but highlighted the maintainability cost of coupling.
- The project introduced collaborative planning and version-control practices, alongside CI/CD concepts in a GitLab context.

<br>

**🇫🇷 FR**
- Le dépôt rassemble un prototype de bureau Python/Pyglet ainsi que ses documents de conception et de planification.
- La séparation des données de cartes et des ressources multimédias du code facilite les mises à jour de contenu sans réécrire l’interface.
- La structure en classes et modules a permis de mettre en pratique la conception orientée objet et les interactions entre composants.
- La configuration partagée a facilité le prototypage, tout en mettant en évidence le coût du couplage pour la maintenabilité.
- Le projet a permis d’aborder la planification collaborative et le versionnement, ainsi que les concepts de CI/CD dans un contexte GitLab.

<a id="getting-started"></a>
## Getting started

### Prerequisites / Prérequis

- Python 3 and `pip`
- A desktop environment with graphics and audio support

The repository does not currently provide a dependency lockfile or pinned package versions.

### Install and run / Installer et lancer

Run the prototype from `src/`, which is the working directory expected by its relative paths to images, sounds and card data:

```bash
cd src
python -m pip install pyglet numpy
python main.py
```

<a id="project-resources"></a>
## Project resources / Ressources du projet

**🇬🇧 EN**
The [UML design document](UML/REIGNIB_presentation.pdf) and [Gantt planning chart](UML/gantt.png) record design and project-planning work. The original [GitLab project history](https://git.enib.fr/y0lagadi/CPO_02_Groupe2) provides further context on the collaborative workflow. Current repository tasks are tracked in [GitHub Issues](https://github.com/mlmdc/S6_CPO_Game/issues).

**🇫🇷 FR**
Le [dossier de conception UML](UML/REIGNIB_presentation.pdf) et le [planning Gantt](UML/gantt.png) présentent le travail de conception et de planification. L’[historique du projet sur GitLab](https://git.enib.fr/y0lagadi/CPO_02_Groupe2) apporte un complément de contexte sur le travail collaboratif. Les tâches du dépôt actuel sont suivies dans les [issues GitHub](https://github.com/mlmdc/S6_CPO_Game/issues).

### Contributors / Contributeurs

- MADEC Maël — [m0madec@enib.fr](mailto:m0madec@enib.fr)
- COLLET Guillaume — [g0collet@enib.fr](mailto:g0collet@enib.fr)
- LE CORFF Louis — [l0lecorf@enib.fr](mailto:l0lecorf@enib.fr)
- LAGADIC Youenn — [y0lagadi@enib.fr](mailto:y0lagadi@enib.fr)

<a id="license"></a>
## License / Licence
This project is licensed under the [MIT License](LICENSE).<br>
Ce projet est distribué sous licence [MIT](LICENSE).
