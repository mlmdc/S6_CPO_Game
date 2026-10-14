# Changelog #fusion-functions
Branche fusion-functions du projet : l'objectif est de relier la partie graphique développée en Pyglet avec la partie distribution des cartes. En parallèle, le cadre de l'application est développé afin de faciliter la suite du developpement par découpage en modules. 

## Changements

### Harmonisation des cartes (07/11/23)
Le [commit](https://git.enib.fr/y0lagadi/CPO_02_Groupe2/-/commit/424a522feff2508bf2b22cedd16cf70832a75df0) a pour objectif d'harmoniser les noms avec ceux du diagramme de classe de conception. Par exemple :

```bash
def afficher_carte(self, fenetre, angle_rotation):
```
devient

```bash
def showCard(self, fenetre, angle_rotation):
```
De plus, des ajouts de code sont effectués pour des usages postérieurs.

### Creation de cfg, tools, init, display_events, cardlib
Les fichiers ont les rôles suivants :
- cfg.py est le fichier config/cfg des guidelines python. Son rôle est le partage de variables globales à travers les fichiers.
- tools.py est similaire à utils, dans la fourniture de fonctions utilitaires.
- init.py sert à garnir les variables globales de cfg de manière controlée.
- display_events gère spécifiquement les évenements de la fenetre
- cardlib est un fichier lib qui propose le chargement dans la mémoire les png et les cartes que les autres fichiers peuvent ensuite utiliser.

### Update de card.py
```bash
def __redimensionner_sprite(self, taille):
    self.sprite.width = taille
```
devient

```bash
def __redimensionner_sprite(self, taille):
    self.sprite.update(scale_x = (taille/self.sprite.width)
                        ,scale_y= (taille/self.sprite.height))
```
car les attributs width et height de pyglet.sprite deviennent dans une mise à jour privés et donc uniquement addressables à travers update(...).

### Bugfix de selector.py
Modification du système de sélection de cartes car l'opération '==' n'existe pas pour les objets d'une même classe. Le résultat est le même

### Bugfix de thread.py
La fonction cardGive() est modifié pour le nouveau système de sélection.

### Finition de la classe RandomThread
L'auto-remplissage depuis un pool de cartes random a été implémenté. 

### Template (jj/mm/aa)
Le [hypertexte](https://lien/) lorem ipsum.

```bash
template
```

## Contributeurs

- m0madec
