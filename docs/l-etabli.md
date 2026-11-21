# L'Établi

Dossier du skill : [`l-etabli/`](../l-etabli). Installation et licence : voir le [README](../README.md).

Un skill pour Claude qui aide à concevoir et fabriquer des meubles et ouvrages en bois sur mesure, en intérieur comme en extérieur non structurel. Il s'adresse aux bricoleurs et aux autodidactes.

Il repose sur un corpus technique de 12 fichiers et sur un script de calcul. Le skill lit le corpus avant de répondre et exécute le script pour tout dimensionnement, au lieu de répondre de mémoire.

## Ce qu'il sait faire

- Dimensionner une tablette : flèche instantanée, flèche finale avec fluage, portée maximale selon le matériau et la charge.
- Choisir un panneau ou une essence selon l'usage, y compris dehors (classes d'emploi).
- Choisir la quincaillerie : charnières, coulisses, fixations murales, visserie.
- Concevoir un caisson, un placard, une bibliothèque, un dressing, un meuble TV, un bureau.
- Dérouler un montage pas à pas et proposer une finition.
- Bloquer une conception dangereuse : meuble haut non fixé, porte trop lourde, meuble suspendu trop chargé, matériau inadapté à l'extérieur.

Exemples de questions :

- « Tablette en mélaminé de 900 mm, 18 mm d'épaisseur, pleine de livres. Ça tient ? »
- « Quel bois pour une jardinière posée en pleine terre ? »
- « Porte en MDF de 1800 × 500 × 18 : combien de charnières ? »

## Contenu

```
l-etabli/
├── SKILL.md              rôle, méthode, contrôles de sécurité, routage
├── CHANGELOG.md
├── references/           corpus technique (01 à 12) et jeu de tests (13)
└── scripts/calc.py       flèche, portée, poids de porte, charnières
```

Le script s'utilise aussi seul, sans dépendance :

```
python3 l-etabli/scripts/calc.py fleche mdf 600 300 18 25
python3 l-etabli/scripts/calc.py portee cp_bouleau 18 300 25
python3 l-etabli/scripts/calc.py porte 1800 500 18 mdf
python3 l-etabli/scripts/calc.py table
```

## D'où viennent les données

Chaque donnée du corpus porte un niveau de provenance, que le skill annonce dans ses réponses.

| Niveau | Origine | Confiance annoncée |
|---|---|---|
| 1 | Normes, notamment EN 622-5, EN 312, EN 300, EN 335, EN 350, EN 204, EN 1995-1-1 (Eurocode 5), DTU 51.4 | sûr |
| 2 | Documentation de fabricants et littérature technique | probable |
| 3 | Règles de l'art et estimations de l'auteur (chunks marqués `corpus v3 de l'auteur`) | hypothèse |

Les normes sont citées par leur code et par quelques seuils. Leur texte n'est pas reproduit ici. Pour un chantier réel, reporte-toi au document officiel.

Plusieurs tableaux et règles s'appuient sur cet ouvrage, cité avec la page à chaque emploi :

> Olivier Hamon, Vincent Roullat, *100 fiches pratiques de menuiserie, agencement et ébénisterie*, Dunod, 2022, ISBN 978-2-10-083086-2.

Le corpus ne contient aucun prix.

## Limites et avertissement

Ce skill est une aide à la conception pour du mobilier et des ouvrages non structurels. Il ne remplace ni un bureau d'études, ni un professionnel, ni la notice du fabricant.

- Il ne calcule pas de structure porteuse : pergola fixée à une façade, garde-corps, plancher, charge de neige ou de vent. Dans ces cas il le dit et renvoie vers les textes applicables.
- Les valeurs de niveau 3 sont des ordres de grandeur.
- Un modèle de langage peut se tromper, même avec un corpus. Vérifie les cotes et les charges avant de couper, de percer ou de suspendre un meuble.
- Fixe au mur tout meuble haut, surtout dans un logement avec des enfants.

Tu utilises ce contenu sous ta seule responsabilité. Il est fourni sans garantie, comme le précise la licence.

## Marques

Blum, Hettich, Salice, Grass, Häfele, IKEA et les autres marques citées appartiennent à leurs propriétaires. Elles sont nommées pour décrire des produits et des cotes courantes. Ce projet n'a aucun lien avec elles.

## Tests

`l-etabli/references/13-evals.md` contient 24 questions à réponse connue. Les valeurs chiffrées se recalculent avec `calc.py`. Relance-les après toute modification du corpus ou du script.
