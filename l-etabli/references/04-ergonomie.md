# 04-ergonomie

<!-- Corpus menuiserie v3.1.0 — catégorie 04-ergonomie -->

## Sommaire du fichier
- `engine.content_analyzer` — Table de rangement par contenu (module, zone, hauteurs unitaires)
- `ergo.formulas` — Ergonomie : formules de dimensionnement
- `ergo.meuble.banquette_coffre` — Ergonomie meuble : Banquette coffre
- `ergo.meuble.bibliotheque` — Ergonomie meuble : Bibliotheque
- `ergo.meuble.buffet_vaisselier` — Ergonomie meuble : Buffet vaisselier
- `ergo.meuble.bureau` — Ergonomie meuble : Bureau
- `ergo.meuble.commode` — Ergonomie meuble : Commode
- `ergo.meuble.console_entree` — Ergonomie meuble : Console entree
- `ergo.meuble.cuisine` — Ergonomie meuble : Cuisine
- `ergo.meuble.dressing_armoire` — Ergonomie meuble : Dressing armoire
- `ergo.meuble.etagere_murale` — Ergonomie meuble : Etagere murale
- `ergo.meuble.lit_rangement` — Ergonomie meuble : Lit rangement
- `ergo.meuble.meuble_salle_de_bain` — Ergonomie meuble : Meuble salle de bain
- `ergo.meuble.meuble_sous_escalier` — Ergonomie meuble : Meuble sous escalier
- `ergo.meuble.meuble_tv` — Ergonomie meuble : Meuble tv
- `ergo.meuble.placard_rangement` — Ergonomie meuble : Placard rangement
- `ergo.meuble.table_salle_a_manger` — Ergonomie meuble : Table salle a manger
- `ergo.objets_reference` — Ergonomie : dimensions de référence des objets stockés (livres, médias, vêtements, vaisselle, chaussures, jouets)
- `ergo.principes_generaux` — Ergonomie : principes généraux (zones de confort, circulations, portée)

---

<!-- chunk_id: engine.content_analyzer | source: corpus v3 de l'auteur -->

# Table de rangement par contenu (module, zone, hauteurs unitaires)

Table de correspondance entre **ce qu'on range** et le **module + zone** adaptés, avec les hauteurs unitaires et espacements de tablette. Sert à dimensionner un meuble à partir d'un inventaire d'objets.

## Catégories de contenu
| Contenu | Module | Zone | Hauteur unitaire | Espacement tablette |
|---|---|---|---|---|
| Chemises / vestes (cintres) | penderie courte | active | 50 mm | — |
| Manteaux / robes longues | penderie longue | active | 80 mm | — |
| Pantalons / jupes (pliés) | tiroirs | active | 40 mm | — |
| Pulls / t-shirts (pliés) | étagères | active | 35 mm | 280 mm |
| Chaussures (paires) | range-chaussures | bas | 40 mm | — |
| Bottes | étagères | bas | 120 mm | 450 mm |
| Livres de poche / romans | étagères | active | 8 mm | 220 mm |
| Grands livres / encyclopédies | étagères | bas | 15 mm | 350 mm |
| BD / albums | étagères | active | 12 mm | 340 mm |
| Vinyles | étagères | bas | 4 mm | 340 mm |
| Jeux de société | étagères | bas | 70 mm | 350 mm |
| Vêtements hors saison | étagères | haut | 60 mm | 300 mm |
| Draps / serviettes | étagères | haut | 50 mm | 300 mm |
| Sacs / accessoires | étagères | haut | 100 mm | 350 mm |

## Placement ergonomique par zone
- **Bas (0–400 mm)** : objets lourds, chaussures, tiroirs.
- **Active (400–1400 mm)** : usage fréquent, penderies, tablettes principales.
- **Haut (1800 mm +)** : saisonnier, rare, léger.

## Hauteur minimale de zone par module
| Module | Hauteur min |
|---|---|
| Penderie courte | 1100 mm |
| Penderie longue | 1600 mm |
| Bloc tiroirs | 300 mm |
| Range-chaussures | 400 mm |
| Étagères réglables | 200 mm |

## Heuristiques de dimensionnement
- **Tiroirs** : `nombre = ⌈nb_articles / 8⌉`, borné 1–6.
- **Range-chaussures** : `niveaux = ⌈paires / 5⌉`, borné 2–8.
- **Étagères** : `nombre = ⌈hauteur_nécessaire / espacement⌉`, borné 1–12.
- Repère : **~20 chemises par 1000 mm** de tringle.



---

<!-- chunk_id: ergo.formulas | source: corpus v3 de l'auteur -->

# Ergonomie : formules de dimensionnement

## worktop_height_ideal
- **ID** : `F_ERGO_001`
- **Variables** : user_height_mm
- **Formule** : `user_height_mm * 0.52`
- **Sortie** : worktop_height_mm

## shelf_depth
- **ID** : `F_ERGO_002`
- **Variables** : max_object_width_mm
- **Formule** : `max_object_width_mm + 30`
- **Sortie** : shelf_depth_mm

## shelf_spacing
- **ID** : `F_ERGO_003`
- **Variables** : max_object_height_mm, margin_mm
- **Formule** : `max_object_height_mm + margin_mm`
- **Sortie** : shelf_spacing_mm
- **Paramètres** : - **margin mm** :
  - **min** : 50
  - **max** : 70
  - **default** : 60

## hanging_rod_height
- **ID** : `F_ERGO_004`
- **Variables** : longest_garment_mm, hanger_height_mm, bottom_margin_mm
- **Formule** : `longest_garment_mm + hanger_height_mm + bottom_margin_mm`
- **Sortie** : rod_zone_height_mm
- **Paramètres** : - **hanger height mm** :
  - **default** : 100
- **bottom margin mm** :
  - **default** : 50

## tv_unit_width
- **ID** : `F_ERGO_005`
- **Variables** : tv_width_mm
- **Formule** : `tv_width_mm + 300`
- **Sortie** : unit_min_width_mm

## desk_height
- **ID** : `F_ERGO_006`
- **Variables** : user_height_mm
- **Formule** : `user_height_mm * 0.41`
- **Sortie** : desk_height_mm

## table_length_rectangular
- **ID** : `F_ERGO_007`
- **Variables** : seats_per_long_side, width_per_seat_mm, end_margin_mm
- **Formule** : `seats_per_long_side * width_per_seat_mm + 2 * end_margin_mm`
- **Sortie** : table_length_mm
- **Paramètres** : - **width per seat mm** :
  - **min** : 550
  - **max** : 650
  - **default** : 600
- **end margin mm** :
  - **min** : 50
  - **max** : 150
  - **default** : 100

## table_diameter_round
- **ID** : `F_ERGO_008`
- **Variables** : num_seats, width_per_seat_mm
- **Formule** : `(num_seats * width_per_seat_mm) / 3.14159`
- **Sortie** : table_diameter_mm
- **Paramètres** : - **width per seat mm** :
  - **min** : 550
  - **max** : 600
  - **default** : 580

## seat_height_for_table
- **ID** : `F_ERGO_009`
- **Variables** : table_height_mm
- **Formule** : `table_height_mm - 285`
- **Sortie** : seat_height_mm
- **Paramètres** : - **offset mm** :
  - **min** : 270
  - **max** : 300

## min_clearance_under_table
- **ID** : `F_ERGO_010`
- **Variables** : seat_height_mm
- **Formule** : `seat_height_mm + 240`
- **Sortie** : min_clearance_mm

## tv_viewing_distance
- **ID** : `F_ERGO_011`
- **Variables** : screen_diagonal_mm, resolution_factor
- **Formule** : `screen_diagonal_mm * resolution_factor`
- **Sortie** : viewing_distance_mm
- **Paramètres** : - **resolution factor** :
  - **HD** : 2.5
  - **4K** : 1.5

## under_stairs_height
- **ID** : `F_ERGO_012`
- **Variables** : h_start_mm, x_offset_mm, stair_angle_rad
- **Formule** : `h_start_mm + x_offset_mm * Math.tan(stair_angle_rad)`
- **Sortie** : available_height_mm

## bench_length
- **ID** : `F_ERGO_013`
- **Variables** : num_seats, width_per_seat_mm
- **Formule** : `num_seats * width_per_seat_mm`
- **Sortie** : bench_length_mm
- **Paramètres** : - **width per seat mm** :
  - **min** : 500
  - **max** : 600
  - **default** : 550

## clearance_with_opening
- **ID** : `F_ERGO_014`
- **Variables** : furniture_depth_mm, door_swing_mm, circulation_margin_mm
- **Formule** : `furniture_depth_mm + door_swing_mm + circulation_margin_mm`
- **Sortie** : required_passage_mm
- **Paramètres** : - **circulation margin mm** :
  - **min** : 200
  - **max** : 400
  - **default** : 300

## drawer_front_height
- **ID** : `F_ERGO_015`
- **Variables** : useful_height_mm, structure_mm, gap_mm
- **Formule** : `useful_height_mm + structure_mm + gap_mm`
- **Sortie** : front_height_mm
- **Paramètres** : - **structure mm** :
  - **min** : 30
  - **max** : 50
- **gap mm** :
  - **min** : 3
  - **max** : 6

## daily_access_zone
- **ID** : `F_ERGO_016`
- **Formule** : `null`
- **Sortie** : {'zone_bottom_mm': 700, 'zone_top_mm': 1400}
- **Note** : Constant — not a calculation

## shoe_niche_depth
- **ID** : `F_ERGO_017`
- **Variables** : shoe_length_mm, margin_mm
- **Formule** : `shoe_length_mm + margin_mm`
- **Sortie** : niche_depth_mm
- **Paramètres** : - **margin mm** :
  - **min** : 20
  - **max** : 50
  - **default** : 30

## boot_niche_height
- **ID** : `F_ERGO_018`
- **Variables** : boot_height_mm, margin_mm
- **Formule** : `boot_height_mm + margin_mm`
- **Sortie** : niche_height_mm
- **Paramètres** : - **margin mm** :
  - **min** : 30
  - **max** : 80
  - **default** : 50

## drawer_useful_depth
- **ID** : `F_ERGO_019`
- **Variables** : outer_depth_mm, back_thickness_mm, front_thickness_mm, slide_gap_mm
- **Formule** : `outer_depth_mm - back_thickness_mm - front_thickness_mm - slide_gap_mm`
- **Sortie** : useful_depth_mm
- **Paramètres** : - **back thickness mm** :
  - **min** : 8
  - **max** : 19
- **front thickness mm** :
  - **min** : 18
  - **max** : 22
- **slide gap mm** :
  - **min** : 25
  - **max** : 40

## drawer_handle_height
- **ID** : `F_ERGO_020`
- **Variables** : user_elbow_height_mm
- **Formule** : `user_elbow_height_mm - 200`
- **Sortie** : ideal_handle_height_mm
- **Paramètres** : - **offset mm** :
  - **min** : 150
  - **max** : 250

## child_bookshelf_niche
- **ID** : `F_ERGO_021`
- **Variables** : object_height_mm, margin_factor
- **Formule** : `object_height_mm * margin_factor`
- **Sortie** : niche_height_mm
- **Paramètres** : - **margin factor** :
  - **min** : 1.1
  - **max** : 1.2
  - **default** : 1.15



---

<!-- chunk_id: ergo.meuble.banquette_coffre | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Banquette coffre

- **description** : Banquette d'assise avec coffre de rangement intégré
- **hauteur assise mm** :
  - **min** : 420
  - **ideal** : 450
  - **max** : 480
- **profondeur assise mm** :
  - **min** : 400
  - **ideal** : 450
  - **max** : 500
- **profondeur totale mm** :
  - **sans dossier** :
    - **min** : 400
    - **max** : 500
  - **avec dossier** :
    - **min** : 500
    - **max** : 650
- **hauteur dossier mm** :
  - **min** : 300
  - **ideal** : 380
  - **max** : 450
- **longueur par place mm** :
  - **min** : 500
  - **ideal** : 600
- **coffre** :
  - **hauteur utile mm** :
    - **min** : 200
    - **ideal** : 280
    - **max** : 350
  - **profondeur utile mm** :
    - **min** : 250
    - **ideal** : 320
    - **max** : 400
  - **necessite aeration** : oui
- **regles conception** :
  - Avec ouverture dessus : vérifier recul mur/dossier pour le couvercle
  - Profondeur > 50 cm sans coussin ni dossier = confort réduit
  - Pour entrée : hauteur ~45 cm pour chausser facilement



---

<!-- chunk_id: ergo.meuble.bibliotheque | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Bibliotheque

- **description** : Meuble de rangement pour livres, objets déco, médias
- **dimensions globales** :
  - **hauteur basse mm** :
    - **min** : 800
    - **max** : 1100
  - **hauteur mi haute mm** :
    - **min** : 1200
    - **max** : 1500
  - **hauteur standard mm** :
    - **min** : 1800
    - **max** : 2400
  - **profondeur standard mm** :
    - **min** : 250
    - **max** : 350
  - **profondeur beaux livres mm** :
    - **min** : 350
    - **max** : 450
  - **largeur module mm** :
    - **min** : 300
    - **max** : 1200
  - **espace sous plafond mm** :
    - **min** : 50
    - **max** : 100
    - **note** : Respiration visuelle
  - **epaisseur tablette min mm** : 19
  - **epaisseur tablette recommandee mm** : 25
- **hauteurs entre tablettes** :
  - **livres poche** :
    - **hauteur objet mm** : 180
    - **hauteur tablette mm** :
      - **min** : 220
      - **max** : 250
  - **romans A5** :
    - **hauteur objet mm** : 210
    - **hauteur tablette mm** :
      - **min** : 250
      - **max** : 280
  - **BD franco belge** :
    - **hauteur objet mm** : 320
    - **hauteur tablette mm** :
      - **min** : 350
      - **max** : 380
  - **BD comic book** :
    - **hauteur objet mm** : 260
    - **hauteur tablette mm** :
      - **min** : 290
      - **max** : 320
  - **BD manga** :
    - **hauteur objet mm** : 210
    - **hauteur tablette mm** :
      - **min** : 240
      - **max** : 270
  - **beaux livres art** :
    - **hauteur objet mm** :
      - **min** : 300
      - **max** : 400
    - **hauteur tablette mm** :
      - **min** : 350
      - **max** : 450
  - **classeurs** :
    - **hauteur objet mm** : 320
    - **hauteur tablette mm** :
      - **min** : 350
      - **max** : 380
  - **vinyles 33t** :
    - **hauteur objet mm** : 315
    - **hauteur tablette mm** :
      - **min** : 340
      - **max** : 370
  - **CD** :
    - **hauteur objet mm** : 125
    - **hauteur tablette mm** :
      - **min** : 150
      - **max** : 180
  - **DVD** :
    - **hauteur objet mm** : 192
    - **hauteur tablette mm** :
      - **min** : 220
      - **max** : 250
  - **deco vases** :
    - **hauteur tablette mm** :
      - **min** : 300
      - **max** : 400
- **profondeur par contenu** :
  - **livres poche mm** :
    - **min** : 150
    - **max** : 200
  - **romans standard mm** :
    - **min** : 220
    - **max** : 280
  - **BD mm** :
    - **min** : 250
    - **max** : 300
  - **beaux livres mm** :
    - **min** : 300
    - **max** : 450
  - **vinyles mm** :
    - **min** : 320
    - **max** : 350
  - **deco mixte mm** :
    - **min** : 250
    - **max** : 350
- **regles conception** :
  - Profondeur = largeur du plus grand objet + 2-3 cm de marge
  - Hauteur tablette = hauteur du plus grand objet + 5-7 cm
  - Grandes tablettes en bas, plus petites en haut (esthétique + stabilité)
  - Portée max tablette bois massif 25mm : 90 cm ; particules 19mm : 60 cm
  - Fixation anti-basculement obligatoire au-delà de 150 cm de hauteur
  - Espacement passage min 90 cm devant, 105 cm si passage fréquent



---

<!-- chunk_id: ergo.meuble.buffet_vaisselier | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Buffet vaisselier

- **description** : Buffet bas, vaisselier, enfilade pour salle à manger/salon
- **dimensions standard** :
  - **buffet bas** :
    - **hauteur mm** :
      - **min** : 800
      - **max** : 1000
    - **profondeur mm** :
      - **min** : 400
      - **max** : 500
    - **largeur mm** :
      - **min** : 1200
      - **max** : 2200
  - **vaisselier haut** :
    - **hauteur totale mm** :
      - **min** : 1800
      - **max** : 2200
    - **hauteur partie basse mm** :
      - **min** : 800
      - **max** : 1000
    - **profondeur partie haute mm** :
      - **min** : 300
      - **max** : 400
    - **note** : Partie haute moins profonde que la base
- **espacement tablettes** :
  - **assiettes plates mm** :
    - **min** : 150
    - **max** : 200
  - **assiettes creuses empilees mm** :
    - **min** : 200
    - **max** : 250
  - **verres mm** :
    - **min** : 180
    - **max** : 250
  - **bouteilles debout mm** :
    - **min** : 330
    - **max** : 350
- **regles conception** :
  - Hauteur de service buffet : entre 85-95 cm (même logique plan de travail)
  - Portes vitrées : prévoir épaisseur du vitrage (4 mm) dans la feuillure
  - Tiroirs à couverts : hauteur 8-12 cm, diviseurs intérieurs



---

<!-- chunk_id: ergo.meuble.bureau | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Bureau

- **description** : Poste de travail pour usage informatique ou administratif
- **dimensions standard** :
  - **hauteur plateau mm** :
    - **min** : 700
    - **max** : 750
    - **norme fixe** : 720
    - **ref** : NF EN 527-1
  - **hauteur assis debout mm** :
    - **min** : 650
    - **max** : 1250
  - **profondeur min mm** : 600
  - **profondeur standard mm** :
    - **min** : 700
    - **max** : 800
  - **profondeur direction mm** :
    - **min** : 800
    - **max** : 1000
  - **largeur poste simple mm** :
    - **min** : 1200
    - **max** : 1400
  - **largeur double ecran mm** :
    - **min** : 1400
    - **max** : 1600
  - **largeur direction mm** :
    - **min** : 1600
    - **max** : 2000
  - **ecart assise plateau mm** :
    - **min** : 200
    - **max** : 260
- **ergonomie** :
  - **distance ecran yeux mm** :
    - **min** : 500
    - **max** : 700
  - **position clavier bord mm** :
    - **min** : 100
    - **max** : 150
    - **note** : Distance du bord du plateau
  - **recul chaise arriere mm** :
    - **min** : 800
    - **max** : 1000
  - **passage lateral mm** : 600
  - **deboitement pied min mm** : 600
  - **hauteur libre sous plateau mm** :
    - **min** : 650
    - **norme PMR** : 700
  - **profondeur degagement jambes mm** : 600
- **regles conception** :
  - Hauteur plateau = distance sol-coude fléchi - 3 cm
  - Hauteur fixe 72 cm adaptée à une personne de ~175 cm
  - Profondeur min 60 cm pour un écran, 80 cm pour double écran
  - Prévoir passe-câbles et goulotte si bureau fermé sur 3 côtés
  - Tiroir clavier coulissant : profondeur 45-55 cm, hauteur libre 8-10 cm
- **variantes** :
  - **bureau angle L** :
    - **plateau principal mm** : 120-140
    - **retour mm** : 80-120
    - **profondeur mm** : 60-80
  - **bureau compact** :
    - **largeur mm** : 90-100
    - **profondeur mm** : 45-55
    - **usage** : appoint, laptop
  - **bureau mural rabattable** :
    - **largeur mm** : 90-100
    - **profondeur mm** : 40-50



---

<!-- chunk_id: ergo.meuble.commode | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Commode

- **description** : Commode à tiroirs, chiffonnier, semainier
- **dimensions mm** :
  - **profondeur** :
    - **min** : 450
    - **ideal** : 500
    - **max** : 600
  - **hauteur** :
    - **min** : 750
    - **ideal** : 900
    - **max** : 1250
  - **largeur** :
    - **min** : 800
    - **ideal** : 1000
    - **max** : 1600
- **tiroirs** :
  - **nombre** :
    - **commode basse** :
      - **min** : 3
      - **max** : 6
    - **chiffonnier** :
      - **min** : 5
      - **max** : 8
  - **hauteur facade mm** :
    - **petit linge** :
      - **min** : 120
      - **ideal** : 150
      - **max** : 180
    - **linge plie** :
      - **min** : 180
      - **ideal** : 220
      - **max** : 260
    - **volumineux** :
      - **min** : 260
      - **ideal** : 300
      - **max** : 360
  - **hauteur utile mm** :
    - **petit linge** :
      - **min** : 80
      - **ideal** : 100
      - **max** : 120
    - **linge plie** :
      - **min** : 130
      - **ideal** : 160
      - **max** : 190
    - **volumineux** :
      - **min** : 200
      - **ideal** : 240
      - **max** : 300
  - **profondeur utile mm** :
    - **min** : 350
    - **ideal** : 400
    - **max** : 480
- **chiffonnier** :
  - **largeur mm** :
    - **min** : 400
    - **ideal** : 600
    - **max** : 800
  - **hauteur mm** :
    - **min** : 1000
    - **ideal** : 1200
    - **max** : 1400
- **regles conception** :
  - Profondeur 45-50 cm couvre la plupart des usages sans sur-encombrement
  - Tiroir large > 80 cm : coulisses renforcées et fond plus épais
  - Anti-basculement si plusieurs tiroirs ouverts simultanément
  - Tiroirs hauts en partie basse pour accessibilité visuelle



---

<!-- chunk_id: ergo.meuble.console_entree | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Console entree

- **description** : Console d'entrée, vide-poche, meuble d'appoint étroit
- **hauteur mm** :
  - **min** : 750
  - **ideal** : 800
  - **max** : 900
- **profondeur mm** :
  - **ultra compacte** :
    - **min** : 200
    - **max** : 250
  - **standard** :
    - **min** : 260
    - **ideal** : 300
    - **max** : 350
  - **avec tiroir** :
    - **min** : 300
    - **ideal** : 350
    - **max** : 400
- **largeur mm** :
  - **mini** :
    - **min** : 500
    - **max** : 800
  - **standard** :
    - **min** : 800
    - **ideal** : 1000
    - **max** : 1200
- **tiroir** :
  - **hauteur facade mm** :
    - **min** : 80
    - **ideal** : 100
    - **max** : 140
  - **profondeur utile mm** :
    - **min** : 200
    - **ideal** : 240
- **degagement devant mm** :
  - **min** : 800
  - **ideal** : 900
  - **confort** : 1000
- **regles conception** :
  - En entrée étroite, limiter profondeur à 25 cm si circulation < 90 cm
  - Anti-basculement dès que rapport hauteur/profondeur > 3:1



---

<!-- chunk_id: ergo.meuble.cuisine | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Cuisine

- **description** : Meubles de cuisine : bas, hauts, colonnes, îlot
- **meubles bas** :
  - **hauteur caisson standard mm** : 720
  - **hauteur caisson XL mm** : 790
  - **hauteur caisson maxi mm** : 860
  - **hauteur totale standard mm** :
    - **min** : 850
    - **max** : 950
    - **note** : Caisson + plinthe + plan de travail
  - **profondeur standard mm** : 600
  - **largeurs modules mm** :
    - 150
    - 300
    - 450
    - 600
    - 900
    - 1200
  - **plinthe hauteur mm** :
    - **min** : 100
    - **max** : 150
  - **plinthe retrait mm** :
    - **min** : 30
    - **max** : 50
- **plan de travail** :
  - **hauteur standard mm** :
    - **min** : 900
    - **max** : 950
  - **hauteur tendance mm** : 930
  - **profondeur standard mm** : 600
  - **profondeur ilot mm** :
    - **min** : 700
    - **max** : 800
  - **epaisseur mm** :
    - **min** : 20
    - **max** : 100
  - **debord bar mm** :
    - **min** : 350
    - **note** : Pour assise confortable
  - **regle ergonomique** : Coude fléchi 90° → plan 10-15 cm en dessous
- **meubles hauts** :
  - **hauteurs standard mm** :
    - 360
    - 580
    - 720
    - 940
  - **profondeur mm** :
    - **min** : 300
    - **max** : 400
    - **standard** : 350
  - **distance plan travail mm** :
    - **min** : 500
    - **max** : 600
  - **distance avec hotte mm** :
    - **min** : 650
    - **max** : 700
  - **hauteur max accessible mm** : 1500
  - **note** : Au-delà de 150 cm, usage rare ou marchepied
- **colonnes** :
  - **hauteur mm** :
    - **min** : 2100
    - **max** : 2400
  - **profondeur mm** : 600
- **ilot** :
  - **hauteur mm** :
    - **min** : 900
    - **max** : 950
  - **distance meubles mm** :
    - **min** : 900
    - **ideal** : 1200
  - **hauteur tabouret mm** :
    - **min** : 600
    - **max** : 650
- **distances securite** :
  - **evier plaque mm** :
    - **min** : 600
  - **plaque frigo mm** :
    - **min** : 400
    - **max** : 600
  - **four mur mm** :
    - **min** : 900
    - **max** : 1000
  - **triangle activite cote mm** :
    - **min** : 1200
    - **max** : 2700
  - **triangle activite total mm** :
    - **max** : 6500
  - **passage cuisine table mm** :
    - **min** : 1000
    - **max** : 1200
- **hotte** :
  - **hauteur au dessus gaz mm** : 650
  - **hauteur au dessus induction mm** : 500
- **four encastre** :
  - **hauteur ideale sol mm** : 1000
  - **note** : Ergonomie + sécurité enfants
- **PMR** :
  - **hauteur libre sous plan mm** :
    - **min** : 700
  - **profondeur degagement mm** :
    - **min** : 600
  - **rotation fauteuil diametre mm** : 1500



---

<!-- chunk_id: ergo.meuble.dressing_armoire | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Dressing armoire

- **description** : Armoire, penderie, dressing, placard à vêtements
- **dimensions globales** :
  - **profondeur interieure penderie mm** :
    - **min** : 550
    - **ideal** : 550
    - **note** : Cintre standard = 44-46 cm
  - **profondeur exterieure mm** :
    - **min** : 550
    - **max** : 600
    - **note** : Intérieur + portes + fond
  - **profondeur etageres mm** :
    - **min** : 300
    - **max** : 400
  - **profondeur tiroirs mm** : 400
  - **hauteur standard mm** :
    - **min** : 1800
    - **max** : 2400
- **penderie** :
  - **chemises vestes** :
    - **hauteur mm** :
      - **min** : 1100
      - **max** : 1300
  - **robes manteaux** :
    - **hauteur mm** :
      - **min** : 1600
      - **max** : 1700
  - **double penderie** :
    - **barre haute mm** : 2000
    - **barre basse mm** : 1000
    - **note** : Double la capacité pour vêtements courts
  - **largeur module mm** :
    - **min** : 800
    - **max** : 1200
- **etageres** :
  - **espacement pulls mm** :
    - **min** : 250
    - **max** : 300
  - **espacement pulls hiver mm** :
    - **min** : 350
    - **max** : 400
  - **largeur pile vetements mm** :
    - **min** : 300
    - **max** : 400
  - **hauteur pile max mm** : 500
  - **note** : Pouvoir passer la main au-dessus pour retirer un vêtement sans tout faire tomber
- **tiroirs** :
  - **hauteur lingerie mm** : 100
  - **hauteur chaussettes mm** :
    - **min** : 100
    - **max** : 150
  - **hauteur pulls accessoires mm** :
    - **min** : 200
    - **max** : 300
  - **position ergonomique mm** :
    - **min** : 800
    - **max** : 1200
    - **note** : Zone médiane, sans se baisser
  - **largeur mm** :
    - **min** : 300
    - **max** : 650
- **chaussures** :
  - **paires par metre lineaire** :
    - **min** : 4
    - **max** : 5
  - **hauteur chaussures plates mm** :
    - **min** : 150
    - **max** : 200
  - **hauteur bottes mm** :
    - **min** : 400
    - **max** : 500
  - **profondeur mm** :
    - **min** : 300
    - **max** : 350
- **zones ergonomiques** :
  - **acces quotidien mm** :
    - **min** : 800
    - **max** : 1800
  - **stockage haut mm** :
    - **min** : 1800
    - **max** : 2400
    - **usage** : Saisonnier, valises, couettes
  - **stockage bas mm** :
    - **min** : 0
    - **max** : 400
    - **usage** : Chaussures, tiroirs
- **circulations** :
  - **devant portes battantes mm** :
    - **min** : 900
    - **ideal** : 1000
  - **devant portes coulissantes mm** :
    - **min** : 700
  - **dressing couloir largeur totale mm** :
    - **min** : 1450
    - **max** : 1500
    - **calcul** : 60 profondeur + 90 circulation
  - **dressing face a face mm** :
    - **min** : 2100
    - **max** : 2200
    - **calcul** : 60+90+60
- **regles conception** :
  - Profondeur intérieure min 50 cm pour penderie (cintre = 44-46 cm + marge)
  - Moins de 50 cm intérieur = vêtements qui frottent contre les portes
  - Plus de 60 cm extérieur = rarement justifié, masse visuelle excessive
  - Répartition type : 50-60% penderie, 40-50% étagères+tiroirs
  - Système 32 mm pour réglage par pas de 32 mm des accessoires



---

<!-- chunk_id: ergo.meuble.etagere_murale | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Etagere murale

- **description** : Étagère fixée au mur, sans joues latérales au sol
- **dimensions standard** :
  - **profondeur mm** :
    - **min** : 150
    - **max** : 300
  - **longueur max sans support mm** :
    - **bois massif 20mm** : 600
    - **bois massif 30mm** : 900
    - **particules 19mm** : 500
    - **note** : Au-delà, ajouter une équerre ou un support intermédiaire
  - **epaisseur min mm** : 20
  - **hauteur entre etageres mm** :
    - **min** : 250
    - **max** : 350
- **fixation** :
  - **types** :
    - Équerre visible
    - Équerre cachée
    - Rail invisible
    - Tasseau mural
  - **charge equerre standard kg** :
    - **min** : 15
    - **max** : 30
  - **espacement fixations mm** :
    - **min** : 400
    - **max** : 600
  - **note** : Toujours fixer dans les montants (ossature bois) ou avec chevilles adaptées au support (béton, brique, placo)



---

<!-- chunk_id: ergo.meuble.lit_rangement | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Lit rangement

- **description** : Lit avec rangements intégrés — tiroirs sous lit, coffre, tête de lit
- **hauteur sommier mm** :
  - **min** : 300
  - **ideal** : 350
  - **max** : 450
- **hauteur assise finie mm** :
  - **min** : 450
  - **ideal** : 500
  - **max** : 600
- **tiroirs sous lit** :
  - **hauteur utile mm** :
    - **basse** :
      - **min** : 120
      - **max** : 200
    - **standard** :
      - **min** : 180
      - **ideal** : 220
      - **max** : 280
  - **profondeur utile mm** :
    - **lit 90** :
      - **min** : 500
      - **ideal** : 600
    - **lit 140 160** :
      - **min** : 600
      - **ideal** : 700
  - **largeur utile mm** :
    - **petit** :
      - **min** : 400
      - **ideal** : 500
    - **grand** :
      - **min** : 700
      - **ideal** : 900
  - **recul ouverture mm** :
    - **min** : 600
    - **ideal** : 750
    - **confort** : 900
- **tete de lit** :
  - **hauteur depuis sol mm** :
    - **min** : 900
    - **ideal** : 1050
    - **max** : 1300
  - **epaisseur mm** :
    - **min** : 20
    - **ideal** : 40
    - **max** : 100
  - **niches** :
    - **profondeur mm** :
      - **min** : 120
      - **ideal** : 180
    - **hauteur mm** :
      - **min** : 120
      - **ideal** : 180
- **passages autour lit mm** :
  - **min** : 750
  - **ideal** : 900
- **regles conception** :
  - Lit collé au mur d'un côté = tiroirs condamnés de ce côté
  - Hauteur finie 45-55 cm pour lever/coucher confortable
  - Coffre relevable : débattement vertical suffisant requis
  - Poignées non saillantes sur tiroirs sous lit (chocs tibia)



---

<!-- chunk_id: ergo.meuble.meuble_salle_de_bain | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Meuble salle de bain

- **description** : Meuble vasque, colonne, miroir pour salle de bain
- **dimensions standard** :
  - **meuble vasque** :
    - **hauteur standard mm** :
      - **min** : 800
      - **max** : 900
      - **note** : Dessus de vasque
    - **profondeur mm** :
      - **min** : 400
      - **max** : 550
    - **largeur simple vasque mm** :
      - **min** : 600
      - **max** : 900
    - **largeur double vasque mm** :
      - **min** : 1200
      - **max** : 1500
    - **entre axes double vasque mm** :
      - **min** : 600
  - **colonne** :
    - **hauteur mm** :
      - **min** : 1500
      - **max** : 1900
    - **profondeur mm** :
      - **min** : 250
      - **max** : 350
    - **largeur mm** :
      - **min** : 250
      - **max** : 400
  - **miroir** :
    - **bord inferieur sol mm** :
      - **min** : 1000
      - **max** : 1150
    - **hauteur mm** :
      - **min** : 600
      - **max** : 800
- **contraintes specifiques** :
  - Matériaux résistants à l'humidité obligatoires (contreplaqué marine, MDF hydro, mélaminé P5)
  - Ventilation intérieure du caisson recommandée
  - Normes électriques zones 0/1/2/3 autour des points d'eau
  - Prévoir accès plomberie (fond démontable ou trappe)
  - Piètement surélevé ou suspendu pour nettoyage sol



---

<!-- chunk_id: ergo.meuble.meuble_sous_escalier | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Meuble sous escalier

- **description** : Aménagement sur mesure sous escalier droit ou tournant
- **hauteur min utilisable mm** :
  - **etagere ouverte** : 200
  - **tiroir** : 250
  - **placard portes** : 400
  - **penderie courte** : 1000
- **zonage** :
  - **zone basse mm** :
    - **min** : 200
    - **max** : 600
    - **usages** :
      - chaussures
      - tiroirs
      - rangement saisonnier
  - **zone intermediaire mm** :
    - **min** : 600
    - **max** : 1200
    - **usages** :
      - tiroirs extractibles
      - niches
      - aspirateur
  - **zone haute mm** :
    - **min** : 1200
    - **max** : 2200
    - **usages** :
      - placard
      - penderie
      - bibliothèque
- **formule hauteur** : h(x) = h_depart + x × tan(angle_escalier)
- **regles conception** :
  - Modules indépendants plutôt qu'un seul volume monolithique
  - Tiroirs ou coulissants dans les zones basses (porte battante impraticable sous pente)
  - Faux aplomb si sous-face irrégulière — façades alignées
  - Ne jamais couper limons ou appuis sans validation structurelle
  - Prévoir accès technique si réseaux sous escalier
  - Push-to-open ou profils intégrés en circulation étroite
  - Nez de marche débordant : décaler façades ou cadre de compensation
  - Laisser 5 cm de vide sanitaire contre le mur du fond (ventilation)



---

<!-- chunk_id: ergo.meuble.meuble_tv | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Meuble tv

- **description** : Meuble bas ou suspendu pour téléviseur et équipements multimédia
- **dimensions standard** :
  - **hauteur meuble mm** :
    - **min** : 400
    - **max** : 550
  - **profondeur mm** :
    - **min** : 350
    - **max** : 500
  - **largeur mm** :
    - **min** : 1200
    - **max** : 2000
    - **note** : Selon taille TV, dépasser de 15-20 cm de chaque côté
  - **hauteur centre ecran sol mm** :
    - **min** : 1000
    - **max** : 1200
    - **note** : Yeux à hauteur du centre écran en position assise
- **compartiments** :
  - **hauteur appareils mm** :
    - **min** : 150
    - **max** : 200
    - **note** : Lecteur, console, décodeur
  - **ventilation mm** :
    - **min** : 50
    - **note** : Espace arrière et au-dessus des appareils
  - **passe cables** : oui
  - **profondeur utile min mm** : 350
- **regles conception** :
  - Largeur meuble ≥ largeur TV pour équilibre visuel
  - Prévoir passe-câbles arrière et ventilation
  - Distance TV-spectateur = 1.5 à 2.5× la diagonale de l'écran
  - Si suspendu : fixation dans montants ou rails, charge max du mur à vérifier



---

<!-- chunk_id: ergo.meuble.placard_rangement | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Placard rangement

- **description** : Placard intégré, sous-escalier, sous-pente, niche murale
- **dimensions standard** :
  - **profondeur standard mm** :
    - **min** : 500
    - **max** : 600
  - **profondeur peu profond mm** :
    - **min** : 300
    - **max** : 400
    - **usage** : Couloir, entrée, chaussures
  - **hauteur mm** : s'adapte au plafond ou à la sous-pente
  - **largeur module mm** :
    - **min** : 400
    - **max** : 1200
- **sous pente** :
  - **hauteur min utilisable mm** : 600
  - **note** : En dessous de 60 cm, stockage de type coffre uniquement
  - **astuce** : Meuble en escalier suivant la pente avec étagères dégressives
- **regles conception** :
  - Mesurer le plafond EN PLUSIEURS POINTS (faux aplomb fréquent)
  - Prévoir 5 mm de jeu entre meuble et mur/plafond
  - Portes coulissantes si recul < 80 cm
  - Portes battantes si recul ≥ 90 cm
  - Pour sous-pente : relever la pente au niveau du mur et à 30-50 cm du mur



---

<!-- chunk_id: ergo.meuble.table_salle_a_manger | source: corpus v3 de l'auteur -->

# Ergonomie meuble : Table salle a manger

- **description** : Table de repas — salle à manger, cuisine, séjour
- **hauteur mm** :
  - **standard** : 750
  - **min** : 720
  - **max** : 760
- **epaisseur plateau mm** :
  - **min** : 20
  - **ideal** : 30
  - **max** : 50
- **espace jambes sous plateau mm** :
  - **min** : 600
  - **ideal** : 670
  - **max** : 720
- **retrait pied bord mm** :
  - **min** : 80
  - **ideal** : 120
  - **max** : 200
- **largeur par convive mm** :
  - **min** : 550
  - **ideal** : 600
  - **confort** : 650
- **profondeur par convive mm** :
  - **min** : 350
  - **ideal** : 400
  - **confort** : 450
- **degagement chaise mm** :
  - **chaise rentree** :
    - **min** : 150
    - **ideal** : 200
  - **chaise occupee recul** :
    - **min** : 450
    - **ideal** : 550
    - **confort** : 600
  - **passage derriere chaise occupee** :
    - **min** : 750
    - **ideal** : 900
    - **confort** : 1000
- **dimensions par capacite** :
  - **rectangulaire** :
    - **4 personnes mm** :
      - **longueur** :
        - **min** : 1200
        - **ideal** : 1400
      - **largeur** :
        - **min** : 800
        - **ideal** : 900
    - **6 personnes mm** :
      - **longueur** :
        - **min** : 1600
        - **ideal** : 1800
      - **largeur** :
        - **min** : 900
        - **ideal** : 950
    - **8 personnes mm** :
      - **longueur** :
        - **min** : 2000
        - **ideal** : 2200
      - **largeur** :
        - **min** : 950
        - **ideal** : 1000
    - **10 personnes mm** :
      - **longueur** :
        - **min** : 2400
        - **ideal** : 2800
      - **largeur** :
        - **min** : 1000
        - **ideal** : 1050
    - **12 personnes mm** :
      - **longueur** :
        - **min** : 3000
        - **ideal** : 3200
      - **largeur** :
        - **min** : 1000
        - **ideal** : 1100
  - **ronde diametre mm** :
    - **2 personnes** :
      - **min** : 700
      - **ideal** : 800
    - **4 personnes** :
      - **min** : 900
      - **ideal** : 1000
    - **6 personnes** :
      - **min** : 1200
      - **ideal** : 1300
    - **8 personnes** :
      - **min** : 1450
      - **ideal** : 1500
  - **carree mm** :
    - **2 personnes** :
      - **cote** :
        - **min** : 700
        - **ideal** : 800
    - **4 personnes** :
      - **cote** :
        - **min** : 900
        - **ideal** : 1000
    - **8 personnes** :
      - **cote** :
        - **min** : 1400
        - **ideal** : 1500
- **regles conception** :
  - Prévoir au moins 60 cm de largeur par convive adulte
  - Hauteur libre sous plateau ≥ 60 cm pour les genoux
  - Éviter ceintures ou traverses descendant sous 62 cm de hauteur libre
  - Pour table extensible : même largeur utile sur les allonges que sur le plateau principal
  - Piétement central : cercle libre ~45 cm autour de l'axe pour les pieds



---

<!-- chunk_id: ergo.objets_reference | source: corpus v3 de l'auteur -->

# Ergonomie : dimensions de référence des objets stockés (livres, médias, vêtements, vaisselle, chaussures, jouets)

- **description** : Dimensions de référence des objets courants pour dimensionner les meubles
- **livres** :
  - **poche** :
    - **largeur mm** : 110
    - **hauteur mm** : 180
  - **roman A5** :
    - **largeur mm** : 150
    - **hauteur mm** : 210
  - **BD franco belge** :
    - **largeur mm** : 240
    - **hauteur mm** : 320
  - **BD comic book** :
    - **largeur mm** : 170
    - **hauteur mm** : 260
  - **manga** :
    - **largeur mm** : 130
    - **hauteur mm** : 180
  - **beau livre art** :
    - **largeur mm** :
      - **min** : 250
      - **max** : 350
    - **hauteur mm** :
      - **min** : 300
      - **max** : 400
  - **encyclopedie** :
    - **largeur mm** : 220
    - **hauteur mm** : 300
  - **classeur A4** :
    - **largeur mm** : 280
    - **hauteur mm** : 320
    - **epaisseur mm** : 80
- **medias** :
  - **vinyle 33t** :
    - **cote mm** : 315
  - **vinyle 45t** :
    - **cote mm** : 187
  - **CD** :
    - **hauteur mm** : 125
    - **largeur mm** : 142
  - **DVD** :
    - **hauteur mm** : 192
    - **largeur mm** : 136
  - **bluray** :
    - **hauteur mm** : 171
    - **largeur mm** : 135
- **vetements** :
  - **cintre standard largeur mm** :
    - **min** : 440
    - **max** : 460
  - **tshirt plie hauteur mm** : 30
  - **pull plie hauteur mm** : 120
  - **manteaux par metre lineaire** : 6
  - **chaussures par metre lineaire** :
    - **min** : 4
    - **max** : 5
- **vaisselle** :
  - **assiette plate diametre mm** :
    - **min** : 240
    - **max** : 280
  - **verre hauteur mm** :
    - **min** : 120
    - **max** : 250
  - **bouteille vin hauteur mm** : 320
  - **bouteille vin diametre mm** : 80
- **chaussures** :
  - **sneakers adulte mm** :
    - **longueur** :
      - **min** : 280
      - **max** : 340
    - **largeur** :
      - **min** : 90
      - **max** : 130
    - **hauteur** :
      - **min** : 100
      - **max** : 140
  - **chaussures ville mm** :
    - **longueur** :
      - **min** : 270
      - **max** : 330
    - **largeur** :
      - **min** : 80
      - **max** : 110
    - **hauteur** :
      - **min** : 80
      - **max** : 120
  - **talons femme mm** :
    - **longueur** :
      - **min** : 240
      - **max** : 300
    - **largeur** :
      - **min** : 80
      - **max** : 100
    - **hauteur totale** :
      - **min** : 90
      - **max** : 180
  - **bottines mm** :
    - **longueur** :
      - **min** : 260
      - **max** : 320
    - **largeur** :
      - **min** : 90
      - **max** : 130
    - **hauteur** :
      - **min** : 150
      - **max** : 250
  - **bottes mollet mm** :
    - **longueur** :
      - **min** : 270
      - **max** : 330
    - **largeur** :
      - **min** : 100
      - **max** : 140
    - **hauteur** :
      - **min** : 320
      - **max** : 450
  - **bottes hautes cavalieres mm** :
    - **longueur** :
      - **min** : 280
      - **max** : 340
    - **largeur** :
      - **min** : 100
      - **max** : 140
    - **hauteur** :
      - **min** : 400
      - **max** : 520
  - **compartiments rangement mm** :
    - **etagere standard** :
      - **hauteur** :
        - **min** : 160
        - **ideal** : 200
        - **max** : 220
      - **profondeur** :
        - **min** : 300
        - **ideal** : 350
        - **max** : 380
    - **casier bottes** :
      - **hauteur** :
        - **min** : 400
        - **ideal** : 500
        - **max** : 550
      - **profondeur** :
        - **min** : 350
        - **ideal** : 400
        - **max** : 450
    - **range chaussures incline** :
      - **profondeur** :
        - **min** : 200
        - **ideal** : 240
        - **max** : 280
  - **astuce** : Tablettes inclinées 15-20° avec butée = profondeur réduite de 35 à 30 cm
- **jouets enfant** :
  - **albums jeunesse mm** :
    - **portrait** :
      - **largeur** :
        - **min** : 180
        - **max** : 260
      - **hauteur** :
        - **min** : 240
        - **max** : 340
      - **epaisseur** :
        - **min** : 8
        - **max** : 30
    - **carre** :
      - **cote** :
        - **min** : 180
        - **max** : 260
      - **epaisseur** :
        - **min** : 10
        - **max** : 30
  - **bd romans jeunesse mm** :
    - **largeur** :
      - **min** : 130
      - **max** : 190
    - **hauteur** :
      - **min** : 180
      - **max** : 310
    - **epaisseur** :
      - **min** : 10
      - **max** : 40
  - **boites jeux societe mm** :
    - **petite** :
      - **largeur** : 200
      - **profondeur** : 200
      - **hauteur** : 50
    - **standard** :
      - **largeur** : 300
      - **profondeur** : 300
      - **hauteur** : 70
    - **rectangulaire** :
      - **largeur** : 370
      - **profondeur** : 270
      - **hauteur** : 70
  - **boites puzzle mm** :
    - **petite** :
      - **largeur** : 180
      - **profondeur** : 180
      - **hauteur** : 40
    - **standard** :
      - **largeur** : 260
      - **profondeur** : 190
      - **hauteur** : 50
    - **grande** :
      - **largeur** : 370
      - **profondeur** : 270
      - **hauteur** : 60
  - **briques construction mm** :
    - **petit** :
      - **l** : 200
      - **p** : 150
      - **h** : 70
    - **moyen** :
      - **l** : 260
      - **p** : 190
      - **h** : 90
    - **grand bac** :
      - **l** : 400
      - **p** : 300
      - **h** : 180
  - **peluches mm** :
    - **petite** :
      - **largeur** : 150
      - **profondeur** : 120
      - **hauteur** : 200
    - **moyenne** :
      - **largeur** : 250
      - **profondeur** : 200
      - **hauteur** : 350
    - **grande** :
      - **largeur** : 350
      - **profondeur** : 300
      - **hauteur** : 500
  - **vehicules jouets mm** :
    - **petits** :
      - **l** : 80
      - **p** : 40
      - **h** : 40
    - **moyens** :
      - **l** : 180
      - **p** : 90
      - **h** : 100
    - **grands** :
      - **l** : 300
      - **p** : 150
      - **h** : 180
  - **bacs rangement mm** :
    - **petit** :
      - **l** : 200
      - **p** : 300
      - **h** : 150
    - **standard** :
      - **l** : 300
      - **p** : 400
      - **h** : 200
    - **grand** :
      - **l** : 400
      - **p** : 500
      - **h** : 250
  - **regles rangement** :
    - Albums de face : tablette ou bac avec retenue frontale 4-8 cm
    - Niche standard jeux de société : 33×33×30 cm
    - Niches basses (0-60 cm) : jouets lourds/volumineux
    - Niches intermédiaires : livres fréquemment manipulés



---

<!-- chunk_id: ergo.principes_generaux | source: corpus v3 de l'auteur -->

# Ergonomie : principes généraux (zones de confort, circulations, portée)

- **regle coude** : La hauteur de plan de travail idéale place le plan à 10-15 cm sous le coude fléchi à 90°
- **zone confort vertical** :
  - **zone active** :
    - **min mm** : 400
    - **max mm** : 1400
    - **usage** : Accès quotidien, objets fréquents
  - **zone semi active** :
    - **min mm** : 1400
    - **max mm** : 1800
    - **usage** : Penderie, objets réguliers
  - **zone passive haute** :
    - **min mm** : 1800
    - **max mm** : 2400
    - **usage** : Stockage saisonnier, objets rares
  - **zone passive basse** :
    - **min mm** : 0
    - **max mm** : 400
    - **usage** : Tiroirs, rangement lourd, chaussures
- **circulations** :
  - **passage minimum mm** : 600
  - **passage confortable mm** : 800
  - **recul chaise mm** :
    - **min** : 800
    - **max** : 1000
  - **passage avec circulation mm** :
    - **min** : 900
    - **max** : 1200
  - **espace devant tiroir ouvert mm** : 900
  - **espace devant porte battante mm** : 1000
- **portee tablette** :
  - **regle** : Portée max sans fléchissement = f(matériau, épaisseur, charge)
  - **panneau particules 19mm max mm** : 600
  - **mdf 19mm max mm** : 700
  - **contreplaque 18mm max mm** : 800
  - **bois massif 25mm max mm** : 900
  - **charge max tablette 60cm kg** : 30
  - **charge max tablette 80cm kg** :
    - **bois massif** : 25
    - **panneau particules** : 15
  - **note** : Au-delà, ajouter un support intermédiaire (séparateur vertical ou taquet renforcé)



