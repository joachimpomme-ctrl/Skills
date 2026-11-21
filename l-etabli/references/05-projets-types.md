# 05-projets-types

<!-- Corpus menuiserie v3.1.0 — catégorie 05-projets-types -->

## Sommaire du fichier
- `projet.armoire` — 🗄️ Projet type : Armoire
- `projet.banquette_coffre` — 🪑 Projet type : Banquette / Coffre d'entrée
- `projet.bibliotheque` — 📚 Projet type : Bibliothèque
- `projet.buffet` — 🍽️ Projet type : Buffet / Enfilade
- `projet.bureau` — 💻 Projet type : Bureau
- `projet.cave_vin` — 🍷 Projet type : Cave à vin / Casier bouteilles
- `projet.commode` — 🗃️ Projet type : Commode / Chiffonnier
- `projet.cuisine` — 🍳 Projet type : Cuisine
- `projet.etagere_murale` — 🪵 Projet type : Étagère murale
- `projet.lit_cabane_mezzanine` — 🏠 Projet type : Lit cabane / Mezzanine enfant
- `projet.meuble_chaussures` — 👟 Projet type : Meuble à chaussures
- `projet.meuble_salle_de_bain` — 🚿 Projet type : Meuble salle de bain
- `projet.meuble_tv` — 📺 Projet type : Meuble TV
- `projet.placard` — 🚪 Projet type : Placard / Dressing
- `projet.sous_escalier` — 🪜 Projet type : Meuble sous-escalier
- `projet.table` — 🪵 Projet type : Table sur mesure
- `projet.templates_defaut` — Templates par défaut : 9 types de meubles (valeurs de démarrage)
- `projet.vestiaire_entree` — 🧥 Projet type : Vestiaire d'entrée

---

<!-- chunk_id: projet.armoire | source: corpus v3 de l'auteur -->

# 🗄️ Projet type : Armoire

**Description** : Meuble fermé de grande hauteur, rangement mixte


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous
- fond
- porte

## Composants optionnels
- tablette_fixe
- tablette_reglable
- separateur
- tiroir
- tringle
- plinthe

## Dimensions par défaut
- **hauteur mm** : 2000
- **largeur mm** : 1000
- **profondeur mm** : 550
- **epaisseur panneau mm** : 18
- **nb portes** : 2

## Règles de génération
- **portes 2** :
  - **type** : applique
  - **largeur** : F_CON_002
  - **hauteur** : F_CON_008
  - **charniere** : demi-recouvrement si séparateur central, applique sinon
- **interieur type** :
  - **zone haute** :
    - **tringle** : oui
    - **hauteur mm** : 1100
  - **zone basse** :
    - **tablettes** : 2
    - **ou tiroirs** : 2

## Contraintes
- regle: Hauteur > 200cm → transport difficile · action: Proposer caisson haut séparé
- regle: Poids porte > limite charnières · action: Calculer poids, ajuster nb charnières
- regle: Anti-basculement obligatoire · action: Toujours alerter
- regle: Porte MDF 18mm, H200cm, L50cm ≈ 13kg · action: Vérifier abaque charnières
- regle: Hauteur > 210 cm en monobloc · action: Alerter transport et montage

## Variantes
- nom: Armoire lingère · tablettes: oui · tringle: non
- nom: Armoire bonnetière · porte unique: oui · largeur etroite: oui

## Pièges courants
- Armoire non fixée au mur = danger basculement (surtout enfants)
- Portes lourdes → 4-5 charnières obligatoires
- Transport en un seul bloc quasi impossible au-delà de 210cm → prévoir démontable
- Porte pleine sur toute la hauteur sans espagnolette → voilage garanti
- Large porte unique trop lourde et qui voile
- Meuble haut monté loin du mur puis impossible à redresser au plafond



---

<!-- chunk_id: projet.banquette_coffre | source: corpus v3 de l'auteur -->

# 🪑 Projet type : Banquette / Coffre d'entrée

**Description** : Assise avec rangement intégré pour l'entrée ou le pied de lit


## Composants obligatoires
- joue_gauche
- joue_droite
- assise
- dessous
- fond

## Composants optionnels
- dossier
- accoudoir
- separateur
- coussin
- tiroir
- porte

## Dimensions par défaut
- **hauteur assise mm** : 450
- **largeur mm** : 1200
- **profondeur mm** : 450
- **epaisseur mm** : 18
- **coffre hauteur utile mm** : 280

## Règles de génération
- **coffre ouverture dessus** :
  - **assise** : Plateau articulé par charnière piano ou compas
  - **verin** : Vérin à gaz pour maintien en position ouverte
  - **force verin N** : poids_assise_kg × 10 / nb_verins
- **coffre ouverture frontale** :
  - **type** : tiroirs ou porte en façade
  - **note** : Conserver traverse basse reculée pour les pieds

## Contraintes
- regle: Hauteur assise 42-48cm finie (avec coussin) · action: Ajuster structure
- regle: Profondeur > 50cm sans dossier → inconfortable · action: Alerter
- regle: Ouverture dessus : vérifier recul mur/dossier pour débattement · action: Calculer
- regle: Aération coffre si rangement textile · action: Proposer trous ventilation

## Pièges courants
- Oublier les vérins → le couvercle retombe sur les doigts
- Assise trop profonde sans dossier → on glisse
- Pas d'aération → odeur de renfermé dans le coffre



---

<!-- chunk_id: projet.bibliotheque | source: corpus v3 de l'auteur -->

# 📚 Projet type : Bibliothèque

**Description** : Meuble de rangement ouvert pour livres, objets déco, médias


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous
- fond

## Composants optionnels
- tablette_fixe
- tablette_reglable
- separateur
- porte
- tiroir
- bandeau
- plinthe

## Dimensions par défaut
- **hauteur mm** : 2000
- **largeur mm** : 800
- **profondeur mm** : 300
- **epaisseur panneau mm** : 18
- **nb tablettes reglables** : 4

## Règles de génération
- **joues** :
  - **longueur** : hauteur_meuble - (si plinthe : hauteur_plinthe)
  - **largeur** : profondeur_meuble
- **dessus dessous** :
  - **longueur** : largeur_meuble - (2 × epaisseur_panneau)
  - **largeur** : profondeur_meuble
  - **note** : Si joues prioritaires (forme 1)
- **tablettes fixes** :
  - **longueur** : largeur_interieure
  - **largeur** : profondeur - epaisseur_fond
  - **position** : Une en haut (sous le dessus) et une en bas (sur le dessous) minimum
- **tablettes reglables** :
  - **longueur** : largeur_interieure - 2mm
  - **largeur** : profondeur - epaisseur_fond - 2mm
  - **espacement defaut** : réparti régulièrement entre tablettes fixes
- **fond** :
  - **longueur** : hauteur_meuble - (si rainure : 2 × profondeur_rainure)
  - **largeur** : largeur_meuble - (si rainure : 2 × profondeur_rainure)
  - **epaisseur mm** : 5
  - **type** : rainure

## Quincaillerie associée
- **sans porte** :
  - taquets Ø5mm (4 par tablette réglable)
  - vis assemblage ou tourillons Ø8mm
- **avec portes** :
  - + charnières Ø35mm applique 110°
  - + poignées (entraxe selon choix)
- **fixation murale** : Anti-basculement obligatoire si H > 150cm

## Contraintes
- regle: Portée tablette chargée livres (25 kg/m) ≤ ~83cm (CP bouleau 18mm), ~42cm (MDF), ~38cm (mélaminé) — calcul exact via scripts/calc.py · action: Proposer séparateur vertical
- regle: Hauteur > 150cm · action: Alerter anti-basculement obligatoire
- regle: Profondeur < 20cm · action: Alerter stabilité insuffisante sans fixation murale
- regle: Largeur > 120cm · action: Proposer séparateur central pour éviter fléchissement
- regle: Profondeur > 35 cm sur meuble haut non fixé · action: Alerter poids et risque basculement avec tiroirs/portes
- regle: Présence de bacs enfants en partie basse · action: Alerter sur pincement doigts et stabilité

## Variantes
- nom: Bibliothèque ouverte · portes: non · tiroirs: non
- nom: Bibliothèque avec portes basses · portes position: bas · tablette separation: oui
- nom: Bibliothèque vitrée · portes: oui · vitrage: oui
- nom: Bibliothèque asymétrique · separateur: oui · largeurs differentes: oui
- nom: Bibliothèque enfant · hauteur mm: 1200 · profondeur mm: 280 · niches bacs: oui
- nom: Bibliothèque pont · modules lateraux: oui · module haut pont: oui
- nom: Bibliothèque suspendue · fixation murale: oui

## Pièges courants
- Sous-estimer le poids des livres → vérifier portée tablettes
- Oublier l'anti-basculement → danger mortel avec enfants
- Fond trop fin (3mm) sur grande largeur → meuble qui se déforme
- Ne pas prévoir assez de trous système 32 → tablettes non repositionnables
- Ne pas vérifier la hauteur sous plafond avec corniche ou surmeuble
- Tablettes réglables seules sur grande largeur : manque de rigidité globale



---

<!-- chunk_id: projet.buffet | source: corpus v3 de l'auteur -->

# 🍽️ Projet type : Buffet / Enfilade

**Description** : Meuble bas long pour salle à manger, vaisselle, rangement


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous
- fond

## Composants optionnels
- separateur
- tablette_fixe
- tablette_reglable
- porte
- tiroir
- plinthe

## Dimensions par défaut
- **hauteur mm** : 850
- **largeur mm** : 1800
- **profondeur mm** : 450
- **epaisseur panneau mm** : 18
- **nb compartiments** : 3

## Règles de génération
- **structure** : 2 séparateurs → 3 compartiments égaux
- **par compartiment** :
  - **porte** : applique
  - **tablette reglable** : 1
- **tiroir option** : 1 tiroir haut sur toute la largeur (couverts, nappes)

## Contraintes
- regle: Largeur > 120cm sans séparateur → dessus fléchit · action: Imposer séparateur
- regle: Largeur totale > 200cm → transport · action: Proposer 2 caissons juxtaposés
- regle: Charge dessus (TV, déco) → épaisseur plateau · action: Recommander 25mm si charge > 30kg
- regle: Largeur > 180 cm · action: Proposer deux caissons juxtaposés
- regle: Dessus utilisé comme plan de service très chargé · action: Proposer plateau 25 mm ou renfort

## Variantes
- nom: Enfilade portes + tiroirs hauts · tiroirs hauts: oui
- nom: Buffet vitré haut/bas · partie haute vitree: oui

## Pièges courants
- Dessus trop fin sur grande longueur → fléchit sous son propre poids
- Oublier les séparateurs → meuble instable latéralement
- Profondeur 45cm avec portes épaisses (22mm) → profondeur utile réduite à 35cm
- Long meuble assemblé sans vrai fond : il vrille à la manutention



---

<!-- chunk_id: projet.bureau | source: corpus v3 de l'auteur -->

# 💻 Projet type : Bureau

**Description** : Poste de travail avec plateau, rangements, passage de câbles


## Composants obligatoires
- plateau
- joue_gauche
- joue_droite

## Composants optionnels
- fond
- tablette_fixe
- tiroir
- porte
- passe_cables
- tablette_clavier
- separateur
- bandeau_pudeur

## Dimensions par défaut
- **hauteur plateau mm** : 750
- **largeur mm** : 1400
- **profondeur mm** : 700
- **epaisseur plateau mm** : 25
- **epaisseur panneau mm** : 18

## Règles de génération
- **plateau** :
  - **longueur** : largeur_bureau
  - **largeur** : profondeur_bureau
- **joues** :
  - **longueur** : hauteur_plateau - epaisseur_plateau
  - **largeur** : profondeur - debord_avant (30mm)
  - **note** : Joues en retrait par rapport au plateau pour le confort des jambes
- **bandeau pudeur** :
  - **longueur** : largeur_interieure
  - **hauteur mm** :
    - **min** : 300
    - **max** : 400
  - **position** : Arrière du bureau, fixé entre les joues
  - **note** : Cache les câbles et les jambes côté visiteur
- **caisson tiroirs** :
  - **position** : Un côté (gauche ou droite), sous le plateau
  - **largeur mm** :
    - **min** : 400
    - **max** : 500
  - **hauteur libre jambes mm** :
    - **min** : 650
    - **note** : Espace libre sous plateau côté sans caisson
  - **tiroirs** :
    - type: petit · h facade mm: 120 · usage: fournitures
    - type: moyen · h facade mm: 180 · usage: dossiers A4
    - type: grand · h facade mm: 300 · usage: dossiers suspendus

## Quincaillerie associée
- **structure** :
  - Excentriques ou vis confirmation pour assemblage plateau/joues
  - Tourillons Ø8mm pour alignement
- **tiroirs** :
  - Coulisses à billes sortie totale
- **plateau** :
  - Passe-câbles Ø60 ou Ø80mm (perçage scie cloche)
- **fixation** : Anti-basculement si caisson haut ajouté

## Contraintes
- regle: Hauteur libre sous plateau ≥ 65cm (PMR : ≥ 70cm) · action: Alerter
- regle: Profondeur ≥ 60cm pour usage écran · action: Alerter si < 60cm
- regle: Débord plateau avant ≥ 20mm · action: Suggérer 30mm pour confort
- regle: Largeur ≥ 140cm pour double écran · action: Informer
- regle: Portée plateau > 140 cm sans ceinture ni piètement central · action: Alerter fléchissement
- regle: Bureau enfant · action: Proposer angles adoucis et hauteur adaptée

## Variantes
- nom: Bureau simple (plateau sur tréteaux) · caisson: non · fond: non
- nom: Bureau avec caisson tiroirs · caisson: droite · tiroirs: 3
- nom: Bureau en L · retour: oui · largeur retour mm: 1000
- nom: Bureau mural rabattable · fixation: charnière piano + compas · profondeur mm: 450
- 
  - **nom** : Bureau assis-debout
  - **hauteur mm** :
    - **min** : 650
    - **max** : 1250
- nom: Bureau caisson suspendu · caisson suspendu: oui
- nom: Bureau niche imprimante · niche technique: oui

## Pièges courants
- Oublier le passe-câbles → percer après montage est risqué
- Plateau trop fin (18mm sur 140cm) → fléchissement garanti sans traverse de renfort
- Caisson tiroirs des deux côtés = aucune place pour les jambes
- Hauteur standard 72cm inadaptée si utilisateur < 165cm ou > 185cm → prévoir réglable
- Plateau trop profond ou trop peu profond selon l'usage écran/clavier
- Passe-câbles oubliés sur un bureau adossé au mur



---

<!-- chunk_id: projet.cave_vin | source: corpus v3 de l'auteur -->

# 🍷 Projet type : Cave à vin / Casier bouteilles

**Description** : Rangement pour bouteilles de vin, horizontal ou incliné


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous

## Composants optionnels
- separateur
- tablette
- croisillons
- fond
- porte_vitree

## Dimensions par défaut
- **hauteur mm** : 1200
- **largeur mm** : 600
- **profondeur mm** : 350
- **type** : casier_losange

## Règles de génération
- **dimensions bouteille standard** :
  - **bordeaux** :
    - **diametre mm** : 75
    - **longueur mm** : 300
  - **bourgogne** :
    - **diametre mm** : 80
    - **longueur mm** : 310
  - **champagne magnum** :
    - **diametre mm** : 90
    - **longueur mm** : 330
- **alvéole unitaire mm** :
  - **largeur** :
    - **min** : 85
    - **standard** : 100
  - **hauteur** :
    - **min** : 85
    - **standard** : 100
  - **profondeur** :
    - **min** : 320
    - **standard** : 340
- **types casier** :
  - **losange croisillon** :
    - **description** : Grille en X formant des losanges — le plus classique
    - **materiau croisillon mm** :
      - **largeur** : 18
      - **epaisseur** : 10
    - **assemblage** : Mi-bois au centre, collé
  - **etageres horizontales** :
    - **espacement mm** : 100
    - **profondeur mm** : 340
    - **note** : Plus simple à fabriquer, accès facile aux bouteilles
  - **tubes ou cylindres** :
    - **diametre interieur mm** : 90
    - **note** : Tubes PVC, terre cuite ou béton — achetés, pas fabriqués
- **inclinaison** :
  - **horizontale pure** : Bouchon liège en contact avec le vin — position idéale
  - **legere inclinaison deg** :
    - **min** : 3
    - **max** : 5
  - **note** : Légère pente bouchon vers le bas pour maintenir le contact liège/vin

## Contraintes
- regle: Profondeur ≥ 32cm (bouteille standard 30cm + marge) · action: Alerter
- regle: Stockage horizontal obligatoire pour vins à bouchon liège · action: Informer
- regle: Poids : 1 bouteille ≈ 1.3kg → 50 bouteilles ≈ 65kg · action: Vérifier structure
- regle: Vibrations à éviter (pas contre machine à laver) · action: Informer
- regle: Si meuble haut chargé de bouteilles → fixation murale obligatoire · action: Imposer

## Pièges courants
- Alvéoles trop étroites pour bouteilles de Bourgogne (plus larges que Bordeaux)
- Profondeur insuffisante → bouteilles qui dépassent
- Matériau qui transmet les odeurs (certains résineux) → CP bouleau ou chêne préféré
- Poids total sous-estimé → effondrement de la structure



---

<!-- chunk_id: projet.commode | source: corpus v3 de l'auteur -->

# 🗃️ Projet type : Commode / Chiffonnier

**Description** : Meuble à tiroirs pour chambre, rangement linge


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous
- fond
- tiroir

## Composants optionnels
- separateur
- tablette_fixe
- plinthe

## Dimensions par défaut
- **hauteur mm** : 900
- **largeur mm** : 1000
- **profondeur mm** : 500
- **nb tiroirs** : 4
- **epaisseur mm** : 18

## Règles de génération
- **tiroirs** :
  - **repartition** : Tiroirs multiples empilés (domaine 3)
  - **type defaut** : progressive (plus hauts en bas)
  - **facades** : rapportées
  - **pas progression mm** : 32

## Contraintes
- regle: Anti-basculement obligatoire (plusieurs tiroirs ouverts = levier) · action: Toujours alerter
- regle: Largeur tiroir > 80cm → coulisses renforcées · action: Alerter
- regle: Poids total tiroirs pleins · action: Vérifier charge coulisses
- regle: Plus de 4 tiroirs hauts et étroits · action: Renforcer contrainte anti-basculement

## Variantes
- nom: Chiffonnier étroit · largeur mm: 600 · nb tiroirs: 6
- nom: Commode mixte tiroirs + porte · zone porte: oui

## Pièges courants
- Commode non fixée au mur + enfant qui grimpe = basculement mortel
- Tiroirs tous ouverts simultanément → centre de gravité bascule
- Fond de tiroir trop fin → claque au rangement, effet cheap
- Jeux de façades mal répartis, aspect irrégulier très visible
- Fond rapporté trop fin sur grand meuble à tiroirs



---

<!-- chunk_id: projet.cuisine | source: corpus v3 de l'auteur -->

# 🍳 Projet type : Cuisine

**Description** : Meubles bas, hauts et colonnes de cuisine


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous
- fond
- plinthe

## Composants optionnels
- tablette_fixe
- tablette_reglable
- porte
- tiroir
- fileur
- joue_habillage
- corniche
- bandeau

## Dimensions par défaut
- **meuble bas** :
  - **hauteur caisson mm** : 720
  - **profondeur mm** : 560
  - **largeurs modules mm** :
    - 300
    - 400
    - 450
    - 600
    - 800
    - 900
    - 1200
  - **plinthe mm** : 100
  - **plan de travail mm** :
    - **hauteur totale** : 900
    - **epaisseur** : 30
    - **profondeur** : 600
    - **debord avant mm** : 200
- **meuble haut** :
  - **hauteur caisson mm** : 720
  - **profondeur mm** : 330
  - **largeurs modules mm** :
    - 300
    - 400
    - 450
    - 600
    - 800
    - 900
  - **distance plan travail mm** : 550
- **colonne** :
  - **hauteur mm** : 2200
  - **profondeur mm** : 560
  - **largeurs mm** :
    - 600

## Règles de génération
- **meuble bas** :
  - **joues** :
    - **longueur mm** : 720
    - **largeur** : profondeur caisson
  - **dessus dessous** :
    - **longueur** : largeur - 2×épaisseur
    - **largeur** : profondeur
  - **fond** :
    - **retrait mm** : 15
    - **note** : Décollé du mur pour rail de suspension
  - **portes ou tiroirs** : Selon choix utilisateur, calcul F_CON_001/002
- **meuble haut** :
  - **fond** :
    - **retrait mm** : 15
    - **note** : Espace pour rail de suspension
  - **suspension** : Boîtiers dans joues supérieures + rail mural

## Quincaillerie associée
- **meuble bas** :
  - Pieds réglables H100mm
  - Clips plinthe
  - Charnières 110° avec amortisseur
  - Coulisses sortie totale 45kg
- **meuble haut** :
  - Rail de suspension
  - Boîtiers de suspension (65kg/pièce)
  - Charnières 110° amortisseur
- **generale** :
  - Vis de liaison inter-caissons Ø7mm
  - Fileurs d'angle
  - Joints plan de travail

## Contraintes
- regle: Plan de travail hauteur 90-95cm · action: Ajuster plinthe + caisson pour atteindre la cible
- regle: Triangle d'activité (évier-plaque-frigo) : chaque côté 120-270cm, total ≤ 650cm · action: Informer
- regle: Distance meubles hauts ↔ plan de travail ≥ 50cm · action: Alerter
- regle: Hotte : 65cm au-dessus gaz, 50cm au-dessus induction · action: Alerter
- regle: Meuble haut : charge par boîtier ≤ 65kg · action: Calculer poids total estimé
- regle: Lave-vaisselle ou four intégré adjacent · action: Vérifier fileurs, ventilation et jeux de pose
- regle: Plan de travail avec débord ou retombée atypique · action: Vérifier ouverture des portes/tiroirs
- regle: Meuble évier · action: Imposer protection contre humidité et accès plomberie

## Variantes
- 
  - **nom** : Casserolier (tiroirs uniquement)
  - **portes** : non
  - **tiroirs** :
    - h facade mm: 140
    - h facade mm: 140
    - h facade mm: 400
- nom: Meuble évier · fond decoupe: oui · plomberie accessible: oui
- nom: Meuble d'angle · type: angle_droit_borgne · fileur mm: 65
- nom: Caisson avec casserolier · tiroirs profonds: oui
- nom: Colonne four + micro-ondes · niches techniques: oui
- nom: Îlot central · double face: oui

## Pièges courants
- Oublier le retrait du fond pour le rail de suspension (15mm)
- Ne pas vérifier le poids total du meuble haut chargé vs capacité rail
- Portes qui tapent contre le mur en angle → fileur obligatoire
- Plan de travail : mesurer EN DERNIER, après pose des caissons de niveau
- Oublier l'épaisseur réelle des façades et poignées dans les angles
- Niveau du sol négligé, puis plan de travail impossible à aligner



---

<!-- chunk_id: projet.etagere_murale | source: corpus v3 de l'auteur -->

# 🪵 Projet type : Étagère murale

**Description** : Étagère fixée au mur, avec ou sans joues


## Composants obligatoires
- tablette

## Composants optionnels
- joue_gauche
- joue_droite
- fond
- tablette_supplementaire

## Dimensions par défaut
- **largeur mm** : 800
- **profondeur mm** : 220
- **nb tablettes** : 3
- **espacement mm** : 300
- **epaisseur mm** : 18

## Règles de génération
- **avec joues** :
  - **tablettes** : largeur_interieure - 2mm
  - **joues** : hauteur_totale
  - **fond** : optionnel (rigidité)
- **sans joues** :
  - **tablettes** : indépendantes, fixées individuellement au mur
  - **fixation** : Équerres cachées, rails invisibles, ou tasseau (french cleat)

## Contraintes
- regle: Portée sans support intermédiaire = f(matériau, épaisseur) · action: Vérifier domaine 1
- regle: Type de mur → type de cheville · action: Alerter et guider le choix
- regle: Charge totale estimée vs capacité fixation · action: Calculer
- regle: Étagère au-dessus d'un lit, bureau ou zone de passage · action: Alerter sécurité fixation critique

## Variantes
- nom: Étagère en U · joues: oui · forme en U: oui
- nom: Étagère invisible · fixation invisible: oui

## Pièges courants
- Visser dans du placo sans trouver le montant → chute assurée
- Étagère trop profonde par rapport aux équerres → basculement
- Ne pas vérifier l'horizontalité au niveau → livres qui glissent
- Poids des livres mal évalué sur fixation invisible



---

<!-- chunk_id: projet.lit_cabane_mezzanine | source: corpus v3 de l'auteur -->

# 🏠 Projet type : Lit cabane / Mezzanine enfant

**Description** : Lit surélevé ou cabane pour enfant, avec espace de jeu ou bureau dessous


## Composants obligatoires
- montants
- cadre_sommier
- garde_corps
- echelle

## Composants optionnels
- toit_cabane
- barriere_decorative
- bureau_dessous
- etagere
- tiroir_sous_lit
- rideau

## Dimensions par défaut
- **couchage mm** :
  - **longueur** : 1900
  - **largeur** : 900
- **hauteur mezzanine mm** : 1800
- **hauteur cabane mm** : 1300
- **section montants mm** :
  - **min** : 70×70
  - **standard** : 90×90

## Règles de génération
- **mezzanine** :
  - **hauteur sous plancher mm** :
    - **min** : 1200
    - **note** : Pour bureau enfant dessous
  - **hauteur au dessus matelas mm** :
    - **min** : 600
    - **note** : Pour s'asseoir dans le lit
  - **hauteur totale max mm** : 2200
  - **note** : Hauteur sous plafond - hauteur_mezzanine ≥ 60cm (s'asseoir)
- **cabane mi hauteur** :
  - **hauteur plancher mm** :
    - **min** : 600
    - **max** : 900
  - **espace dessous** : Rangement, coin lecture, cabane de jeu

## Contraintes
- regle: Garde-corps obligatoire sur tous les côtés sauf accès échelle · action: Imposer · severite: critique
- regle: Espacement barreaux ≤ 6.5cm (norme enfant) · action: Vérifier · severite: critique
- regle: Hauteur sous plafond - hauteur mezzanine ≥ 60cm · action: Alerter si insuffisant
- regle: Section montants ≥ 70×70mm · action: Alerter si inférieur · severite: critique
- regle: Assemblage par boulons traversants, pas de vis seules · action: Alerter · severite: critique
- regle: Matelas max 15-18cm d'épaisseur pour que le garde-corps reste efficace · action: Informer

## Pièges courants
- Vis seules pour la structure → danger d'effondrement
- Garde-corps trop bas avec matelas épais → enfant qui tombe
- Barreaux trop espacés → tête d'enfant coincée
- Échelle non fixée → bascule
- Bois brut non poncé → échardes
- Pas de plafond suffisant au-dessus du matelas → enfant qui se cogne en s'asseyant

## Sécurité (NF EN 747)
- **garde corps** :
  - **hauteur min au dessus matelas mm** : 300
  - **espacement barreaux max mm** : 65
  - **ouverture acces largeur mm** :
    - **min** : 400
    - **max** : 500
  - **note** : Norme NF EN 747 : espacement max 7.5cm entre barreaux (75mm)
- **echelle** :
  - **largeur min mm** : 300
  - **espacement barreaux mm** :
    - **min** : 200
    - **max** : 300
  - **inclinaison deg** :
    - **min** : 70
    - **max** : 80
  - **fixation** : Solidaire de la structure, pas simplement posée
- **structure** :
  - **section montants min mm** : 70×70
  - **assemblage** : Boulons traversants ou ferrures métalliques — JAMAIS vis seules
  - **visserie min** : Boulons M8 ou M10 avec écrou + rondelle
- **age minimum recommande** :
  - **mezzanine haute** : 6 ans
  - **cabane mi hauteur** : 3 ans



---

<!-- chunk_id: projet.meuble_chaussures | source: corpus v3 de l'auteur -->

# 👟 Projet type : Meuble à chaussures

**Description** : Rangement dédié aux chaussures, compact et fonctionnel


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous

## Composants optionnels
- porte
- abattant_incline
- tablette
- tiroir
- fond
- plinthe

## Dimensions par défaut
- **hauteur mm** : 1200
- **largeur mm** : 800
- **profondeur mm** : 300
- **epaisseur mm** : 18

## Règles de génération
- **tablettes inclinees** :
  - **angle deg** :
    - **min** : 15
    - **max** : 20
  - **butee avant mm** : 15
  - **espacement mm** : 200
  - **profondeur reduite mm** :
    - **min** : 250
    - **max** : 300
  - **note** : Réduit la profondeur nécessaire vs tablettes horizontales
- **tablettes horizontales** :
  - **espacement chaussures plates mm** : 180
  - **espacement bottines mm** : 250
  - **espacement bottes mm** : 450
  - **profondeur mm** : 350
- **abattants** :
  - **description** : Portes à bascule avec rangement intégré (style IKEA TRONES)
  - **profondeur fermee mm** : 180
  - **capacite** : 2-3 paires par abattant

## Contraintes
- regle: Profondeur ≥ 30cm pour chaussures adulte (longueur 28-34cm) · action: Alerter si < 28cm
- regle: Ventilation obligatoire · action: Proposer fond ajouré ou trous
- regle: En entrée étroite : profondeur max 25cm avec tablettes inclinées · action: Suggérer inclinaison

## Variantes
- nom: Meuble fermé avec portes · profondeur mm: 350 · portes: oui
- nom: Tablettes inclinées ouvertes · profondeur mm: 250 · portes: non
- nom: Abattants basculants · profondeur mm: 180 · compact: oui
- nom: Banc à chaussures · assise: oui · hauteur mm: 500

## Pièges courants
- Pas de ventilation → odeurs et moisissures
- Profondeur 25cm avec tablettes horizontales → chaussures qui dépassent
- Oublier les bottes → prévoir au moins un compartiment haut (45cm)



---

<!-- chunk_id: projet.meuble_salle_de_bain | source: corpus v3 de l'auteur -->

# 🚿 Projet type : Meuble salle de bain

**Description** : Meuble vasque, colonne, rangement pour salle de bain


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous
- fond

## Composants optionnels
- tiroir
- porte
- tablette_reglable
- plinthe

## Dimensions par défaut
- **hauteur mm** : 850
- **largeur mm** : 800
- **profondeur mm** : 450
- **epaisseur panneau mm** : 18

## Règles de génération
- **meuble vasque** :
  - **dessus** : Découpe pour vasque (dimensions selon modèle)
  - **fond** : Découpe pour évacuation et arrivées d'eau
  - **tiroirs ou portes** : 2 portes si vasque encastrée, tiroirs échancrés si vasque posée

## Contraintes
- regle: Matériau résistant à l'humidité obligatoire · action: Forcer CP marine, MDF hydro ou mélaminé P5
- regle: Piètement surélevé ou suspendu · action: Recommander (nettoyage sol + protection eau)
- regle: Accès plomberie · action: Fond démontable ou trappe d'accès
- regle: Normes électriques zones 0/1/2/3 · action: Informer (pas de prise ni interrupteur en zone 1)
- regle: Meuble suspendu avec vasque lourde · action: Calculer charge murale renforcée
- regle: Plan vasque mince en panneau dérivé · action: Alerter risque gonflement si chant exposé

## Variantes
- nom: Colonne salle de bain · colonne haute: oui
- nom: Double vasque · double decoupe: oui

## Pièges courants
- Utiliser du MDF standard → gonfle à la première éclaboussure
- Fond fixe sans accès plomberie → galère en cas de fuite
- Oublier la ventilation intérieure → moisissures
- Tiroirs qui butent contre le siphon → prévoir tiroir échancré
- Chants non protégés autour des découpes de plomberie et vasque
- Tiroirs non échancrés au bon endroit pour siphon déporté



---

<!-- chunk_id: projet.meuble_tv | source: corpus v3 de l'auteur -->

# 📺 Projet type : Meuble TV

**Description** : Meuble bas pour téléviseur, équipements multimédia et rangement


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous
- fond

## Composants optionnels
- tablette_fixe
- separateur
- porte
- tiroir
- niche_ouverte
- passe_cables

## Dimensions par défaut
- **hauteur mm** : 450
- **largeur mm** : 1600
- **profondeur mm** : 450
- **epaisseur panneau mm** : 18

## Règles de génération
- **structure type** : 3 compartiments (gauche fermé, centre ouvert, droit fermé)
- **separateurs** : 2
- **compartiment central** :
  - **usage** : Niche ouverte pour décodeur, console, barre de son
  - **largeur mm** :
    - **min** : 500
    - **max** : 700
  - **hauteur niche mm** :
    - **min** : 150
    - **max** : 200
  - **ventilation** : Fond ajouré ou absent dans la niche centrale
- **compartiments lateraux** :
  - **portes** : applique
  - **tablette reglable** : 1

## Quincaillerie associée
- **portes** :
  - Charnières Ø35mm 110° avec amortisseur
- **tiroirs** :
  - Coulisses sortie totale
- **passe cables** :
  - Perçage Ø60mm dans le fond
- **fixation** : Si suspendu : rail de suspension ou french cleat

## Contraintes
- regle: Largeur meuble ≥ largeur TV + 30cm · action: Alerter
- regle: Ventilation obligatoire pour appareils électroniques · action: Proposer fond ajouré
- regle: Poids TV + appareils → vérifier portée dessus · action: Renforcer si > 40kg
- regle: Si suspendu : charge max au mur à vérifier · action: Calculer poids total
- regle: Barre de son prévue · action: Vérifier niche centrale et débord du plateau
- regle: Porte fermée devant appareil télécommandé · action: Proposer porte tissu, verre ou report infrarouge

## Variantes
- nom: Meuble TV bas posé · hauteur mm: 450 · pieds: oui
- nom: Meuble TV suspendu · hauteur mm: 350 · fixation: rail
- nom: Meuble TV avec colonne latérale · colonne hauteur mm: 1800
- nom: Meuble TV avec claustra de ventilation · ventilation renforcee: oui

## Pièges courants
- Oublier la ventilation → surchauffe des appareils
- Fond plein sans passe-câbles → câbles qui sortent par le dessus (laid)
- Meuble trop étroit → TV instable visuellement
- Suspendu sur placo sans montants → chute garantie
- Fond ajouré mais sans gestion propre des câbles
- Réception télécommande bloquée par une façade opaque



---

<!-- chunk_id: projet.placard | source: corpus v3 de l'auteur -->

# 🚪 Projet type : Placard / Dressing

**Description** : Rangement fermé intégré, dressing, penderie


## Composants obligatoires
- joue_gauche
- joue_droite
- dessus
- dessous
- fond

## Composants optionnels
- tablette_fixe
- tablette_reglable
- separateur
- porte
- tiroir
- tringle_penderie
- bandeau
- plinthe
- joue_habillage
- fileur

## Dimensions par défaut
- **hauteur mm** : 2400
- **largeur mm** : 1200
- **profondeur mm** : 600
- **epaisseur panneau mm** : 18
- **plinthe mm** : 80

## Règles de génération
- **joues** :
  - **longueur** : hauteur - plinthe
  - **largeur** : profondeur
- **dessus dessous** :
  - **longueur** : largeur - (2 × épaisseur)
  - **largeur** : profondeur
- **portes** :
  - **type defaut** : applique
  - **calcul** : Formules F_CON_001 ou F_CON_002 selon nb portes
  - **hauteur** : Formule F_CON_008 (zone couverte + recouvrements - jeux)
- **tringle** :
  - **longueur** : largeur_interieure - 10mm
  - **position haut** : 50mm sous le dessus ou tablette fixe
  - **hauteur libre sous tringle** :
    - **chemises vestes mm** : 1100
    - **robes manteaux mm** : 1600
- **tiroirs** :
  - **position** : Zone basse (80-120cm du sol) pour accès ergonomique
  - **calcul largeur** : F_QUI_002 (intérieur - 25.4mm)
  - **calcul facade** : Tiroirs multiples empilés (domaine 3)

## Quincaillerie associée
- **portes battantes** :
  - Charnières Ø35mm applique 110°
  - Poignées entraxe 128 ou 160mm
- **portes coulissantes** :
  - Rails haut/bas
  - Roulettes
  - Guide bas
- **tiroirs** :
  - Coulisses à billes sortie totale
  - Façade rapportée
- **penderie** :
  - Supports de tringle Ø25mm
  - Tringle chromée
- **taquets** : Ø5mm système 32

## Contraintes
- regle: Profondeur penderie ≥ 55cm intérieur · action: Alerter si profondeur < 55cm
- regle: Porte coulissante → perte de 50% d'accès simultané · action: Informer l'utilisateur
- regle: Porte battante → recul min 90cm devant · action: Vérifier espace disponible
- regle: Hauteur > 240cm · action: Proposer caisson haut séparé + corniche
- regle: Largeur module tiroirs ≤ 80cm · action: Au-delà : coulisses renforcées
- regle: Module large > 100 cm avec une seule porte battante · action: Alerter poids et prise au vent, proposer 2 portes
- regle: Dressing ouvert sans fond ni fixation · action: Imposer contreventement ou fixation murale

## Variantes
- nom: Penderie simple · tringle: oui · tablettes: 1 · tiroirs: 0
- nom: Dressing complet · tringle haute: oui · tringle basse: oui · tiroirs: 3 · tablettes: 4
- nom: Placard d'entrée · profondeur mm: 400 · pateres: oui · etagere chaussures: oui
- nom: Sous-pente · hauteur variable: oui · modules degressifs: oui
- nom: Dressing pont de lit · caisson haut: oui · modules lateraux: oui
- nom: Dressing ouvert sans porte · portes: non

## Pièges courants
- Profondeur 50cm = cintres qui frottent contre les portes
- Oublier le fileur contre le mur (faux équerrage → portes qui coincent)
- Portes coulissantes : penser au recouvrement entre les panneaux (50-70mm)
- Tiroirs derrière portes coulissantes → vérifier qu'ils ne butent pas sur le rail
- Ne pas vérifier la hauteur de cintres avec vêtements volumineux
- Oublier les plinthes ou prises murales qui empêchent le meuble de se plaquer



---

<!-- chunk_id: projet.sous_escalier | source: corpus v3 de l'auteur -->

# 🪜 Projet type : Meuble sous-escalier

**Description** : Aménagement sur mesure exploitant l'espace sous un escalier


## Composants obligatoires
- joue_exterieure
- dessus_ou_rampant

## Composants optionnels
- porte
- tiroir_extractible
- tablette
- separateur
- fond
- plinthe

## Dimensions par défaut
- **hauteur max mm** : 2200
- **hauteur min mm** : 300
- **profondeur mm** : 800
- **angle pente deg** :
  - **min** : 30
  - **max** : 40
  - **standard** : 35

## Règles de génération
- **parametrique** :
  - **formule hauteur** : h(x) = h_depart + x × tan(angle_pente)
  - **modules independants** : oui
  - **decoupage** : Diviser en modules de 40-60cm de large, du plus bas au plus haut
- **zonage par hauteur** :
  - **zone basse 0 60cm** :
    - **solutions** :
      - Tiroirs extractibles sur coulisses charge lourde
      - Coffre à chaussures
    - **note** : Porte battante impraticable sous pente basse
  - **zone intermediaire 60 120cm** :
    - **solutions** :
      - Placards avec portes
      - Tiroirs pleine extraction
      - Niches ouvertes
    - **note** : Zone la plus polyvalente
  - **zone haute 120 plus** :
    - **solutions** :
      - Placard pleine hauteur
      - Penderie courte
      - Bibliothèque
    - **note** : Exploiter au maximum la hauteur disponible

## Contraintes
- regle: Ne jamais couper limons, contremarches ou appuis structurels · action: Alerter — validation structurelle requise · severite: critique
- regle: Mesurer la pente EN PLUSIEURS POINTS · action: Demander h_min, h_max et longueur au sol
- regle: Déduire 2-3cm de la hauteur dispo pour panneaux de finition et jeu · action: Appliquer automatiquement
- regle: Vide sanitaire 5cm contre le mur du fond · action: Soustraire de la profondeur utile
- regle: Nez de marche débordant · action: Alerter — décaler les façades ou cadre de compensation

## Variantes
- nom: Tiroirs extractibles (zone basse) · type: tiroirs_profonds
- nom: Placard multizone · type: mixte_portes_tiroirs
- nom: Bureau sous escalier · hauteur min mm: 750 · note: Uniquement dans la zone haute
- nom: Cave à vin · note: Si température et humidité compatibles
- nom: Vestiaire d'entrée · pateres: oui · banc: oui

## Pièges courants
- Mesurer en un seul point → la pente n'est jamais parfaitement régulière
- Module monolithique → transport et installation impossibles, préférer modules indépendants
- Profondeur > 60cm sans extractible → le fond est inaccessible et inutile
- Réseau (électricité, plomberie) sous l'escalier → prévoir trappe d'accès
- Push-to-open recommandé en circulation étroite (pas de poignée qui dépasse)



---

<!-- chunk_id: projet.table | source: corpus v3 de l'auteur -->

# 🪵 Projet type : Table sur mesure

**Description** : Table de repas, table basse, console à fabriquer soi-même


## Composants obligatoires
- plateau

## Composants optionnels
- pieds
- ceinture
- traverse
- rallonge
- tiroir

## Dimensions par défaut
- **type** : repas_6_personnes
- **longueur mm** : 1800
- **largeur mm** : 900
- **hauteur mm** : 750
- **epaisseur plateau mm** : 30

## Règles de génération
- **plateau** :
  - **longueur** : selon nb convives × 60cm
  - **largeur** : 90-100cm
- **ceinture** :
  - **hauteur mm** :
    - **min** : 60
    - **max** : 100
  - **retrait bord mm** :
    - **min** : 20
    - **max** : 40
  - **note** : Hauteur libre sous ceinture ≥ 62cm pour les genoux
- **pieds** :
  - **section mm** :
    - **min** : 60×60
    - **max** : 80×80
  - **retrait bord mm** :
    - **min** : 80
    - **ideal** : 120

## Contraintes
- regle: Hauteur sous ceinture ≥ 62cm · action: Alerter
- regle: Épaisseur plateau vs portée sans ceinture · action: Calculer fléchissement
- regle: Stabilité latérale si pieds sans ceinture · action: Recommander entretoises
- regle: Table extensible · action: Vérifier alignement rallonges, épaisseur et verrouillage
- regle: Table enfant ou usage intensif familial · action: Proposer angles adoucis

## Variantes
- nom: Table de repas · hauteur mm: 750
- nom: Table basse · hauteur mm: 400 · profondeur mm: 600
- nom: Table haute / bar · hauteur mm: 1100 · tabouret mm: 800
- nom: Table extensible · rallonge: oui · ferrure: coulisses synchrones
- nom: Console extensible · profondeur fermee mm: 350 · rallonges: oui
- nom: Tablette murale rabattable · fixation murale: oui · compas: oui

## Pièges courants
- Plateau massif sans ceinture ni traverse → fléchissement au centre
- Pieds trop près du bord → basculement quand quelqu'un s'appuie
- Table extensible : épaisseur rallonge ≠ épaisseur plateau → décalage disgracieux
- Oublier de traiter les mouvements du bois massif (jeu longitudinal, fixation par trou oblong)
- Ceinture qui gêne les genoux alors que la hauteur totale semble correcte
- Piètement esthétique mais trop étroit pour la stabilité



---

<!-- chunk_id: projet.templates_defaut | source: corpus v3 de l'auteur -->

# Templates par défaut : 9 types de meubles (valeurs de démarrage)

Templates de référence : valeurs par défaut intelligentes pour 9 types de meubles courants.

## 📚 Bibliothèque
**ID** : `bibliotheque`
**Description** : Bibliothèque murale classique, avec tablettes fixes et réglables.
**AI hint** : bibliothèque murale avec tablettes pour livres
**Matériau par défaut** : `cp_bouleau`

**Dimensions par défaut** :
- largeur_mur_cm : 200
- profondeur_mur_cm : 35
- hauteur_plafond_cm : 250
- plinthe_h_cm : 10
- plinthe_p_cm : 2

**Corps par défaut** :
- largeur_cm : 80
- profondeur_cm : 28
- hauteur_utile_cm : 240
- tablettes_fixes : 2
- tablettes_reglables : 4

## 🪵 Étagère murale
**ID** : `etagere`
**Description** : Étagère ouverte légère, fixée au mur. 3-5 niveaux.
**AI hint** : étagère murale ouverte, légère, 3 à 5 niveaux
**Matériau par défaut** : `cp_bouleau`

**Dimensions par défaut** :
- largeur_mur_cm : 150
- profondeur_mur_cm : 30
- hauteur_plafond_cm : 250

**Corps par défaut** :
- largeur_cm : 60
- profondeur_cm : 22
- hauteur_utile_cm : 120
- tablettes_fixes : 4

## 📺 Meuble TV
**ID** : `meuble-tv`
**Description** : Meuble bas pour téléviseur, avec niches et portes.
**AI hint** : meuble TV bas, longueur 150-180 cm, hauteur 50 cm, avec niches
**Matériau par défaut** : `melamine`

**Dimensions par défaut** :
- largeur_mur_cm : 300
- profondeur_mur_cm : 50
- hauteur_plafond_cm : 250

**Corps par défaut** :
- largeur_cm : 60
- profondeur_cm : 45
- hauteur_utile_cm : 50
- nb_caissons : 3

## 👔 Armoire / Dressing
**ID** : `armoire`
**Description** : Armoire ou dressing avec penderie et étagères.
**AI hint** : armoire ou dressing, penderie + étagères, hauteur 200-240 cm
**Matériau par défaut** : `melamine`

**Dimensions par défaut** :
- largeur_mur_cm : 200
- profondeur_mur_cm : 65
- hauteur_plafond_cm : 250
- plinthe_h_cm : 8
- plinthe_p_cm : 2

**Corps par défaut** :
- penderie_largeur_cm : 90
- etageres_largeur_cm : 60
- profondeur_cm : 55
- hauteur_utile_cm : 230

## 🍽 Buffet / Bahut
**ID** : `buffet`
**Description** : Meuble de rangement bas avec portes et/ou tiroirs.
**AI hint** : buffet bas, hauteur 80-90 cm, largeur 120-180 cm, avec portes
**Matériau par défaut** : `cp_bouleau`

**Dimensions par défaut** :
- largeur_mur_cm : 250
- profondeur_mur_cm : 50
- hauteur_plafond_cm : 250

**Corps par défaut** :
- largeur_cm : 60
- profondeur_cm : 40
- hauteur_utile_cm : 80
- nb_caissons : 2

## 🖥 Bureau
**ID** : `bureau`
**Description** : Bureau avec plateau, caisson de rangement et passe-câbles.
**AI hint** : bureau de travail, plateau 120-160 cm, caisson tiroirs
**Matériau par défaut** : `cp_bouleau`

**Dimensions par défaut** :
- largeur_mur_cm : 200
- profondeur_mur_cm : 70
- hauteur_plafond_cm : 250

**Corps par défaut** :
- plateau_largeur_cm : 140
- plateau_profondeur_cm : 65
- hauteur_assise_cm : 73
- caisson_tiroirs_largeur_cm : 40
- caisson_tiroirs_profondeur_cm : 55
- caisson_tiroirs_hauteur_cm : 60

## 🍳 Caisson cuisine
**ID** : `cuisine`
**Description** : Caisson de cuisine standard (haut ou bas), adaptable.
**AI hint** : caisson cuisine, norme 32 mm, profondeur 56-58 cm bas ou 32 cm haut
**Matériau par défaut** : `melamine`

**Dimensions par défaut** :
- largeur_mur_cm : 300
- profondeur_mur_cm : 65
- hauteur_plafond_cm : 250
- plinthe_h_cm : 15
- plinthe_p_cm : 2

**Corps par défaut** :
- bas_profondeur_cm : 56
- bas_hauteur_cm : 70
- haut_profondeur_cm : 32
- haut_hauteur_cm : 70
- largeur_caisson_cm : 60

## 🚿 Meuble salle de bain
**ID** : `sdb`
**Description** : Meuble vasque avec rangement, adapté à l'humidité.
**AI hint** : meuble vasque salle de bain, résistant humidité, 60-120 cm
**Matériau par défaut** : `cp_okoume`

**Dimensions par défaut** :
- largeur_mur_cm : 150
- profondeur_mur_cm : 50
- hauteur_plafond_cm : 250

**Corps par défaut** :
- largeur_cm : 80
- profondeur_cm : 45
- hauteur_utile_cm : 60

## 🚪 Placard mural
**ID** : `placard`
**Description** : Placard encastré avec portes, du sol au plafond.
**AI hint** : placard mural encastré, sol au plafond, portes coulissantes ou battantes
**Matériau par défaut** : `melamine`

**Dimensions par défaut** :
- largeur_mur_cm : 160
- profondeur_mur_cm : 60
- hauteur_plafond_cm : 250
- plinthe_h_cm : 8
- plinthe_p_cm : 2

**Corps par défaut** :
- largeur_cm : 80
- profondeur_cm : 60
- hauteur_utile_cm : 240



---

<!-- chunk_id: projet.vestiaire_entree | source: corpus v3 de l'auteur -->

# 🧥 Projet type : Vestiaire d'entrée

**Description** : Meuble d'entrée combinant patères, miroir, rangement chaussures et banc


## Composants obligatoires
- joue_gauche
- joue_droite
- fond

## Composants optionnels
- banc
- pateres
- miroir
- etagere_chapeau
- rangement_chaussures
- tiroir
- porte
- tablette

## Dimensions par défaut
- **hauteur mm** : 1900
- **largeur mm** : 1000
- **profondeur mm** : 350
- **hauteur banc mm** : 450

## Règles de génération
- **zones** :
  - **zone banc 0 45cm** :
    - **banc** : oui
    - **coffre** : oui
    - **chaussures dessous** : oui
  - **zone pateres 120 170cm** :
    - **pateres** : oui
    - **espacement mm** : 150
    - **hauteur patere mm** : 1500
  - **zone etagere haute 170 190cm** :
    - **etagere** : oui
    - **usage** : Bonnets, gants, sacs
- **miroir** :
  - **position** : Porte intérieure ou panneau latéral
  - **hauteur mm** :
    - **min** : 1000
    - **max** : 1400

## Contraintes
- regle: Profondeur ≤ 35-40cm en entrée (circulation) · action: Alerter si > 40cm
- regle: Patères à hauteur enfant (90-100cm) si famille · action: Suggérer double rangée
- regle: Fixation murale obligatoire (meuble étroit et haut) · action: Imposer

## Pièges courants
- Profondeur insuffisante pour cintres → utiliser patères, pas tringle
- Miroir non sécurisé → risque de chute et bris
- Oublier la rangée de patères basse pour les enfants
- Étagère haute inaccessible sans tabouret → la rendre moins profonde



