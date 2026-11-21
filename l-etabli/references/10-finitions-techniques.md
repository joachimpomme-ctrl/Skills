# 10-finitions-techniques

<!-- Corpus menuiserie v3.1.0 — catégorie 10-finitions-techniques -->

## Sommaire du fichier
- `atelier.conseils` — Conseils atelier : du plan à la réalisation (synthèse pratique)
- `didactique.debit-cout` — Didactique : Débit et coût : optimisation panneaux
- `didactique.montage` — Didactique : Montage et notice
- `didactique.pieces` — Didactique : Pièces du meuble : rôle et règles
- `didactique.portes-tiroirs` — Didactique : Portes et tiroirs : règles pratiques
- `didactique.structure` — Didactique : Concepts structurels du meuble panneau
- `didactique.validation` — Didactique : Validation et alertes
- `engine.procurement` — Décisions d'approvisionnement : acheter, retoucher ou débiter
- `finitions.synthese` — Finitions : cire, huile, vernis, gomme-laque (4 familles)

---

<!-- chunk_id: atelier.conseils | source: corpus v3 de l'auteur -->

# Conseils atelier : du plan à la réalisation (synthèse pratique)

Synthèse pratique pour passer du plan à la réalisation. Concentre les conseils chantier les plus impactants.

## Avant de couper
- Vérifier les alertes de validation (erreurs bloquantes en rouge).
- Identifier le type de mur (béton / brique / placo) pour choisir les chevilles.
- Mesurer la largeur du mur en 4 points (sol, 50 cm, 120 cm, plafond) — prendre la **plus petite valeur**. Les murs ne sont jamais droits.
- Idem pour la hauteur sol-plafond : 4 points, plus petite valeur.

## Trait de scie (kerf)
- Trait standard scie circulaire : **3 mm**.
- Trait scie japonaise / lame fine : 1.5-2 mm.
- À déclarer dans le calepinage pour ne pas obtenir des pièces trop courtes.

## Bandes de chant
- Appliquer les bandes **AVANT l'assemblage** (sur les chants visibles).
- Fer à repasser (bandes thermo-collantes) ou plaqueuse de chant.
- Toujours tester sur une chute pour ajuster température / pression.
- Ordre de plaquage : chants de longueur en premier, puis chants de largeur (recouvrent les premiers).

## Perçage système 32
- Diamètre 5 mm, profondeur 12 mm.
- Entraxe vertical 32 mm, axe à 37 mm du chant avant et du chant arrière.
- Gabarit indispensable pour la régularité (cher du commerce, ou DIY avec une règle alu percée).

## Anti-basculement
- Tout meuble > 1,5 m de hauteur doit être fixé au mur (norme sécurité enfants).
- Équerre anti-basculement (commerce) ou tasseau vissé au mur entre le meuble et le mur (caché par le bandeau).

## Fond de meuble
- HDF ou CP fin (3-6 mm). N'est pas optionnel.
- Sans fond, le meuble se déforme en losange dans le temps (perd l'équerrage).
- Rainurer dans les joues et tablettes (idéal) ou agrafer à l'arrière (plus simple).

## Montage à blanc
- TOUJOURS monter à blanc (sans colle) avant l'assemblage définitif.
- Vérifier l'équerrage : 2 diagonales égales à 1-2 mm près.
- Identifier les ajustements à faire avant qu'il ne soit trop tard.

## Fixation au mur
- **Béton** : cheville à expansion Ø8 mm, vis 6×60.
- **Brique creuse** : cheville Fischer SX, ou chimique pour gros poids.
- **Placo** : cheville Molly à expansion ou Multi-Materials. Idéal : fixer dans les montants métalliques (ossature).
- Fixation suspendue : ferrures Ø8 minimum, 2 par corps minimum. Au-delà de 25 kg sur placo, prévoir Molly + montants.

## Équerrage
- Mesurer les **deux diagonales** d'un caisson rectangulaire.
- Égales à 1-2 mm près = bon. Sinon, ajuster avant collage/séchage.
- Le fond rainuré aide à tenir l'équerrage durant le séchage.



---

<!-- chunk_id: didactique.debit-cout | source: corpus v3 de l'auteur -->

# Didactique : Débit et coût : optimisation panneaux

Explications pédagogiques pour les concepts de la catégorie « Débit et coût : optimisation panneaux ».

## panneaux-total
Nombre de panneaux bruts nécessaires après optimisation. L'algorithme teste 6 stratégies et garde la meilleure.

## rendement
Pourcentage de matière utilisée. > 70% c'est bon. < 50%, réorganiser ou changer de format de panneau.

## surface-utile
Surface totale de bois qui devient des pièces du meuble.

## surface-chute
Surface perdue en chutes. Garder les grandes chutes pour futurs projets.

## strategie
Algorithme qui a donné le meilleur résultat. « Étagère » = ligne par ligne. « Guillotine » = coupes droites successives.

## trait-scie
Épaisseur du trait de scie en mm. Scie circulaire ≈ 3 mm. Matière perdue à chaque coupe.

## piece-non-placable
Pièces trop grandes pour un seul panneau, même tournées. Réduire la pièce ou choisir panneau plus grand.

## rotation
Le symbole ↻ indique que la pièce a été tournée 90° pour mieux s'insérer.

## prix-panneau
Prix d'achat panneau brut HT. Varie selon négoce, quantité, qualité.

## cout-total
Coût total panneaux bruts, sans quincaillerie ni finition.

## cout-chutes
Part du coût qui finit en chutes. Indication pour juger l'économie du calepinage.



---

<!-- chunk_id: didactique.montage | source: corpus v3 de l'auteur -->

# Didactique : Montage et notice

Explications pédagogiques pour les concepts de la catégorie « Montage et notice ».

## elevation
Vue de face du meuble. Rectangles colorés = joues et tablettes. Pointillés = tablettes réglables.

## joint-corps
Ligne pointillée jaune indiquant la hauteur de joint entre joues basses et hautes (à 180 cm). Tablette fixe à ce niveau renforce et cache le joint.

## releve-cotes
Avant toute découpe, vérifier les dimensions sur place. Murs/sols/plafonds jamais parfaits. Mesurer en au moins 4 points.

## debit-notice
Étape de découpe. Faire couper les grandes pièces en magasin (gratuit ou facturé à la coupe selon l'enseigne) puis affiner à la scie circulaire sur rail.

## rainures
Rainures pour crémaillères métalliques de tablettes réglables. Défonceuse + guide parallèle.

## percages-sys32
Système 32 = standard industriel pour taquets. Tous les 32 mm, à 37 mm du bord. Gabarit indispensable.

## decoupe-plinthe
Entailler le bas de chaque joue pour enjamber la plinthe murale. Le meuble se plaque au mur tout en restant posé au sol.

## assemblage
Montage corps par corps, à plat sur tréteaux. Coller + visser tablettes fixes, vérifier équerrage (diagonales égales à 2 mm près).

## equerrage
Vérifier que le corps est bien rectangle (pas en losange). Mesurer les 2 diagonales : égales à 2 mm près = bon.

## mise-en-place
Poser le premier corps contre le mur, vérifier verticalité au niveau (2 axes), caler si besoin, fixer au mur (2-3 vis + chevilles).

## finitions
Bandeaux de plafond, jonctions entre corps, finitions de surface (vernis/huile/peinture) en dernier.



---

<!-- chunk_id: didactique.pieces | source: corpus v3 de l'auteur -->

# Didactique : Pièces du meuble : rôle et règles

Explications pédagogiques pour les concepts de la catégorie « Pièces du meuble : rôle et règles ».

## piece-joue
La joue est un montant vertical (gauche ou droit). Elle fait toute la hauteur utile et porte le meuble. Pièce structurelle principale.

## piece-tablette-fixe
Tablette permanente collée + vissée. Rigidifie le corps. Minimum 2 par corps (haut + bas).

## piece-tablette-reglable
Tablette posée sur taquets amovibles, repositionnable. Installer en dernier.

## piece-bandeau
Pièce décorative (souvent en haut) qui cache l'espace meuble-plafond. Aspect fini et intégré.

## piece-porte
Pièce mobile sur charnières. Prévoir 2 mm de jeu. Largeur max 60 cm en 18 mm (risque de voile).

## piece-tiroir-facade
Façade qui recouvre l'ouverture du tiroir. Mêmes règles de jeu que les portes. Vis depuis l'intérieur du caisson tiroir.

## piece-fond
Le fond rigidifie le caisson. Généralement HDF/CP 3-6 mm, rainuré ou agrafé. Indispensable pour l'équerrage.

## piece-longueur
Plus grande dimension. Pour une joue : sa hauteur. Pour une tablette : sa portée.

## piece-largeur
Plus petite dimension. Pour une joue : profondeur du meuble. Pour une tablette : aussi la profondeur.

## piece-qty
Nombre d'exemplaires identiques à découper. Ex : 2 joues par corps, 3 tablettes réglables identiques.



---

<!-- chunk_id: didactique.portes-tiroirs | source: corpus v3 de l'auteur -->

# Didactique : Portes et tiroirs : règles pratiques

Explications pédagogiques pour les concepts de la catégorie « Portes et tiroirs : règles pratiques ».

## charniere
Charnière standard Ø35 mm (Blum/Hettich) s'encastre dans une cuvette fraisée. Réglable 3 axes après pose. 2 charnières < 60 cm, 3 au-delà.

## porte-pose
3 poses : enveloppante (recouvre la joue), demi-recouvrement (2 portes même joue), affleurante (dans le cadre). Coudure différente selon pose.

## porte-pose-enveloppante
Enveloppante : la porte recouvre entièrement le chant de la joue. Charnière coudure 0 mm. Jeu 2 mm entre portes.

## porte-pose-demi-recouvrement
Demi-recouvrement : recouvre moitié du chant. Pour 2 portes sur même joue centrale. Coudure = demi-épaisseur joue.

## porte-pose-affleurante
Affleurante : la porte s'insère dans le cadre, affleurant le chant. Le plus élégant mais le plus exigeant. Jeu 2 mm tout autour.

## porte-jeu
Toujours 2 mm de jeu entre portes adjacentes ET en haut/bas. Sans jeu : frottement. Trop : aspect négligé.

## tiroir-coulisse
Galets (économique, ouverture 75%) ou billes (sortie totale, plus robuste). 12.5 mm de jeu latéral chaque côté.

## tiroir-dim
Hauteur caisson tiroir = hauteur façade − 25 mm. Profondeur = profondeur intérieure − 10 mm. Fond HDF 3 mm rainuré à 8 mm du bas.



---

<!-- chunk_id: didactique.structure | source: corpus v3 de l'auteur -->

# Didactique : Concepts structurels du meuble panneau

Explications pédagogiques pour les concepts de la catégorie « Concepts structurels du meuble panneau ».

## materiau
Le choix du matériau conditionne tout : solidité, esthétique, prix et méthodes d'assemblage. Le contreplaqué bouleau est le plus polyvalent pour un meuble sur mesure.

## densite
La densité (kg/m³) indique le poids du matériau. Plus c'est dense, plus c'est lourd mais souvent plus résistant. Le MDF (750) est plus lourd que l'OSB (600).

## flexMPa
La résistance en flexion (MOR, en MPa) mesure la charge de rupture. Ne pas la confondre avec le module d'élasticité E, qui gouverne la flèche : c'est E (chunk `materiau.mecanique`) qui dicte les portées, pas le MOR.

## portee-max
La portée max est la longueur maximale d'une tablette sans support intermédiaire. Elle dépend du matériau (E), de l'épaisseur, de la charge réelle (livres ≈ 25 kg/m, pas 8) et du fluage. Valeurs par matériau dans `materiau.mecanique`, calcul via `scripts/calc.py`.

## vis
La tenue des vis dans le matériau. « Excellent » = vis directe possible. « Faible » = il faut des excentriques ou tourillons, jamais de vis dans les chants.

## largeur-mur
Mesurer la largeur du mur à 4 hauteurs différentes (sol, 50 cm, 120 cm, plafond) et prendre la plus petite valeur. Les murs ne sont jamais parfaitement droits.

## hauteur-plafond
Mesurer la hauteur sol-plafond à 4 points différents. Les plafonds varient souvent de 1-2 cm. Prendre la plus petite valeur pour éviter les mauvaises surprises.

## hauteur-plinthe
La plinthe existante au pied du mur. On entaille le bas des joues pour que le meuble se plaque contre le mur. Typiquement 7-10 cm.

## profondeur-plinthe
L'épaisseur de la plinthe murale. L'entaille en bas des joues doit être au moins aussi profonde pour que le meuble touche le mur.

## panneau
Le panneau est la plaque de bois brute dans laquelle on découpe toutes les pièces. Formats standards France : 250×125 cm (courant) ou 305×152 cm (grand).

## panneau-largeur
Largeur du panneau brut en cm. Format courant : 250 cm. C'est dans ce panneau qu'on optimise le placement de toutes les pièces.

## panneau-hauteur
Hauteur du panneau brut en cm. Format courant : 125 cm. Un panneau 250×125 pèse ~30 kg en CP bouleau 18 mm.

## panneau-epaisseur
L'épaisseur en cm (1.8 = 18 mm). Standard meuble : 18 mm. Pour les fonds : 6 mm.

## corps
Un « corps » est un module indépendant du meuble. On assemble chaque corps séparément puis on les fixe côte à côte (mur ou entre eux). Facilite transport et montage.

## corps-largeur
Largeur extérieure du corps. Largeur intérieure (pour tablettes) sera réduite de 2× épaisseur du panneau (joues gauche/droite).

## corps-profondeur
Profondeur du corps de l'arrière vers l'avant. 25-30 cm pour livres, 35-40 cm pour dressing/buffet, 50-60 cm pour plan de travail.

## int-tablette
Largeur intérieure utile = largeur corps − 2× épaisseur joues. C'est la longueur des tablettes.

## poids-corps
Poids estimé de toutes les pièces du corps (basé sur la densité du matériau). Utile pour transport et fixation murale.



---

<!-- chunk_id: didactique.validation | source: corpus v3 de l'auteur -->

# Didactique : Validation et alertes

Explications pédagogiques pour les concepts de la catégorie « Validation et alertes ».

## erreur
Bloquante : problème dimensionnel concret (pièce > panneau, joues mauvaise hauteur, etc.).

## avertissement
Risque potentiel. On peut continuer, mais vérifier et corriger si nécessaire.

## flexion
Flèche = courbure d'une tablette sous charge. Au-delà de L/200, déformation visible. Réduire portée ou augmenter épaisseur.

## formaldehyde
Composé volatil irritant des colles. France : E1 obligatoire depuis 2006. Préférer E0.5 pour intérieur.

## orientation-debit
CP et OSB ont un sens de fil affectant résistance et esthétique. MDF et mélaminé : pas de sens.



---

<!-- chunk_id: engine.procurement | source: corpus v3 de l'auteur -->

# Décisions d'approvisionnement : acheter, retoucher ou débiter

Pour chaque pièce, le projet tranche : **l'acheter toute faite, l'acheter et la retoucher, ou la débiter** dans un panneau. C'est l'arbitrage entre gain de temps (pièces standard du commerce) et flexibilité (débit sur mesure).

## Les 3 statuts
| Statut | Sens |
|---|---|
| `buy_exact` | Acheter un produit catalogue **utilisable tel quel** |
| `buy_and_rework` | Acheter un produit catalogue **puis le retoucher** en atelier |
| `cut_from_sheet` | **Débiter** la pièce dans un panneau (sur mesure) |

## Opérations de retouche possibles
- **perçage** (drilling)
- **plaquage de chant** (edge_banding)

(liste volontairement extensible : recoupe, surfaçage, découpe… à venir)

## Heuristique de décision
1. Pas de référence catalogue associée → **`cut_from_sheet`** (« pièce sur mesure : à débiter »).
2. Référence catalogue **+ perçage ou plaquage requis** → **`buy_and_rework`** (« acheter X puis perçage + plaquage de chant en atelier »).
3. Référence catalogue **seule**, sans retouche → **`buy_exact`** (« produit X utilisable tel quel »).

Les compteurs de synthèse (combien à acheter / retoucher / débiter) sont **pondérés par les quantités** de chaque pièce.



---

<!-- chunk_id: finitions.synthese | source: Hamon & Roullat, Dunod 2022 -->

# Finitions : cire, huile, vernis, gomme-laque (4 familles)

Les 4 finitions principales pour bois massif et CP en menuiserie meuble (Hamon & Roullat, Dunod 2022 p78 fiche 39).

## 1. Cire
- **Application** : manuelle au pinceau, chiffon ou mèche de coton.
- **Brillant** : obtenu par lustrage après séchage.
- **Avantages** : facile, naturel, réparable.
- **Inconvénients** : peu résistant à l'humidité et aux taches. Renouvellement annuel.
- **Usage** : meubles décoratifs, peu sollicités.

## 2. Huile (lin, dure)
- **Application** : manuelle, pénètre dans le bois.
- **Pénétration** : l'huile de lin peut être fluidifiée au bain-marie à 60 °C.
- **Avantages** : aspect mat naturel, met en valeur le veinage, réparable, sain (sans solvant si huile dure naturelle).
- **Inconvénients** : protection limitée, plusieurs couches nécessaires.
- **Usage** : tables, plans de travail, mobilier nature.

## 3. Vernis (PU, acrylique, polyester)
- **Application** : pinceau, rouleau ou tampon. Dernier passage dans le sens du veinage.
- **Avantages** : protection maximale (eau, taches, rayures), brillance variable (mat, satiné, brillant).
- **Inconvénients** : films épais, irréparable localement (ponçage complet nécessaire).
- **Usage** : meubles très sollicités, salle de bain, cuisine.

## 4. Vernis gomme-laque
- **Application** : au tampon avec mèche dans tissu de coton.
- **Avantages** : finition très brillante traditionnelle.
- **Inconvénients** : fragile (alcool, eau), savoir-faire requis.
- **Usage** : restauration, mobilier ancien.

## Choix synthèse
| Sollicitation | Finition |
|---|---|
| Décoratif sec | Cire |
| Usage normal salon/chambre | Huile dure |
| Cuisine, salle de bain, enfants | Vernis PU mat |
| Restauration ancien | Gomme-laque |



