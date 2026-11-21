# 09-systeme-32

<!-- Corpus menuiserie v3.1.0 — catégorie 09-systeme-32 -->

## Sommaire du fichier
- `engine.drilling` — Positions de perçage normalisées (système 32, charnières, confirmats, coulisses)
- `sys32.principes` — Système 32 : principes et règles de perçage

---

<!-- chunk_id: engine.drilling | source: corpus v3 de l'auteur -->

# Positions de perçage normalisées (système 32, charnières, confirmats, coulisses)

Positions de perçage normalisées utilisées par le générateur de plans. Repère : origine (0,0) = coin **bas-gauche de la face** de la pièce ; `x` = horizontal (le long de la longueur), `y` = vertical (le long de la largeur). Toutes cotes en mm.

## Système 32 — taquets d'étagères (sur les joues)
- **2 rangées verticales** : une près du chant **avant**, une près du chant **arrière** (l'arrière tient compte de l'épaisseur du fond).
- Distance d'une rangée à son chant : **37 mm** (`SYS32_EDGE_SETBACK`).
- **Entraxe vertical : 32 mm**. Premier et dernier trou à **37 mm** des extrémités haut/bas.
- Diamètre **Ø5 mm**, **profondeur 10 mm**.
- Générés uniquement si la zone contient des étagères réglables.

## Cuvettes de charnières Ø35 (sur la porte, face intérieure)
- **Ø35 mm**, **profondeur 12 mm**.
- Centre de la cuvette à **22,5 mm du chant** côté charnière (`HINGE_CUP_SETBACK`).
- Distance haut/bas : **100 mm** du bord (`HINGE_EDGE_OFFSET`).
- Répartition verticale :
  - 1 charnière → au milieu.
  - 2 charnières → à 100 mm du haut et 100 mm du bas.
  - ≥ 3 → 100 mm haut + 100 mm bas, les intermédiaires répartis régulièrement (`pas = (H − 200) / (n − 1)`).
- **Nombre de charnières (formule moteur)** : `n = max(2, ⌈(H − 800) / 500⌉ + 2)`.
  Règle métier équivalente : porte < 600 mm → 2 ; 600–1200 → 3 ; 1200–1800 → 4 ; > 1800 → 5.

## Vis Confirmat — assemblage de caisson
- **Avant-trou** dans le **chant** de la pièce reçue (dessus, dessous, tablette fixe) : **Ø5 mm, profondeur 30 mm**, à **37 mm de chaque extrémité**, sur les chants gauche ET droit.
- **Trou traversant** dans la **face** de la joue : **Ø7 mm, débouchant**, à **37 mm** des chants avant/arrière, à la hauteur de chaque tablette/dessus/dessous.

## Coulisses de tiroir (sur les joues)
- Hauteur de la rangée = bas du tiroir **+ 37 mm** (`SLIDE_SETBACK`).
- **3 points de fixation par tiroir** : avant à **50 mm**, milieu à **profondeur utile / 2**, arrière à **profondeur utile − 50 mm**.
- Vis **Ø4 mm, profondeur 10 mm**.

## Note de cohérence
La profondeur des trous **Ø5 du système 32 est de 10 mm** dans le moteur (les guides généraux citent 12–13 mm, valeur qui concerne surtout les cuvettes de charnières ; 10 mm suffit pour des taquets Ø5).



---

<!-- chunk_id: sys32.principes | source: Hamon & Roullat, Dunod 2022, p119 fiche 55 -->

# Système 32 : principes et règles de perçage

Le **système 32** est le standard industriel mondial de perçage des panneaux pour la quincaillerie de meuble (charnières, taquets, coulisses, vis d'assemblage).

## Règles fondamentales (Hamon & Roullat, Dunod 2022, p119, fiche 55)

| Règle | Valeur |
|---|---|
| Entraxe vertical des perçages | **32 mm** |
| Distance axe perçage / chant vertical | **37 mm** (avant ET arrière) |
| Diamètre taquets, charnières, coulisses, goujons | **Ø 5 mm** |
| Diamètre tourillons | **Ø 6 ou 8 mm** |
| Diamètre collet vis d'assemblage dans côtés | **Ø 7 mm** |

## Application
- Sur **chaque joue (montant vertical)**, on perce **deux rangées verticales** de trous Ø5 mm :
  - une rangée à 37 mm du chant **avant**
  - une rangée à 37 mm du chant **arrière**
- Trous espacés de 32 mm sur toute la hauteur utile.
- Profondeur 12-13 mm (jamais traversant — un panneau de 18 mm doit conserver 5 mm sur l'autre face).

## Pourquoi 32 mm ?
Compromis historique entre densité de positions (suffisamment de choix de hauteur pour les tablettes réglables) et rigidité résiduelle de la joue. Tous les fabricants de quincaillerie (Blum, Hettich, Salice, Häfele) calibrent leurs ferrures sur ce pas.

## Outillage
- Gabarit de perçage système 32 (Bosch, Festool, Trend) : pose-le contre le chant, perce, décale, perce.
- Ou perceuse multibroches industrielle (perceuse à 21 broches Ø5 espacées de 32 mm — un coup de presse perce une joue entière).
- DIY : règle aluminium percée + chevilles d'index pour répétabilité.

## Conséquences pour la conception
- Les **hauteurs de tablettes réglables** sont quantifiées par 32 mm.
- Les **charnières** ont leur platine fixée à 37 mm du chant avant.
- Les **coulisses** se fixent sur les mêmes trous de la rangée arrière.
- Si on veut un meuble propre, **toutes les ferrures doivent tomber sur ces trous** : ne jamais percer hors système.



