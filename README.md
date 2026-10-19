# Reignib

**A choice-driven game about governing a fictional country and balancing the consequences of political decisions.**<br>
**Un jeu à choix où l'on gouverne un pays fictif et où chaque décision fait évoluer ses équilibres.**

![Reignib game artwork](src/png/main_paysage.png)

[Source code](https://github.com/mlmdc/S6_CPO_Game) · [Table of contents / Sommaire](#table-of-contents-sommaire)

<a id="table-of-contents-sommaire"></a>
## Table of contents / Sommaire

- [Overview / Présentation](#overview--présentation)
- [Problem & approach / Problématique et approche](#problem--approach--problématique-et-approche)
- [Technical decisions / Choix techniques](#technical-decisions--choix-techniques)
- [Results & learnings / Résultats et apprentissages](#results--learnings--résultats-et-apprentissages)
- [Getting started](#getting-started)
- [Project resources / Ressources du projet](#project-resources--ressources-du-projet)

## Overview / Présentation

**EN**<br>
Reignib is a Python desktop game inspired by [Reigns](https://www.devolverdigital.com/games/reigns), developed by [Nerial](https://www.nerial.co.uk/). It is intended for players interested in the consequences of public decisions. The player governs a fictional country by responding to events with one of two choices. Each decision changes four indicators—industry, people, climate and treasury. The project uses this loop to make the trade-offs around sustainable and short-term decisions visible through gameplay.

**FR**<br>
Reignib est un jeu de bureau en Python inspiré de [Reigns](https://www.devolverdigital.com/games/reigns), développé par [Nerial](https://www.nerial.co.uk/). Il s'adresse aux joueurs intéressés par les conséquences des décisions publiques. Le joueur gouverne un pays fictif en répondant à des événements par l'un de deux choix. Chaque décision modifie quatre indicateurs — industrie, population, climat et trésorerie. Le projet rend ainsi visibles, dans le jeu, les compromis entre décisions durables et court-termistes.

### Features / Fonctionnalités

**EN**
- Make left-or-right decisions in response to political and social events.
- Track four indicators; reaching an indicator's limit ends the game.
- Play with illustrated cards, menus, sound controls and a pause menu.
- Save a limited amount of game state locally.

**FR**
- Répondre à des événements politiques et sociaux par un choix à gauche ou à droite.
- Suivre quatre indicateurs ; atteindre la limite de l'un d'eux met fin à la partie.
- Jouer avec des cartes illustrées, des menus, des réglages sonores et un menu pause.
- Enregistrer localement une partie avec une portée limitée.

## Problem & approach / Problématique et approche

**EN**<br>
The initial brief was to make sustainable development part of the gameplay rather than a separate lesson. The team built a card-based decision loop in which each choice changes shared indicators and can reveal a contextual consequence. The main constraint was to deliver a playable prototype with original visual and narrative content as part of a student project.

**FR**<br>
L'objectif initial était d'intégrer le développement durable au jeu plutôt que d'en faire un contenu pédagogique séparé. L'équipe a créé une boucle de décisions à base de cartes : chaque choix modifie des indicateurs communs et peut révéler une conséquence contextualisée. La contrainte principale était de livrer un prototype jouable avec des contenus visuels et narratifs originaux dans le cadre d'un projet étudiant.

## Technical decisions / Choix techniques

**EN**<br>
Python and Pyglet handle the desktop window, rendering, input, timing and audio; NumPy supports weighted thread selection, although the active game flow currently registers a single random thread. Cards and their effects are stored in a semicolon-separated CSV so game content can be edited separately from rendering code. The code is split into modules for cards, menus, statistics, selection and event handling. A shared configuration module simplified coordination in the prototype, at the cost of tighter coupling between those modules.

**FR**<br>
Python et Pyglet gèrent la fenêtre, le rendu, les entrées, le rythme de jeu et l'audio ; NumPy permet la sélection pondérée des fils narratifs, bien que le jeu actif n'enregistre actuellement qu'un seul fil aléatoire. Les cartes et leurs effets sont stockés dans un CSV séparé par des points-virgules, dissociant le contenu du code de rendu. Le code est réparti en modules pour les cartes, les menus, les statistiques, la sélection et les événements. Un module de configuration partagé a simplifié la coordination dans le prototype, au prix d'un couplage plus fort entre ces modules.

## Results & learnings / Résultats et apprentissages

**EN**
- The repository contains a playable desktop prototype with a card interface, four tracked indicators, audio and menu flows.
- Separating card data from the UI made it possible to edit and extend event content without rewriting the rendering code.
- The project highlighted the trade-off between quick iteration through shared global state and the maintainability of more independent modules.
- Cards currently come from a random pool; although the code includes classes for narrative threads, branching paths are not connected to the active game flow.
- The local JSON save stores the current card, month counter and indicators, but not the full decision history or narrative progression. Completing and validating narrative paths and broadening save coverage are possible next steps.

**FR**
- Le dépôt contient un prototype de bureau jouable avec une interface à cartes, quatre indicateurs, de l'audio et plusieurs menus.
- La séparation des données de cartes et de l'interface permet de modifier et d'enrichir les événements sans réécrire le code de rendu.
- Le projet a mis en évidence le compromis entre la rapidité d'itération permise par un état global partagé et la maintenabilité de modules plus indépendants.
- Les cartes proviennent actuellement d'un pool aléatoire ; bien que le code comporte des classes pour les fils narratifs, les parcours à embranchements ne sont pas reliés au déroulement actif du jeu.
- La sauvegarde JSON locale conserve la carte courante, le compteur de mois et les indicateurs, mais pas l'historique complet des décisions ni la progression narrative. Compléter et valider les parcours narratifs, puis étendre la sauvegarde, sont des pistes d'évolution.

## Getting started

### Prerequisites

- Python 3 and `pip`
- A desktop environment with graphics and audio support

The repository does not currently provide a dependency lockfile or pinned package versions.

### Install and run

Run the game from `src/`, which is the working directory expected by its relative paths to images, sounds and card data:

```bash
cd src
python -m pip install pyglet numpy
python main.py
```

From the main menu, select **Jouer**, then drag a card left or right to make a decision.

## Project resources / Ressources du projet

**EN**<br>
The [UML design document](UML/REIGNIB_presentation.pdf) records the original design work. Current project tasks are tracked in [GitHub Issues](https://github.com/mlmdc/S6_CPO_Game/issues).

**FR**<br>
Le [dossier de conception UML](UML/REIGNIB_presentation.pdf) présente le travail de conception initial. Les tâches actuelles sont suivies dans les [issues GitHub](https://github.com/mlmdc/S6_CPO_Game/issues).

### Contributors / Contributeurs

- MADEC Maël — [m0madec@enib.fr](mailto:m0madec@enib.fr)
- COLLET Guillaume — [g0collet@enib.fr](mailto:g0collet@enib.fr)
- LE CORFF Louis — [l0lecorf@enib.fr](mailto:l0lecorf@enib.fr)
- LAGADIC Youenn — [y0lagadi@enib.fr](mailto:y0lagadi@enib.fr)
