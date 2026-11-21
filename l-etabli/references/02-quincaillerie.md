# 02-quincaillerie

<!-- Corpus menuiserie v3.1.0 — catégorie 02-quincaillerie -->

## Sommaire du fichier
- `quincaillerie.amortisseurs_rapportes` — Quincaillerie : Amortisseurs rapportes
- `quincaillerie.assemblage_caisson` — Quincaillerie : Assemblage caisson
- `quincaillerie.chants_adhesifs` — Quincaillerie : Chants adhesifs
- `quincaillerie.charnieres_invisibles` — Quincaillerie : Charnieres invisibles
- `quincaillerie.charnieres_speciales` — Quincaillerie : Charnieres speciales
- `quincaillerie.charnieres_synthese` — Charnières : synthèse des 4 types courants (Ø35, 170°, piano, invisible)
- `quincaillerie.compas_et_verins` — Quincaillerie : Compas et verins
- `quincaillerie.coulisses_tiroir` — Quincaillerie : Coulisses tiroir
- `quincaillerie.ferrures_table_extensible` — Quincaillerie : Ferrures table extensible
- `quincaillerie.fixation_murale` — Quincaillerie : Fixation murale
- `quincaillerie.formulas` — Quincaillerie : formules de calcul (charnières, coulisses, perçages)
- `quincaillerie.pieds_et_plinthes` — Quincaillerie : Pieds et plinthes
- `quincaillerie.poids_max_porte` — Quincaillerie : Poids max porte
- `quincaillerie.poignees_et_boutons` — Quincaillerie : Poignees et boutons
- `quincaillerie.portes_pose` — Portes battantes : 4 types de pose (enveloppante, demi-recouvrement, appliquée, affleurante)
- `quincaillerie.quincaillerie_lit` — Quincaillerie : Quincaillerie lit
- `quincaillerie.regles_de_choix` — Quincaillerie : règles de choix (matrice de décision)
- `quincaillerie.serrures_et_verrous` — Quincaillerie : Serrures et verrous
- `quincaillerie.systemes_push_to_open` — Quincaillerie : Systemes push to open
- `quincaillerie.taquets_etagere` — Quincaillerie : Taquets etagere
- `quincaillerie.tiroirs_synthese` — Tiroirs : synthèse coulisses (galets / billes / invisibles) + dimensionnement

---

<!-- chunk_id: quincaillerie.amortisseurs_rapportes | source: corpus v3 de l'auteur -->

# Quincaillerie : Amortisseurs rapportes

- **types** :
  - À percer (cylindre dans le chant)
  - À visser (en applique sur platine)
- **percage encastrement** :
  - **diametre mm** : 10
  - **profondeur mm** : 50
- **positionnement** : Côté poignée pour levier optimal, au centre ou près des points d'impact
- **references** :
  - Blumotion à percer (Blum)
  - Smove (Salice)



---

<!-- chunk_id: quincaillerie.assemblage_caisson | source: corpus v3 de l'auteur -->

# Quincaillerie : Assemblage caisson

- **description** : Quincaillerie pour assembler les pièces du caisson entre elles
- **tourillons** :
  - **description** : Chevilles bois pour assemblage collé
  - **diametres mm** :
    - 6
    - 8
    - 10
  - **diametre courant mm** : 8
  - **longueur mm** :
    - **min** : 30
    - **max** : 40
  - **percage mm** :
    - **diametre** : = diamètre tourillon
    - **profondeur** : moitié longueur tourillon + 1mm
  - **espacement mm** :
    - **min** : 100
    - **max** : 150
  - **colle** : Colle à bois vinylique (D3 pour pièces humides)
  - **usage** : Assemblage définitif, invisible, très résistant
  - **note** : Nécessite un gabarit de perçage pour alignement précis
- **lamelles biscuits** :
  - **description** : Plaquettes ovales en hêtre compressé (type Lamello)
  - **tailles** :
    - **0** :
      - **longueur mm** : 47
      - **largeur mm** : 15
      - **epaisseur mm** : 4
      - **epaisseur bois min mm** : 10
    - **10** :
      - **longueur mm** : 53
      - **largeur mm** : 19
      - **epaisseur mm** : 4
      - **epaisseur bois min mm** : 12
    - **20** :
      - **longueur mm** : 56
      - **largeur mm** : 23
      - **epaisseur mm** : 4
      - **epaisseur bois min mm** : 15
  - **rainure** :
    - **largeur mm** : 4
    - **profondeur mm** :
      - **min** : 10
      - **max** : 13
  - **outil** : Fraiseuse à lamelles (lamelleuse / biscuit jointer)
  - **espacement mm** :
    - **min** : 100
    - **max** : 200
  - **colle** : Colle à bois vinylique
  - **usage** : Assemblage rapide, bon alignement, assez résistant
- **vis assemblage** :
  - **eurovis** :
    - **description** : Vis spéciale ameublement à tête fraisée
    - **diametre mm** : 6.3
    - **longueur mm** :
      - 11
      - 13
      - 16
    - **percage avant trou mm** :
      - **diametre** : 4
      - **profondeur** : longueur vis
    - **usage** : Fixation embases de charnières, quincaillerie sur panneau
  - **vis confirmation** :
    - **description** : Vis d'assemblage de panneaux (type Confirmat / Euroschraube)
    - **diametre mm** :
      - **tete** : 7
      - **filetage** : 5
    - **longueur mm** :
      - 40
      - 50
      - 70
    - **percage panneau traverse mm** : 7
    - **percage panneau receveur mm** : 5
    - **profondeur vis min mm** : 30
    - **usage** : Assemblage rapide de caissons en panneaux de particules/MDF
  - **vis bois classique** :
    - **diametres courants mm** :
      - 3.5
      - 4
      - 4.5
      - 5
    - **regle percage** : Avant-trou = 60-70% du diamètre de la vis dans le bois dur, 50% dans le résineux
    - **note** : Toujours pré-percer dans les panneaux dérivés pour éviter l'éclatement
- **excentriques** :
  - **description** : Système boîtier excentrique + goujon pour assemblage démontable
  - **diametre boitier mm** :
    - **standard** : 15
    - **alternatif** : 20
  - **goujon** :
    - **diametre mm** :
      - **min** : 5
      - **max** : 7
    - **longueur mm** :
      - **min** : 24
      - **max** : 34
  - **percage boitier** :
    - **diametre mm** : 15
    - **profondeur mm** : 12.5
    - **distance chant mm** :
      - **min** : 34
      - **note** : Centre du perçage à 34mm du chant d'assemblage
  - **percage goujon** :
    - **diametre mm** : 5
    - **profondeur mm** : 13
    - **note** : Dans le chant du panneau receveur
  - **usage** : Meubles en kit, assemblage/démontage possible
  - **note** : Quart de tour pour verrouiller



---

<!-- chunk_id: quincaillerie.chants_adhesifs | source: corpus v3 de l'auteur -->

# Quincaillerie : Chants adhesifs

- **materiaux** :
  - **melamine pre encollee** :
    - **epaisseur mm** :
      - 0.3
      - 0.4
    - **pose** : Fer à repasser ~160°C
    - **usage** : Bricoleur standard
  - **ABS PVC** :
    - **epaisseur mm** :
      - 0.8
      - 1
      - 2
    - **pose** : Plaqueuse (pro) ou pré-encollé + fer
    - **usage** : Résistance chocs, cuisine/SdB
  - **placage bois** :
    - **epaisseur mm** :
      - 0.5
      - 0.6
      - 1.5
    - **pose** : Colle contact + ponçage + finition
    - **usage** : Haut de gamme
- **choix largeur selon panneau mm** :
  - **panneau 16** :
    - 19
    - 22
  - **panneau 18** :
    - 22
    - 23
  - **panneau 25** :
    - 28
    - 30
  - **panneau 38** :
    - 40
    - 42
- **regle surplus** : Largeur chant = épaisseur panneau + 2-4mm (arasé après pose)
- **regles** :
  - ABS 1-2mm sur chants exposés cuisine/SdB
  - Mélamine auto-adhésive : retouche uniquement, pas durable sur chant brut sollicité
  - Araser au coupe-chant ou cutter après pose



---

<!-- chunk_id: quincaillerie.charnieres_invisibles | source: corpus v3 de l'auteur -->

# Quincaillerie : Charnieres invisibles

- **description** : Charnières à encastrer (cup hinges) — standard de l'industrie du meuble
- **principe** : Boîtier cylindrique encastré dans la porte + embase vissée sur le côté du caisson
- **boitier** :
  - **diametres standard mm** :
    - 26
    - 35
  - **diametre courant mm** : 35
  - **profondeur encastrement mm** :
    - **min** : 11
    - **max** : 13
    - **standard** : 12
  - **distance centre boitier chant porte mm** :
    - **formule** : centre = 17.5 + K
    - **K mm** :
      - **min** : 3
      - **standard** : 4
      - **max** : 7
    - **resultat mm** :
      - **min** : 20.5
      - **standard** : 21.5
      - **max** : 24.5
    - **note** : K = distance bord perçage Ø35 au chant de porte. Cote variable selon modèle.
  - **outil requis** : Fraise Forstner Ø35mm (ou Ø26mm pour ancien standard)
  - **note** : Profondeur boîtier < épaisseur porte — vérifier impérativement
- **types pose** :
  - **applique** :
    - **autre nom** : recouvrement total
    - **description** : La porte recouvre entièrement le côté du caisson
    - **coudure mm** : 0
    - **recouvrement mm** :
      - **standard** : 16
      - **max** : 25
    - **jeu mm** : 0
    - **usage** : 80% des installations — porte unique sur un côté de caisson
  - **demi recouvrement** :
    - **autre nom** : semi-applique
    - **description** : La porte recouvre partiellement le côté (2 portes sur un montant central)
    - **coudure mm** : 9
    - **recouvrement mm** :
      - **standard** : 8
      - **note** : Moitié de l'épaisseur du montant
    - **jeu entre portes mm** :
      - **min** : 2
      - **max** : 3
    - **usage** : Deux portes juxtaposées sur un même montant intermédiaire
  - **rentrant** :
    - **autre nom** : encastré / affleurant
    - **description** : La porte est contenue à l'intérieur du caisson
    - **coudure mm** : 16
    - **recouvrement mm** : 0
    - **jeu mm** :
      - **min** : 2
      - **max** : 3
      - **note** : Encombrement nécessaire à l'ouverture
    - **usage** : Esthétique épurée, portes affleurantes
- **angles ouverture** :
  - **standard deg** : 110
  - **courant deg** :
    - 95
    - 110
  - **grand angle deg** :
    - 135
    - 150
    - 165
  - **usage grand angle** : Meubles d'angle, accès élargi, portes à angle non droit
- **embase** :
  - **description** : Plaque de fixation sur le côté du caisson
  - **distance fixation chant avant mm** : 37
  - **entraxe fixation mm** :
    - **systeme 32 pas vertical caisson mm** : 32
    - **schemas percage boitier porte** :
      - **blum clip top** : 45/9.5 mm
      - **salice** : 48/6 mm
      - **hettich sensys** : 52/5.5 mm
    - **note** : Schémas bidimensionnels (distance horizontale / distance verticale). 32mm = pas vertical du système 32 sur le caisson, PAS un entraxe de boîtier.
  - **note entraxe** : L'entraxe désigne la distance entre les vis de fixation du boîtier dans la porte. 52mm = Hettich Sensys. 48mm = Salice. 45mm = ancien standard.
  - **types montage** :
    - à visser
    - clip-on (sans outil)
    - à expansion (Fix Hettich)
  - **reglages 3D** :
    - **hauteur mm** :
      - **amplitude** : 3
    - **profondeur mm** :
      - **amplitude** : 3
      - **outil** : vis sans fin
    - **derive laterale mm** :
      - **amplitude** : 3
- **nombre charnieres** :
  - **regle** : Le nombre dépend de la hauteur ET du poids (abaque fabricant). Valeurs pour largeur standard ≤ 600mm.
  - **details** :
    - 
      - **hauteur porte mm** :
        - **max** : 900
      - **poids max kg** : 8
      - **nb charnieres** : 2
    - 
      - **hauteur porte mm** :
        - **min** : 900
        - **max** : 1600
      - **poids max kg** : 13
      - **nb charnieres** : 3
    - 
      - **hauteur porte mm** :
        - **min** : 1600
        - **max** : 2000
      - **poids max kg** : 17
      - **nb charnieres** : 4
    - 
      - **hauteur porte mm** :
        - **min** : 2000
        - **max** : 2400
      - **poids max kg** : 22
      - **nb charnieres** : 5
  - **position premiere mm** :
    - **min** : 60
    - **max** : 100
    - **note** : Distance du bord haut ou bas de la porte
  - **note** : Répartir les charnières intermédiaires de manière régulière
- **epaisseur porte** :
  - **standard mm** :
    - **min** : 16
    - **max** : 24
  - **porte fine mm** :
    - **min** : 10
    - **max** : 15
    - **charniere** : modèles spéciaux (Tiomos M9, Sensys thin door)
  - **porte epaisse mm** :
    - **min** : 24
    - **max** : 35
    - **note** : Nécessite embases adaptées
- **amortissement** :
  - **types** :
    - intégré à la charnière (Blumotion, Silentia, Sensys)
    - amortisseur rapporté (clip séparé)
    - sans amortissement
  - **recommandation** : Privilégier l'amortissement intégré pour le bricoleur (plus simple, fiable)
- **marques reference** :
  - **hettich** :
    - **gammes** :
      - Sensys (entraxe 52mm)
      - Intermat (entraxe 52mm)
    - **note** : Leader allemand
  - **blum** :
    - **gammes** :
      - Clip Top Blumotion (entraxe 45/9.5mm)
    - **note** : Référence cuisine haut de gamme
  - **salice** :
    - **gammes** :
      - Silentia+ (entraxe 48mm)
      - Logica
    - **note** : Italien, très courant
  - **grass** :
    - **gammes** :
      - Tiomos
    - **note** : Haut de gamme autrichien



---

<!-- chunk_id: quincaillerie.charnieres_speciales | source: corpus v3 de l'auteur -->

# Quincaillerie : Charnieres speciales

- **pour verre** :
  - **epaisseur verre mm** :
    - 4
    - 5
    - 6
  - **percage mm** :
    - 26
    - 35
  - **note** : Coquille avec cache décoratif. Modèles sans perçage par mâchoire pour petites charges.
- **pour cadre aluminium** :
  - **epaisseur cadre min mm** : 19
  - **fixation** : Vis de blocage ou équerres dans les rainures du profilé alu
- **pour angle** :
  - **bi fold** :
    - **angle deg** : 60
    - **usage** : Charnière intermédiaire entre 2 portes pliantes
  - **grand angle** :
    - **angle deg** :
      - 155
      - 170
    - **usage** : Charnière fixant la première porte pliante au caisson
- **pour portes epaisses** :
  - **epaisseur mm** :
    - **min** : 24
    - **max** : 32
- **pour portes fines** :
  - **epaisseur mm** :
    - **min** : 8
    - **max** : 15
  - **note** : Thin-door spécifique



---

<!-- chunk_id: quincaillerie.charnieres_synthese | source: corpus v3 de l'auteur -->

# Charnières : synthèse des 4 types courants (Ø35, 170°, piano, invisible)

Synthèse des 4 types de charnières les plus courantes en menuiserie meuble.

## 1. Charnière à encastrer Ø35 mm — STANDARD INDUSTRIEL
- **Ouverture** : 95-110° (modèles standard)
- **Cuvette** : Ø35 mm fraisée dans la porte, profondeur 12-13 mm
- **Distance axe cuvette / chant porte** : 21-22 mm
- **Réglages** : 3 axes (hauteur, profondeur, latéral) après pose
- **Platine** : vissée sur la joue, axe à 37 mm du chant avant (système 32)
- **Marques** : Blum (CLIP top BLUMOTION), Hettich (Sensys, Intermat), Grass (Tiomos), Salice
- **Usage** : LE CHOIX par défaut. 95% des meubles modernes.

## 2. Charnière grand angle 170°
- **Ouverture** : 170° (porte plate contre joue adjacente)
- **Même cuvette Ø35**
- **Déport plus important** : nécessite un dégagement
- **Usage** : meubles d'angle, accès à un compartiment derrière la porte ouverte.

## 3. Charnière piano (continue)
- **Ouverture** : 180°
- **Charnière continue** sur toute la hauteur de la porte
- **Fixation** : vis tous les 5-8 cm
- **Aspect** : visible (décoratif ou industriel)
- **Pas de réglage** après pose
- **Usage** : portes très lourdes, abattants de banquette coffre, malles, coffrets.

## 4. Charnière invisible (à tiges, pot)
- **Ouverture** : 90-110°
- **Entièrement invisible** porte fermée
- **Mortaisage** dans le chant de la porte ET dans la joue
- **Outillage** : défonceuse + gabarit
- **Usage** : portes de prestige, design contemporain affleurant.

## Règles de dimensionnement (par porte)
| Hauteur porte | Nb charnières |
|---|---|
| < 60 cm | 2 |
| 60 – 120 cm | 3 |
| 120 – 180 cm | 4 |
| > 180 cm | 5 |

## Charges admissibles charnière Ø35
- Standard : 5-8 kg / charnière
- Renforcée : 10-15 kg
- Spéciale (lourd) : 20-25 kg (Blum CLIP top BLUMOTION 71B3550)

## Position de fixation sur la porte
- Charnière haute : 70-100 mm du bord supérieur
- Charnière basse : 70-100 mm du bord inférieur
- Charnières intermédiaires : réparties régulièrement



---

<!-- chunk_id: quincaillerie.compas_et_verins | source: corpus v3 de l'auteur -->

# Quincaillerie : Compas et verins

- **description** : Systèmes pour portes relevables (meubles hauts, coffres)
- **types** :
  - **verin a gaz** :
    - **description** : Piston pneumatique pour maintien en position ouverte
    - **forces N** :
      - 50
      - 80
      - 100
      - 120
      - 150
      - 200
      - 250
    - **choix force** : Force requise = (poids porte en kg × 10) / nombre de vérins
    - **usage** : Abattants, coffres de rangement, lits coffres
  - **compas a ressort** :
    - **description** : Bras articulé avec ressort intégré
    - **types** :
      - lift (relevable)
      - fall (basculant avant)
    - **usage** : Meubles hauts cuisine, portes relevables
  - **aventos blum** :
    - **description** : Système relevable intégré Blum pour meubles hauts
    - **types** :
      - HK-XS (petit)
      - HF (bi-fold)
      - HL (parallèle)
      - HS (pivotant)
      - HK-TOP (standard)
    - **note** : Solution premium, nécessite calcul de force selon poids et dimensions



---

<!-- chunk_id: quincaillerie.coulisses_tiroir | source: corpus v3 de l'auteur -->

# Quincaillerie : Coulisses tiroir

- **description** : Systèmes de guidage pour tiroirs — choix critique pour l'usage quotidien
- **types** :
  - **a galets** :
    - **description** : Coulisses économiques à roulettes plastique
    - **charge max kg** :
      - **min** : 10
      - **max** : 25
    - **sortie** : partielle (75-80%)
    - **bruit** : moyen à élevé
    - **montage** : latéral ou sous tiroir
    - **prix** : économique
    - **usage** : Tiroirs légers, budget serré
  - **a billes sortie partielle** :
    - **description** : Coulisses à roulement à billes, sortie 75%
    - **charge max kg** :
      - **min** : 10
      - **max** : 25
    - **sortie** : partielle
    - **bruit** : silencieux
    - **montage** : latéral ou en rainure (17mm ou 27mm)
    - **prix** : moyen
    - **usage** : Usage courant, bon rapport qualité/prix
  - **a billes sortie totale** :
    - **description** : Coulisses télescopiques à billes, sortie 100%
    - **charge max kg** :
      - **min** : 25
      - **max** : 60
    - **sortie** : totale
    - **bruit** : silencieux
    - **montage** : latéral
    - **prix** : moyen-haut
    - **usage** : Tiroirs profonds, cuisine, rangement lourd
  - **a billes charge lourde** :
    - **description** : Coulisses renforcées pour charges importantes
    - **charge max kg** :
      - **min** : 45
      - **max** : 100
    - **sortie** : totale
    - **montage** : latéral
    - **prix** : élevé
    - **usage** : Outillage, classement, tiroirs très chargés
  - **systeme metal** :
    - **description** : Tiroirs métal intégrés (type Tandembox Blum, ArciTech Hettich, InnoTech)
    - **charge max kg** :
      - **min** : 30
      - **max** : 70
    - **sortie** : totale
    - **amortissement** : intégré
    - **note** : Tiroir métal complet avec parois — pas un simple guidage
    - **prix** : élevé
    - **usage** : Cuisine équipée, salle de bain, haut de gamme
- **cotes implantation** :
  - **jeu lateral par cote mm** :
    - **coulisses laterales a billes** : 12.7
    - **coulisses sous tiroir** : variable selon modèle
    - **tiroirs metal integres** : 0
    - **note** : 12.7mm (1/2 pouce) EXCLUSIVEMENT pour coulisses latérales à billes. Tandem/Movento/ArciTech ont des implantations spécifiques.
  - **jeu profondeur mm** :
    - **min** : 5
    - **max** : 10
  - **longueur tiroir** : profondeur_caisson - 5 à 10 mm de jeu
  - **position coulisse laterale** : bord avant à 2 mm de la face avant du caisson
  - **hauteur rainure mm** :
    - **types** :
      - 17
      - 27
    - **note** : Pour coulisses en rainure uniquement
- **construction tiroir bois** :
  - **epaisseur cotes mm** :
    - **standard** : 15
    - **alternatif** : 18
  - **epaisseur fond mm** :
    - **rainure** :
      - **min** : 4
      - **max** : 6
    - **rapporte** :
      - **min** : 8
      - **max** : 15
  - **fond rainure position mm** :
    - **note** : Rainure à 8-10 mm du bas des côtés, profondeur 5-6 mm
  - **facade rapportee** :
    - **description** : La façade du tiroir est une pièce séparée, fixée sur le caisson du tiroir après montage
    - **fixation** : Vis depuis l'intérieur du tiroir, ou vis excentriques
    - **jeu facade mm** :
      - **min** : 2
      - **max** : 3
      - **note** : Jeu par côté entre façade et caisson
- **longueurs disponibles mm** :
  - 250
  - 300
  - 350
  - 400
  - 450
  - 500
  - 550
  - 600
  - 650
  - 700
- **note choix longueur** : Choisir la longueur = profondeur du caisson - jeu (5-10mm). Ex: caisson 50cm → coulisse 450 ou 500mm



---

<!-- chunk_id: quincaillerie.ferrures_table_extensible | source: corpus v3 de l'auteur -->

# Quincaillerie : Ferrures table extensible

- **coulisses** :
  - **asynchrones** :
    - **description** : Chaque côté tiré séparément
  - **synchrones** :
    - **description** : Câble acier lie les deux côtés
    - **largeur rallonge mm** :
      - **standard** : 500
      - **confort** : 600
  - **mecanisme papillon** :
    - **description** : Rallonge portefeuille repliée sous le plateau
- **longueurs installees mm** :
  - 740
  - 900
  - 1200
- **charge max kg** :
  - **min** : 40
  - **max** : 60
- **alignement** :
  - tourillons
  - loquets de table
  - taquets de positionnement
- **regles** :
  - Épaisseur rallonge = épaisseur plateau
  - 500-600mm de rallonge ≈ +2 places
  - Verrouillage en position ouverte ET fermée



---

<!-- chunk_id: quincaillerie.fixation_murale | source: corpus v3 de l'auteur -->

# Quincaillerie : Fixation murale

- **description** : Quincaillerie pour fixer meubles et étagères au mur
- **chevilles par support** :
  - **beton plein** :
    - **cheville** : Expansion nylon ou métal
    - **diametre mm** :
      - **min** : 6
      - **max** : 10
    - **charge unitaire kg** :
      - **min** : 20
      - **max** : 80
  - **brique creuse** :
    - **cheville** : Cheville à expansion spéciale creux (type Molly, SX Fischer)
    - **diametre mm** :
      - **min** : 6
      - **max** : 10
    - **charge unitaire kg** :
      - **min** : 10
      - **max** : 40
    - **attention** : Ne jamais utiliser de cheville standard dans du creux
  - **placo BA13** :
    - **cheville** : Cheville Molly métallique ou cheville à bascule
    - **charge unitaire kg** :
      - **min** : 5
      - **max** : 25
    - **charge meuble lourd** : Fixer dans les montants de l'ossature (entraxe 40 ou 60cm)
    - **note** : Pour charges > 30kg : traverser le placo et fixer dans le montant
  - **ossature bois** :
    - **cheville** : Vis à bois directement dans le montant
    - **vis diametre mm** :
      - **min** : 5
      - **max** : 8
    - **longueur penetration mm** :
      - **min** : 40
      - **max** : 60
    - **charge unitaire kg** :
      - **min** : 30
      - **max** : 100
    - **note** : Détecter les montants avec un détecteur de montants
- **ferrures suspente** :
  - **equerre invisible** :
    - **description** : Équerres cachées derrière le meuble
    - **charge paire kg** :
      - **min** : 30
      - **max** : 60
  - **rail de suspension** :
    - **description** : Rail métallique horizontal fixé au mur, crochets réglables sur le meuble
    - **charge m lineaire kg** :
      - **min** : 40
      - **max** : 80
    - **reglages** : Hauteur et profondeur via vis de réglage sur le crochet
    - **usage** : Meubles hauts de cuisine, standard industriel
    - **marques** :
      - Hettich
      - Camar
      - Blum
  - **taquet francais** :
    - **description** : Deux liteaux biseautés à 45° qui s'emboîtent (french cleat)
    - **angle deg** : 45
    - **epaisseur liteau mm** :
      - **min** : 16
      - **max** : 22
    - **charge m lineaire kg** :
      - **min** : 30
      - **max** : 50
    - **usage** : Solution simple et robuste pour meubles lourds, étagères, panneaux d'outils
    - **note** : Facile à fabriquer soi-même à la scie circulaire
  - **equerre anti basculement** :
    - **description** : Sangle ou équerre reliant le haut du meuble au mur
    - **obligatoire** : Tout meuble > 150 cm de hauteur, surtout avec enfants
    - **types** :
      - Sangle textile + vis
      - Équerre métal L
      - Câble acier
    - **source** : règle de l'art du corpus (RT_001), pas une norme ; les fabricants de meubles fournissent en général un kit de fixation murale



---

<!-- chunk_id: quincaillerie.formulas | source: corpus v3 de l'auteur -->

# Quincaillerie : formules de calcul (charnières, coulisses, perçages)

## hinge_count
- **ID** : `F_QUI_001`
- **Variables** : door_height_mm
- **Formule** : `Math.max(2, Math.ceil((door_height_mm - 800) / 500) + 2)`
- **Sortie** : num_hinges
- **Note** : Vérifier le poids sur l'abaque fabricant si la porte dépasse 600 mm de large

## drawer_width_lateral_slides
- **ID** : `F_QUI_002`
- **Variables** : cabinet_inner_width_mm
- **Formule** : `cabinet_inner_width_mm - 25.4`
- **Sortie** : drawer_box_width_mm
- **Note** : 12.7mm per side. ONLY for lateral ball-bearing slides.

## drawer_length
- **ID** : `F_QUI_003`
- **Variables** : cabinet_inner_depth_mm, rear_gap_mm
- **Formule** : `cabinet_inner_depth_mm - rear_gap_mm`
- **Sortie** : drawer_box_length_mm
- **Paramètres** : - **rear gap mm** :
  - **min** : 5
  - **max** : 10
  - **default** : 8

## gas_strut_force
- **ID** : `F_QUI_004`
- **Variables** : lid_weight_kg, num_struts
- **Formule** : `(lid_weight_kg * 9.81) / num_struts`
- **Sortie** : force_per_strut_N
- **Note** : Round UP to next available model

## system_32_hole_positions
- **ID** : `F_QUI_005`
- **Variables** : row_offset_from_edge_mm, start_y_mm, hole_index
- **Formule** : `{'x_mm': 'row_offset_from_edge_mm', 'y_mm': 'start_y_mm + hole_index * 32'}`
- **Sortie** : {'x_mm': 'horizontal position', 'y_mm': 'vertical position'}
- **Paramètres** : - **row offset from edge mm** :
  - **default** : 37

## gap_between_twin_doors
- **ID** : `F_QUI_006`
- **Variables** : divider_thickness_mm, gap_between_doors_mm
- **Formule** : `(divider_thickness_mm - gap_between_doors_mm) / 2`
- **Sortie** : overlay_per_door_mm
- **Paramètres** : - **gap between doors mm** :
  - **min** : 2
  - **max** : 3
  - **default** : 3

## hinge_cup_center
- **ID** : `F_QUI_007`
- **Variables** : K_mm
- **Formule** : `17.5 + K_mm`
- **Sortie** : cup_center_from_edge_mm
- **Paramètres** : - **K mm** :
  - **min** : 3
  - **max** : 7
  - **default** : 4

## door_weight
- **ID** : `F_QUI_008`
- **Variables** : height_mm, width_mm, thickness_mm, density_kg_m3
- **Formule** : `(height_mm * width_mm * thickness_mm * density_kg_m3) / 1000000000`
- **Sortie** : weight_kg
- **Paramètres** : - **density kg m3** :
  - **particleboard** : 650
  - **mdf** : 750
  - **plywood** : 550
  - **glass** : 2500

## handle_screw_length
- **ID** : `F_QUI_009`
- **Variables** : panel_thickness_mm, handle_base_mm, thread_engagement_mm
- **Formule** : `panel_thickness_mm + handle_base_mm + thread_engagement_mm`
- **Sortie** : screw_length_mm
- **Paramètres** : - **thread engagement mm** :
  - **min** : 8
  - **max** : 12
  - **default** : 10

## edge_band_width
- **ID** : `F_QUI_010`
- **Variables** : panel_thickness_mm, trimming_surplus_mm
- **Formule** : `panel_thickness_mm + trimming_surplus_mm`
- **Sortie** : band_width_mm
- **Paramètres** : - **trimming surplus mm** :
  - **min** : 2
  - **max** : 4
  - **default** : 3



---

<!-- chunk_id: quincaillerie.pieds_et_plinthes | source: corpus v3 de l'auteur -->

# Quincaillerie : Pieds et plinthes

- **pieds reglables** :
  - **description** : Pieds à vis pour réglage de niveau du caisson
  - **hauteurs mm** :
    - 100
    - 120
    - 150
    - 200
  - **reglage mm** :
    - **min** : 10
    - **max** : 30
  - **charge par pied kg** :
    - **min** : 50
    - **max** : 150
  - **diametre percage mm** : 10
  - **position** : Retrait de 30-50mm par rapport aux chants avant et latéraux
  - **nombre** : 4 pieds minimum, ajouter pieds intermédiaires au-delà de 80cm de largeur
- **plinthe** :
  - **hauteur standard mm** :
    - **min** : 80
    - **max** : 150
    - **cuisine** : 100
  - **retrait mm** :
    - **min** : 30
    - **max** : 50
  - **fixation** : Clips à encliqueter sur les pieds réglables



---

<!-- chunk_id: quincaillerie.poids_max_porte | source: corpus v3 de l'auteur -->

# Quincaillerie : Poids max porte

- **source** : Abaques Blum et Hettich
- **pour largeur max mm** : 600
- **configurations** :
  - nb charnieres: 2 · hauteur max mm: 900 · poids max kg: 8
  - nb charnieres: 3 · hauteur max mm: 1600 · poids max kg: 13
  - nb charnieres: 4 · hauteur max mm: 2000 · poids max kg: 17
  - nb charnieres: 5 · hauteur max mm: 2400 · poids max kg: 22
- **note** : Porte large (ratio largeur/hauteur inversé) → ajouter 1 charnière supplémentaire



---

<!-- chunk_id: quincaillerie.poignees_et_boutons | source: corpus v3 de l'auteur -->

# Quincaillerie : Poignees et boutons

- **entraxes standard mm** :
  - 32
  - 64
  - 96
  - 128
  - 160
  - 192
  - 224
  - 256
  - 288
  - 320
- **entraxe note** : Multiples de 32mm (système 32)
- **percage diametre mm** :
  - **min** : 4
  - **max** : 5
- **vis fixation** :
  - **filetage** : M4
  - **longueur mm** : épaisseur panneau + 4-5mm (ex: 22mm pour panneau 18mm)
- **boutons un trou** :
  - **note** : Prévoir pion anti-rotation si modèle lourd



---

<!-- chunk_id: quincaillerie.portes_pose | source: corpus v3 de l'auteur -->

# Portes battantes : 4 types de pose (enveloppante, demi-recouvrement, appliquée, affleurante)

4 types de pose pour les portes battantes. Le choix conditionne la dimension de la porte ET le type de charnière (coudure).

## 1. Pose enveloppante (recouvrement total)
- **Description** : la porte recouvre entièrement le chant de la joue.
- **Jeu** : 2 mm entre portes adjacentes.
- **Largeur porte** = largeur intérieure + 2× épaisseur joue − 2 mm de jeu.
- **Hauteur porte** = hauteur ouverture + 2× épaisseur tablettes − 2 mm.
- **Charnière** : coudure 0 mm.
- **Usage** : standard. Aspect simple et propre, pardonne les défauts d'équerrage.

## 2. Pose demi-recouvrement
- **Description** : la porte recouvre la moitié du chant de la joue (pour 2 portes sur même joue).
- **Jeu** : 2 mm entre portes.
- **Largeur porte** = largeur intérieure / 2 + épaisseur joue / 2 − 1 mm.
- **Charnière** : coudure de demi-épaisseur de la joue.
- **Usage** : meuble à 2 portes adjacentes partageant la même joue centrale.

## 3. Pose appliquée
- **Description** : la porte est posée DEVANT le meuble, sans encastrement.
- **Jeu** : 3-5 mm en périphérie.
- **Largeur porte** = largeur ouverture + 10-15 mm de chaque côté.
- **Charnière** : apparente ou invisible.
- **Usage** : solution simple, aspect rustique. Moins de finition.

## 4. Pose affleurante (intérieure)
- **Description** : la porte affleure le chant de la joue, s'insère dans le cadre.
- **Jeu** : 2 mm tout autour.
- **Largeur porte** = largeur intérieure − 4 mm.
- **Hauteur porte** = hauteur ouverture − 4 mm.
- **Charnière** : coudure complète (= épaisseur joue).
- **Usage** : pose la plus élégante. Visible au moindre défaut d'équerrage — exige précision.

## Règles communes
- Largeur max porte battante panneau 18 mm : **60 cm** (au-delà, voile).
- Largeur max panneau 19 mm : **65 cm**.
- Si > 60 cm → renfort par traverse intermédiaire ou cadre collé au dos.
- Toujours prévoir 2 mm de jeu entre portes ET en haut/bas. Sans jeu : frottement. Trop de jeu : aspect négligé.



---

<!-- chunk_id: quincaillerie.quincaillerie_lit | source: corpus v3 de l'auteur -->

# Quincaillerie : Quincaillerie lit

- **pieds** :
  - **hauteurs mm** :
    - 50
    - 80
    - 100
    - 120
    - 150
    - 200
  - **filetage** :
    - M8
    - M10
  - **charge par pied kg** :
    - **min** : 50
    - **max** : 150
- **ferrures assemblage** :
  - **crochets encastres** :
    - **description** : Mâle/femelle à crochet, démontage rapide
    - **hauteur platine mm** :
      - **min** : 90
      - **max** : 150
  - **boulons de lit** :
    - **diametre mm** :
      - 6
      - 8
    - **longueur mm** :
      - 80
      - 100
      - 120
      - 140
  - **equerres renfort** :
    - **ailes mm** :
      - 40x40
      - 50x50
      - 60x60
- **lit coffre** :
  - **poids cadre sommier matelas kg** :
    - 40
    - 50
    - 60
    - 80
  - **verins associes N** :
    - 400
    - 500
    - 600
    - 800
  - **regle** : Choix vérin = poids cadre + sommier + matelas (pas seulement le bois)



---

<!-- chunk_id: quincaillerie.regles_de_choix | source: corpus v3 de l'auteur -->

# Quincaillerie : règles de choix (matrice de décision)

### Q_001 — charnieres
Privilégier Ø35mm pour la majorité des portes bois 15-24mm. Ø26mm reste pertinent pour petites portes légères ou applications spécifiques.

### Q_002 — coulisses
Coulisse à billes sortie totale pour tout tiroir de profondeur > 40cm

### Q_003 — general
Amortissement intégré systématique sur charnières et coulisses — confort majeur pour petit surcoût

### Q_004 — vis
Pré-percer TOUJOURS dans les panneaux dérivés (particules, MDF, mélaminé) — risque d'éclatement sinon

### Q_005 — fixation
Vérifier le type de mur AVANT de choisir les chevilles — un meuble qui tombe est un danger mortel

### Q_006 — coulisses
Pour coulisses latérales à billes télescopiques : largeur tiroir = largeur intérieure - 25.4mm. Non valable pour coulisses à galets, sous tiroir ou tiroirs métal.

### Q_007 — charnieres
Embase charnière toujours à 37mm du chant avant du caisson (système 32)

### Q_008 — securite
Anti-basculement OBLIGATOIRE pour tout meuble > 150cm non fixé au mur par sa structure



---

<!-- chunk_id: quincaillerie.serrures_et_verrous | source: corpus v3 de l'auteur -->

# Quincaillerie : Serrures et verrous

- **serrure a came** :
  - **description** : Serrure batteuse classique, came rotative verrouillant la façade
  - **diametre percage cylindre mm** :
    - **courants** :
      - 16
      - 18
      - 19
      - 22
    - **plus courant** : 19
  - **longueur fut mm** :
    - 16
    - 20
    - 25
    - 30
  - **distance axe chant min mm** : 20
  - **rotation deg** :
    - 90
    - 180
  - **came types** :
    - droite
    - déportée
    - crochet
    - tiroir
  - **usage** :
    - porte battante
    - tiroir
    - trappe
- **serrure en applique** :
  - **description** : Boîtier vissé sur la face interne
  - **diametre cylindre mm** :
    - 18
    - 22
  - **usage** :
    - meubles traditionnels
    - caissons bois massif
- **serrure push lock** :
  - **description** : Bouton poussoir pour façade sans poignée
  - **diametre percage mm** :
    - **courant** : 19
    - **alternatifs** :
      - 20
      - 22
      - 26
  - **epaisseur panneau mm** :
    - **min** : 12
    - **max** : 27
  - **usage** :
    - van
    - meuble mobile
    - façade sans poignée
- **espagnolette rotative** :
  - **description** : Serrure à tringles pour armoires hautes (verrouillage 3 points)
  - **diametre cylindre mm** : 15
  - **usage** : Obligatoire sur portes > 1500mm pour éviter le voilage
- **verrous sans cle** :
  - **loqueteau a bille** :
    - **diametre bille mm** :
      - **min** : 6
      - **max** : 10
    - **force N** :
      - **min** : 5
      - **max** : 20
  - **loqueteau magnetique** :
    - **force N** :
      - **min** : 10
      - **max** : 40
    - **jeu porte mm** :
      - **min** : 1
      - **max** : 3
  - **targette** :
    - **longueur mm** :
      - **min** : 40
      - **max** : 80



---

<!-- chunk_id: quincaillerie.systemes_push_to_open | source: corpus v3 de l'auteur -->

# Quincaillerie : Systemes push to open

- **noms commerciaux** :
  - Tip-On (Blum)
  - Push to open (Hettich)
- **principe** : Doigt mécanique à ressort, supprime le besoin de poignée
- **variantes** :
  - **courte** :
    - **usage** : Portes < 1300mm
    - **course ejection mm** : 17
  - **longue** :
    - **usage** : Portes > 1300mm
    - **course ejection mm** : 38
- **jeu declenchement mm** :
  - **min** : 1.5
  - **max** : 3
  - **note** : Espace vital entre façade et caisson au repos
- **types embouts** :
  - **aimante** : Pour charnières SANS ressort de rappel + plaque métallique sur façade
  - **tampon** : Pour charnières avec ressort inversé



---

<!-- chunk_id: quincaillerie.taquets_etagere | source: corpus v3 de l'auteur -->

# Quincaillerie : Taquets etagere

- **description** : Supports pour tablettes réglables dans un caisson
- **types** :
  - **taquet a enfoncer** :
    - **description** : Tige métallique ou plastique enfoncée dans un trou borgne
    - **diametres mm** :
      - 3
      - 4
      - 5
      - 6
      - 7
    - **diametre courant mm** : 5
    - **charge par taquet kg** :
      - **min** : 15
      - **max** : 60
      - **note** : Selon diamètre et matériau
    - **profondeur percage mm** :
      - **min** : 8
      - **max** : 12
  - **taquet equerre a visser** :
    - **description** : Petite équerre en plastique avec vis de fixation et cache
    - **vis diametre mm** : 4
    - **usage** : Tablettes lourdes, assemblage rapide
    - **charge par taquet kg** :
      - **min** : 20
      - **max** : 75
  - **taquet cremaillere** :
    - **description** : S'insère dans une crémaillère métallique encastrée ou en applique
    - **espacement fentes mm** : 32
    - **usage** : Grande modularité, repositionnement fréquent
  - **taquet ventouse verre** :
    - **description** : Avec ventouse ou patin caoutchouc pour tablettes en verre
    - **diametre tenon mm** : 5
    - **epaisseur verre mm** :
      - **min** : 5
      - **max** : 10
- **percage systeme 32** :
  - **description** : Rangée de trous espacés de 32mm dans les joues du caisson
  - **entraxe mm** : 32
  - **distance axe chant avant mm** : 37
  - **diametre percage mm** : 5
  - **profondeur percage mm** :
    - **min** : 10
    - **max** : 13
  - **premiere ligne depuis bord mm** : 37
  - **note** : Commencer le premier trou à 37mm du chant, puis tous les 32mm. Percer les 4 coins du caisson de manière symétrique.
- **nombre taquets par tablette** : 4
- **regle placement** : Un taquet à chaque angle de la tablette, dans les trous correspondants des 2 joues



---

<!-- chunk_id: quincaillerie.tiroirs_synthese | source: corpus v3 de l'auteur -->

# Tiroirs : synthèse coulisses (galets / billes / invisibles) + dimensionnement

Synthèse coulisses + dimensionnement caisson tiroir.

## Types de coulisses

### Coulisses à galets (économiques)
- Ouverture **partielle** (~75%)
- Charge max : 15-25 kg
- Fixation latérale
- Jeu latéral : **12.5 mm de chaque côté**
- Largeur tiroir = ouverture intérieure − 25 mm

### Coulisses à billes (sortie totale)
- Ouverture **totale** (100%)
- Charge max : 30-50 kg
- Fixation latérale
- Jeu latéral : **12.5 mm de chaque côté**
- Soft-close (fermeture amortie) disponible
- Marques : Blum Tandembox, Hettich KA 1730, Accuride

### Coulisses invisibles (sous tiroir)
- Fixées **sous le fond** du tiroir
- Pas visibles depuis le côté
- Ouverture totale, charge max 30-40 kg
- Jeu latéral : **3 mm de chaque côté seulement**
- Nécessite fond rigide ≥ 16 mm
- Marques : Blum Movento, Hettich Quadro V6+

## Dimensionnement caisson tiroir
- **Hauteur caisson** = hauteur façade − 25 mm (jeu coulisse)
- **Profondeur caisson** = profondeur intérieure meuble − 10 mm (recul arrière)
- **Fond** : HDF 3 mm rainuré à 8 mm du bas

## Dimensionnement façade
- **Hauteur façade** = hauteur d'ouverture − 3 mm (jeu haut + bas)
- **Largeur façade** : identique aux portes selon pose (recouvrement / demi / affleurante)
- **Fixation** : 4 vis depuis l'intérieur du caisson tiroir, en retrait de 3 cm

## Choix
- **Cuisine** : billes ou invisibles (charge + confort).
- **Rangement léger / budget serré** : galets.
- **Design haut de gamme / affleurant** : invisibles.



