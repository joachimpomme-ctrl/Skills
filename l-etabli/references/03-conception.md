# 03-conception

<!-- Corpus menuiserie v3.1.0 — catégorie 03-conception -->

## Sommaire du fichier
- `conception.assemblages_synthese` — Assemblages caisson : synthèse des 7 familles (tourillons, vis, lamelles, confirmats, excentriques, rainure-languette, onglet)
- `conception.calcul_portes` — Conception : Calcul portes
- `conception.calcul_tiroirs` — Conception : Calcul tiroirs
- `conception.chants` — Conception : Chants
- `conception.charge_max_assemblage` — Conception : Charge max assemblage
- `conception.contreventement` — Conception : Contreventement
- `conception.debord_plan_de_travail` — Conception : Debord plan de travail
- `conception.fond_de_caisson` — Conception : Fond de caisson
- `conception.formulas` — Conception : formules de calcul (portes, tiroirs, tablettes)
- `conception.meuble_suspendu` — Conception : Meuble suspendu
- `conception.meubles_angle` — Conception : Meubles angle
- `conception.plinthe_socle` — Conception : Plinthe socle
- `conception.portes_traverses_intermediaires` — Conception : Portes traverses intermediaires
- `conception.regles_conception` — Conception : règles de conception (synthèse)
- `conception.separateurs_verticaux` — Conception : Separateurs verticaux
- `conception.sequence_assemblage` — Conception : Sequence assemblage
- `conception.structure_caisson` — Conception : Structure caisson
- `conception.tablettes` — Conception : Tablettes
- `conception.tiroirs_multiples_empiles` — Conception : Tiroirs multiples empiles
- `conception.tolerances_bricoleur` — Conception : Tolerances bricoleur
- `engine.edge_banding` — Règles de plaquage de chant par type de pièce
- `engine.geometry` — Formules de géométrie : caisson, portes, tiroirs, fond
- `engine.layout` — Agencement automatique : multicorps, portes, zones par défaut

---

<!-- chunk_id: conception.assemblages_synthese | source: Hamon & Roullat, Dunod 2022, p118 -->

# Assemblages caisson : synthèse des 7 familles (tourillons, vis, lamelles, confirmats, excentriques, rainure-languette, onglet)

Familles d'assemblage de caisson en menuiserie panneau (voir Hamon & Roullat, Dunod 2022, p118).

| Famille | Usage | Outillage | Précision requise |
|---|---|---|---|
| Tourillons | Tous panneaux, surtout CP | Perceuse + guide ou colonne, mèche Ø8 | Élevée (alignement perçages) |
| Vis | CP et MDF (PAS dans chants mélaminé) | Perceuse-visseuse, fraise à chanfreiner | Moyenne |
| Lamelles (biscuits) | Tous panneaux | Lamelleuse | Moyenne |
| Confirmats | Mélaminé, MDF dense | Mèche étagée Ø7+Ø5 | Faible (idéal débutant) |
| Excentriques | Mélaminé, montage/démontage | Perceuse, gabarit fabricant | Faible |
| Rainure-languette | CP fin, panneaux à chant à chant | Défonceuse + fraise droite | Élevée |
| Onglet verrouillé | Caissons fins, finition | Scie à onglet + lamelles | Très élevée |

## Règles de choix par matériau
- **CP bouleau / okoumé / peuplier** : tourillons + colle (référence). Vis 4×40 en renfort possible.
- **MDF** : vis + colle obligatoire. Pré-perçage systématique. Ø2 mm dans chants (le MDF se fend).
- **Mélaminé** : excentriques + tourillons. JAMAIS de vis dans les chants.
- **OSB** : vis 4×50 + colle PU pour joints. Pas de tourillons (structure hétérogène).

## Charges admissibles par liaison
- Tourillons Ø8 + colle (paire) : 80-120 kg en cisaillement.
- Vis 4×40 dans CP : 40-60 kg par vis en arrachement.
- Lamelle n°20 + colle : ~80 kg en cisaillement.
- Confirmat 7×50 dans particules : 30-50 kg en arrachement.
- Excentrique : ~25-40 kg, **non comparable** aux liaisons collées (démontable).



---

<!-- chunk_id: conception.calcul_portes | source: corpus v3 de l'auteur -->

# Conception : Calcul portes

- **description** : Formules de calcul des dimensions de portes selon le type de pose
- **jeux standard mm** :
  - **jeu peripherique** :
    - **min** : 1.5
    - **standard** : 2
    - **max** : 3
    - **note** : Jeu entre la porte et le bord du caisson (haut, bas, côté opposé charnière)
  - **jeu entre portes** :
    - **min** : 2
    - **standard** : 3
    - **max** : 5
    - **note** : Jeu entre deux portes adjacentes
  - **jeu porte tiroir** :
    - **min** : 2
    - **standard** : 3
    - **max** : 4
- **porte applique 1 porte** :
  - **description** : 1 porte recouvrant tout le caisson
  - **largeur porte** : largeur_ext_caisson + (2 × recouvrement) - (2 × jeu_peripherique)
  - **recouvrement mm** :
    - **standard** : 16
    - **note** : La porte dépasse de 16mm de chaque côté sur les joues
  - **hauteur porte** : hauteur_ext_caisson + (2 × recouvrement) - (2 × jeu_peripherique)
  - **exemple** :
    - **caisson L mm** : 400
    - **recouvrement mm** : 16
    - **jeu mm** : 2
    - **largeur porte mm** : 400 + 32 - 4 = 428
- **porte applique 2 portes** :
  - **description** : 2 portes sur un même caisson, chacune sur une joue
  - **largeur par porte** : (largeur_ext_caisson + (2 × recouvrement) - jeu_entre_portes) / 2
  - **note** : Chaque porte recouvre sa joue de 'recouvrement' mm et il y a 'jeu_entre_portes' mm entre elles
  - **exemple** :
    - **caisson L mm** : 800
    - **recouvrement mm** : 16
    - **jeu entre mm** : 3
    - **largeur porte mm** : (800 + 32 - 3) / 2 = 414.5
- **porte demi recouvrement** :
  - **description** : Porte sur un montant central partagé entre 2 caissons adjacents
  - **recouvrement par porte mm** : (epaisseur_montant - jeu_entre_portes) / 2
  - **exemple montant 18mm** : recouvrement = (18 - 3) / 2 = 7.5mm par porte
  - **charniere** : Coudure 9mm
- **porte rentrant** :
  - **description** : Porte encastrée dans l'ouverture du caisson
  - **largeur porte** : largeur_interieure_caisson - (2 × jeu_peripherique)
  - **hauteur porte** : hauteur_interieure_caisson - (2 × jeu_peripherique)
  - **jeu mm** :
    - **min** : 2
    - **max** : 3
  - **charniere** : Coudure 16mm
- **position charnieres sur porte mm** :
  - **distance bord sup et inf** :
    - **min** : 60
    - **standard** : 80
    - **max** : 100
  - **centre boitier depuis chant** :
    - **formule** : 17.5 + K
    - **K mm** :
      - **min** : 3
      - **standard** : 4
      - **max** : 7
    - **resultat mm** :
      - **min** : 20.5
      - **standard** : 21.5
      - **max** : 24.5
  - **note** : Charnières intermédiaires réparties régulièrement entre la première et la dernière
- **poids max porte** :
  - **valeurs prudentes avant projet** :
    - 
      - **nb charnieres** : 2
      - **hauteur max mm** : 900
      - **poids max kg** :
        - **prudent** : 5
        - **abaque fabricant** : 8
    - 
      - **nb charnieres** : 3
      - **hauteur max mm** : 1600
      - **poids max kg** :
        - **prudent** : 7
        - **abaque fabricant** : 13
    - 
      - **nb charnieres** : 4
      - **hauteur max mm** : 2000
      - **poids max kg** :
        - **prudent** : 10
        - **abaque fabricant** : 17
    - 
      - **nb charnieres** : 5
      - **hauteur max mm** : 2400
      - **poids max kg** :
        - **prudent** : 13
        - **abaque fabricant** : 22
  - **note** : Valeurs prudentes = avant-projet bricoleur. Abaque fabricant = Blum/Hettich pour largeur ≤ 600mm. Toujours vérifier la doc.



---

<!-- chunk_id: conception.calcul_tiroirs | source: corpus v3 de l'auteur -->

# Conception : Calcul tiroirs

- **description** : Formules de calcul des dimensions de tiroirs avec coulisses latérales
- **facade tiroir** :
  - **applique** :
    - **largeur** : largeur_ext_caisson + (2 × recouvrement) - (2 × jeu_peripherique)
    - **hauteur** : hauteur_ouverture_attribuee + recouvrement_haut + recouvrement_bas - jeu_entre_facades
    - **note** : Même logique que les portes en applique
  - **rentrant** :
    - **largeur** : largeur_interieure_caisson - (2 × jeu_peripherique)
    - **hauteur** : hauteur_ouverture_attribuee - jeu_haut - jeu_bas
  - **jeu entre facades mm** :
    - **min** : 2
    - **standard** : 3
    - **max** : 4
- **caisson tiroir** :
  - **largeur** : largeur_interieure_caisson - (2 × encombrement_coulisse)
  - **encombrement coulisse mm** :
    - **coulisses laterales billes** : 12.7
    - **coulisses sous tiroir invisibles** : variable (ex: Tandem = intérieur - 42mm pour côtés 16mm)
    - **tiroirs metal integres** : 0
    - **note** : 12.7mm UNIQUEMENT pour coulisses latérales à billes. Vérifier la doc fabricant pour tout autre système.
  - **profondeur** : profondeur_interieure_caisson - jeu_arriere (5-10mm)
  - **hauteur cotes mm** :
    - **min** : 60
    - **max** : 200
    - **note** : Selon hauteur utile souhaitée
- **fond tiroir** :
  - **epaisseur mm** :
    - **leger** : 4
    - **standard** : 5
    - **charge** : 8
    - **lourd** : 10
  - **assemblage** :
    - **en rainure** :
      - **position rainure depuis bas mm** :
        - **min** : 8
        - **max** : 10
      - **profondeur rainure mm** :
        - **min** : 5
        - **max** : 6
      - **note** : Le fond glisse dans la rainure des côtés et de la façade intérieure
    - **rapporte sous tiroir** :
      - **description** : Fond vissé ou cloué sous les côtés du tiroir
      - **avantage** : Pas de rainurage nécessaire
      - **inconvenient** : Hauteur utile réduite de l'épaisseur du fond
  - **fixation arriere** : Vis dans trou oblong à l'arrière — permet le mouvement du bois
- **facade rapportee** :
  - **description** : La façade décorative est une pièce séparée, fixée sur le caisson du tiroir après montage des coulisses
  - **methode** :
    - 1. Monter le caisson du tiroir avec les coulisses
    - 2. Positionner la façade avec du scotch double face temporaire
    - 3. Vérifier les jeux et l'alignement
    - 4. Visser depuis l'intérieur du tiroir (2 vis min)
    - 5. Retirer le scotch
  - **avantage** : Permet un ajustement parfait des jeux APRÈS montage



---

<!-- chunk_id: conception.chants | source: corpus v3 de l'auteur -->

# Conception : Chants

- **description** : Finition des tranches visibles des panneaux dérivés
- **types** :
  - **chant thermocollant** :
    - **description** : Bande pré-encollée, application au fer à repasser
    - **epaisseurs mm** :
      - 0.4
      - 0.8
    - **largeurs mm** :
      - 19
      - 22
      - 23
      - 28
      - 33
      - 43
    - **note** : Largeur = épaisseur panneau + 3-4mm (arasé après pose)
    - **application** : Fer à repasser domestique à ~160°C, pression ferme, arasage au coupe-chant
    - **usage** : Bricoleur — solution la plus simple et accessible
  - **chant ABS PVC** :
    - **description** : Bande plastique collée (colle contact ou plaqueuse)
    - **epaisseurs mm** :
      - 0.4
      - 1
      - 2
    - **note** : 1mm et 2mm = finition pro, nécessite plaqueuse de chant
    - **usage** : Professionnel
  - **placage bois** :
    - **description** : Fine feuille de bois véritable (0.5mm) collée
    - **epaisseur mm** : 0.5
    - **usage** : Meubles en contreplaqué — harmoniser le chant avec le parement
- **regles application** :
  - Plaquer les chants AVANT l'assemblage du caisson
  - Chants visibles en priorité : façade du meuble (chant avant des joues, dessus, dessous)
  - Chants intérieurs : nécessaires sur tablettes réglables (toutes les faces visibles)
  - Pas besoin de plaquer le chant arrière si contre un mur
  - Pas besoin de plaquer les chants cachés par une porte
- **ordre plaquage** :
  - 1. Chants transversaux (petits côtés) en premier
  - 2. Chants longitudinaux (grands côtés) ensuite — ils recouvrent les bouts des transversaux
  - → Résultat : les chants longitudinaux (les plus visibles) sont continus



---

<!-- chunk_id: conception.charge_max_assemblage | source: corpus v3 de l'auteur -->

# Conception : Charge max assemblage

- **description** : Ordres de grandeur prudents pour panneaux 16-19mm correctement usinés
- **par liaison** :
  - **tourillons colles** :
    - **charge kg** :
      - **min** : 15
      - **max** : 30
    - **note** : Très résistant au cisaillement. Assemblage définitif.
  - **lamelles collees** :
    - **charge kg** :
      - **min** : 10
      - **max** : 25
    - **note** : Excellent alignement, moins bon en traction directe
  - **vis confirmation** :
    - **charge kg** :
      - **min** : 20
      - **max** : 40
    - **note** : Idéal panneaux dérivés, pré-perçage étagé obligatoire
  - **excentriques goujon** :
    - **charge kg** :
      - **min** : 10
      - **max** : 20
    - **note** : Démontable. Toujours coupler avec tourillons pour alignement
  - **vis bois directe** :
    - **charge kg** :
      - **min** : 8
      - **max** : 18
    - **note** : Dépannage ou petites charges
- **classement** : tourillons collés ≈ vis confirmation > lamelles > excentriques > vis directes
- **note** : La rigidité globale dépend plus du fond et du contreventement que du type d'assemblage seul



---

<!-- chunk_id: conception.contreventement | source: corpus v3 de l'auteur -->

# Conception : Contreventement

- **description** : Rigidité quand le fond seul ne suffit pas
- **seuils surveillance mm** :
  - **largeur** :
    - **surveillance** : 800
    - **renfort** : 1000
  - **hauteur** :
    - **surveillance** : 1200
    - **renfort** : 1800
  - **rapport H L** :
    - **surveillance** : 2
    - **renfort** : 3
- **solutions** :
  - Fond plus épais (8, 10, 12mm)
  - Fond en rainure sur 4 côtés
  - Tablette fixe collée/vissée
  - Séparateur vertical
  - Traverse arrière (H min 60mm, standard 80-120mm)
  - Équerres métal intérieures
  - Cadre arrière (meuble sans fond)
- **regles** :
  - HDF 3mm = petit meuble uniquement. Grand caisson chargé = insuffisant
  - Meuble sans fond = traverses arrière obligatoires (min 1, idéalement 2)
  - Tablette fixe bien liée > tablette réglable pour la rigidité
  - Penser voilement ET flambage des longues joues



---

<!-- chunk_id: conception.debord_plan_de_travail | source: corpus v3 de l'auteur -->

# Conception : Debord plan de travail

- **cuisine** :
  - **avant mm** :
    - **min** : 15
    - **standard** : 20
    - **max** : 30
  - **lateral joue visible mm** :
    - **min** : 10
    - **standard** : 20
    - **max** : 30
  - **arriere mm** :
    - **standard** : 0
    - **vide sanitaire** : 50
- **bureau** :
  - **avant mm** :
    - **min** : 20
    - **standard** : 30
    - **confort** : 40
    - **max** : 60
  - **lateral mm** :
    - **min** : 10
    - **standard** : 20
    - **max** : 40
- **regles** :
  - Débord avant protège les façades des coulures d'eau/liquides
  - Débord trop important sans renfort = fléchissement ou arrachement
  - En bureau, léger débord avant améliore la prise de main



---

<!-- chunk_id: conception.fond_de_caisson | source: corpus v3 de l'auteur -->

# Conception : Fond de caisson

- **description** : Le fond assure le contreventement (équerrage) et la rigidité du caisson
- **types** :
  - **rapporte a plat cul** :
    - **description** : Le fond est cloué/vissé directement sur le chant arrière du caisson
    - **epaisseur mm** :
      - **min** : 3
      - **standard** : 8
      - **charge lourde** : 12
    - **avantages** :
      - Aucun usinage (pas de rainure/feuillure)
      - Profondeur intérieure maximale
      - Le plus rapide
    - **inconvenients** :
      - Chant du fond visible latéralement
      - Interdit si le dessous est visible (meuble suspendu)
    - **fixation** : Pointes sans tête 1.5×25mm, ou vis 3.5×16mm, espacement 15-20cm
    - **usage** : Meubles bas posés contre un mur, caissons non visibles de l'arrière
  - **en rainure** :
    - **description** : Le fond s'insère dans une rainure usinée dans les joues et horizontaux
    - **epaisseur mm** :
      - **standard** : 5
      - **alternatif** : 8
    - **rainure** :
      - **largeur mm** : = épaisseur du fond (5 ou 8mm)
      - **profondeur mm** :
        - **min** : 5
        - **max** : 8
      - **position depuis chant arriere mm** :
        - **min** : 5
        - **max** : 10
        - **standard** : 8
    - **avantages** :
      - Fond invisible des 4 côtés
      - Bon équerrage
      - Guide l'assemblage
    - **inconvenients** :
      - Nécessite rainurage (défonceuse ou scie sur table)
      - Réduit la profondeur utile
    - **regles** :
      - Rainure dans les joues : débouchante (traverse tout le panneau)
      - Rainure dans les horizontaux : arrêtée si le chant est visible, sinon débouchante
      - En cas de rainure arrêtée, finir à la défonceuse ou au ciseau
      - Le fond est assemblé AVANT collage final du caisson (il glisse dans les rainures)
    - **usage** : Meubles visibles des 4 côtés, meubles hauts suspendus
  - **en feuillure** :
    - **description** : Le fond se loge dans une feuillure (entaille en L) usinée dans le chant arrière
    - **epaisseur mm** :
      - **standard** : 8
      - **charge lourde** : 12
    - **feuillure** :
      - **largeur mm** : = épaisseur du fond + 1mm de jeu
      - **profondeur mm** : = épaisseur_panneau / 3 (ex: 6mm pour panneau 18mm)
      - **note** : Règle du tiers : profondeur feuillure = 1/3 de l'épaisseur du montant
    - **avantages** :
      - Fond vissable donc démontable
      - Bon maintien de l'équerrage
      - Profondeur utile quasi maximale
    - **inconvenients** :
      - Chant du fond visible latéralement (fine bande)
      - Usinage requis
    - **fixation** : Vis 3.5×25mm dans la feuillure, espacement 20cm
    - **usage** : Compromis entre 'rapporté' et 'en rainure' — très utilisé en pro
- **materiaux** :
  - **isorel HDF 3mm** :
    - **usage** : Meubles très légers, dos de bibliothèque décoratifs
    - **charge** : très faible
  - **contreplaque 5mm** :
    - **usage** : Usage courant, suffisant pour la plupart des caissons < 80cm de large
    - **charge** : légère
  - **contreplaque 8mm** :
    - **usage** : Standard professionnel, bon équilibre rigidité/poids
    - **charge** : moyenne
  - **melamine 8mm** :
    - **usage** : Quand le fond est visible (intérieur d'un placard)
    - **charge** : moyenne
  - **contreplaque 12mm** :
    - **usage** : Charges lourdes, grands caissons > 100cm
    - **charge** : lourde
- **regles** :
  - Le fond ASSURE l'équerrage : un caisson sans fond n'est pas rigide
  - Pour fond > 80cm de large : ajouter un montant intermédiaire
  - Fond rapporté sans jeu = meilleur équerrage (le fond contraint la géométrie)
  - Pour meuble suspendu : fond en rainure ou feuillure (jamais rapporté vu du dessous)
  - Meuble haut cuisine : fond décollé de 15mm du mur pour système d'accroche (rail)
  - CP 5mm suffisant pour la majorité des usages — 8mm pour la tranquillité d'esprit



---

<!-- chunk_id: conception.formulas | source: corpus v3 de l'auteur -->

# Conception : formules de calcul (portes, tiroirs, tablettes)

## door_width_full_overlay_single
- **ID** : `F_CON_001`
- **Variables** : cabinet_outer_width_mm, overlay_mm, peripheral_gap_mm
- **Formule** : `cabinet_outer_width_mm + 2 * overlay_mm - 2 * peripheral_gap_mm`
- **Sortie** : door_width_mm
- **Paramètres** : - **overlay mm** :
  - **default** : 16
- **peripheral gap mm** :
  - **default** : 2

## door_width_full_overlay_double
- **ID** : `F_CON_002`
- **Variables** : cabinet_outer_width_mm, overlay_mm, gap_between_doors_mm
- **Formule** : `(cabinet_outer_width_mm + 2 * overlay_mm - gap_between_doors_mm) / 2`
- **Sortie** : door_width_mm
- **Paramètres** : - **overlay mm** :
  - **default** : 16
- **gap between doors mm** :
  - **default** : 3

## door_width_inset
- **ID** : `F_CON_003`
- **Variables** : cabinet_inner_width_mm, gap_mm
- **Formule** : `cabinet_inner_width_mm - 2 * gap_mm`
- **Sortie** : door_width_mm
- **Paramètres** : - **gap mm** :
  - **min** : 2
  - **max** : 3
  - **default** : 2

## drawer_box_width
- **ID** : `F_CON_004`
- **Variables** : cabinet_inner_width_mm, slide_clearance_mm
- **Formule** : `cabinet_inner_width_mm - 2 * slide_clearance_mm`
- **Sortie** : drawer_box_width_mm
- **Paramètres** : - **slide clearance mm** :
  - **default** : 12.7

## drawer_box_depth
- **ID** : `F_CON_005`
- **Variables** : cabinet_inner_depth_mm, rear_gap_mm
- **Formule** : `cabinet_inner_depth_mm - rear_gap_mm`
- **Sortie** : drawer_box_depth_mm
- **Paramètres** : - **rear gap mm** :
  - **min** : 5
  - **max** : 10
  - **default** : 8

## rebate_depth_for_back
- **ID** : `F_CON_006`
- **Variables** : panel_thickness_mm
- **Formule** : `Math.round(panel_thickness_mm / 3)`
- **Sortie** : rebate_depth_mm

## half_overlay_per_door
- **ID** : `F_CON_007`
- **Variables** : divider_thickness_mm, gap_between_doors_mm
- **Formule** : `(divider_thickness_mm - gap_between_doors_mm) / 2`
- **Sortie** : overlay_per_door_mm

## door_height_by_zone
- **ID** : `F_CON_008`
- **Variables** : zone_height_mm, overlay_top_mm, overlay_bottom_mm, gap_top_mm, gap_bottom_mm
- **Formule** : `zone_height_mm + overlay_top_mm + overlay_bottom_mm - gap_top_mm - gap_bottom_mm`
- **Sortie** : door_height_mm
- **Paramètres** : - **overlay top mm** :
  - **default** : 16
- **overlay bottom mm** :
  - **default** : 16
- **gap top mm** :
  - **default** : 2
- **gap bottom mm** :
  - **default** : 2

## adjustable_shelf_count
- **ID** : `F_CON_009`
- **Variables** : available_height_mm, fixed_shelf_height_mm, spacing_mm
- **Formule** : `Math.floor((available_height_mm - fixed_shelf_height_mm) / spacing_mm) - 1`
- **Sortie** : num_adjustable_shelves

## system_32_first_hole
- **ID** : `F_CON_010`
- **Formule** : `37`
- **Sortie** : first_hole_x_from_front_edge_mm
- **Note** : Horizontal distance of the drilling row from front edge. Vertical positions follow F_QUI_005.



---

<!-- chunk_id: conception.meuble_suspendu | source: corpus v3 de l'auteur -->

# Conception : Meuble suspendu

- **charges** :
  - **formule** : charge_totale = (poids_vide + contenu + portes_tiroirs) × coefficient_securite
  - **coefficient securite** :
    - **min** : 2
    - **standard** : 2.5
    - **max** : 3
- **fixations** :
  - **position** : Au plus haut possible, zone supérieure arrière
  - **ecartement lateral mm** :
    - **min** : 50
    - **standard** : 80
    - **max** : 120
  - **nombre min** : 2
  - **ajout 3e point largeur mm** : 800
  - **charge par fixation kg** :
    - **maconnerie pleine** :
      - **min** : 20
      - **standard** : 30
      - **max** : 50
    - **support creux** : valider selon cheville et notice fabricant
- **boitiers suspension** :
  - **charge max par boitier kg** : 65
  - **positionnement** : Dans les joues latérales supérieures, JAMAIS dans la tablette du dessus
- **construction** :
  - **fond** :
    - rainure
    - feuillure
    - panneau épais
    - traverse arrière haute
  - **contreventement obligatoire** : oui
- **regles** :
  - Fond mince décoratif ≠ support de fixation
  - Reporter les efforts dans les joues et le dessus via ferrures/traverses
  - Installer ferrures et renforts arrière AVANT la pose au mur



---

<!-- chunk_id: conception.meubles_angle | source: corpus v3 de l'auteur -->

# Conception : Meubles angle

- **description** : Contraintes spécifiques aux caissons d'angle
- **types** :
  - **caisson en L** :
    - **portes** : Grand angle (155-170°) + bi-fold (60°) pour portes pliantes
    - **regles** :
      - Point de reprise rigide à l'angle intérieur
      - Ferrure d'accès pour volumes profonds
  - **caisson biaise 45** :
    - **regles** :
      - Coupe précise obligatoire
      - Gabarits de montage pour maintenir l'angle
  - **jonction deux caissons** :
    - **fileur angle mm** :
      - **min** : 50
      - **standard** : 65
    - **justification fileur** : Empêche les poignées du meuble adjacent de bloquer l'ouverture
    - **liaison** : Vis de liaison Ø6-7mm, L30-50mm entre caissons
- **regles** :
  - Faux équerrage du local se cumule avec celui du meuble → prévoir fileurs et jeux de pose
  - Volume arrière inaccessible sans ferrure → scinder le meuble ou ajouter panier tournant
  - Ne pas placer les assemblages les plus faibles au sommet de l'angle (zone de torsion)



---

<!-- chunk_id: conception.plinthe_socle | source: corpus v3 de l'auteur -->

# Conception : Plinthe socle

- **description** : Base du meuble posé au sol
- **hauteur standard mm** :
  - **min** : 80
  - **standard** : 100
  - **cuisine** : 100
  - **max** : 150
- **retrait mm** :
  - **min** : 30
  - **standard** : 40
  - **max** : 50
- **types** :
  - **socle rapporte** :
    - **description** : Cadre en panneau fixé sous le caisson
    - **avantage** : Renforce la base, permet de compenser les inégalités du sol
  - **pieds reglables avec bandeau** :
    - **description** : Pieds à vérin + bandeau clipsé en façade
    - **avantage** : Réglage de niveau, accès sous le meuble pour nettoyage
    - **usage** : Standard cuisine et salle de bain
  - **plinthe integree** :
    - **description** : Les joues descendent jusqu'au sol avec un retrait en façade
    - **avantage** : Esthétique épurée
    - **inconvenient** : Pas de réglage, nécessite sol parfaitement plan



---

<!-- chunk_id: conception.portes_traverses_intermediaires | source: corpus v3 de l'auteur -->

# Conception : Portes traverses intermediaires

- **description** : Deux portes superposées séparées par une tablette fixe
- **cas** :
  - **traverse visible** :
    - **description** : La traverse apparaît entre les deux portes (style traditionnel)
    - **H porte haute** : H_ouverture_haute - J_haut - J_bas
    - **H porte basse** : H_ouverture_basse - J_haut - J_bas
  - **traverse cachee applique** :
    - **description** : Les portes recouvrent les chants de la traverse (style moderne)
    - **H porte haute** : H_zone_haute + R_haut + R_bas - J_haut - J_entre
    - **H porte basse** : H_zone_basse + R_haut + R_bas - J_entre - J_bas
    - **recouvrement sur tablette 18mm** : 7.5mm par porte (moitié épaisseur - demi-jeu)
- **jeu entre portes mm** :
  - **min** : 2
  - **standard** : 3
  - **max** : 4
- **regles** :
  - Chaque porte est traitée indépendamment pour le nombre de charnières
  - Traverse structurelle obligatoire si largeur > 600-800mm
  - Même logique de jeux sur toute la façade pour cohérence visuelle



---

<!-- chunk_id: conception.regles_conception | source: corpus v3 de l'auteur -->

# Conception : règles de conception (synthèse)

### RC_001
**Règle :** Toujours dessiner la FAÇADE d'abord (portes/tiroirs), puis implanter les montants/joues derrière
**Source :** Bonbonveronbi — L'Air du Bois
**Impact :** Évite les erreurs de recouvrement et de jeux

### RC_002
**Règle :** Jeu standard = 2-3 mm partout (autour des portes, entre portes, entre tiroirs)
**Source :** Pratique courante menuisiers

### RC_003
**Règle :** Régler le meuble de niveau AVANT de monter les portes
**Source :** L'Air du Bois
**Impact :** Sinon les réglages de charnières ne suffisent pas

### RC_004
**Règle :** Un caisson sans fond n'est pas un meuble — le fond assure l'équerrage
**Source :** Principe fondamental de menuiserie

### RC_005
**Règle :** Pour un montant intermédiaire recevant des charnières : largeur min 70 mm
**Source :** Système 32 (37mm embase + 32mm entraxe + marge)

### RC_006
**Règle :** Portée max d'une tablette = fonction du matériau, de la charge et du fluage (à 25 kg/m : ~38 cm mélaminé, ~42 cm MDF, ~83 cm CP bouleau, 18 mm ; voir `materiau.mecanique` et `scripts/calc.py`, 90cm massif 25mm)
**Source :** Domaine 1 — Ergonomie

### RC_007
**Règle :** Privilégier la façade de tiroir rapportée (vis depuis l'intérieur) pour un ajustement parfait des jeux
**Source :** Pratique professionnelle

### RC_008
**Règle :** En cas de doute sur l'épaisseur du fond : 8mm CP = le standard pro qui marche pour tout
**Source :** Consensus L'Air du Bois



---

<!-- chunk_id: conception.separateurs_verticaux | source: corpus v3 de l'auteur -->

# Conception : Separateurs verticaux

- **description** : Cloisons verticales divisant un caisson en compartiments
- **epaisseur mm** :
  - **standard** : 18
  - **fin** : 12
- **assemblage** : Tourillons, lamelles ou vis confirmation dans les tablettes fixes/dessus/dessous
- **impact portes** : Un séparateur crée un montant central → charnières en demi-recouvrement
- **largeur min montant mm** : 70
- **note** : Largeur min 70mm pour pouvoir fixer une embase de charnière (37mm + marge)



---

<!-- chunk_id: conception.sequence_assemblage | source: corpus v3 de l'auteur -->

# Conception : Sequence assemblage

- **description** : Ordre recommandé pour assembler un caisson complet
- **etapes** :
  - ordre: 1 · action: Contrôler toutes les pièces · details: Cotes, équerrage, faces vues, chants à plaquer
  - ordre: 2 · action: Usiner avant montage · details: Rainures fond, perçages sys32, perçages charnières, pré-perçages assemblage
  - ordre: 3 · action: Plaquer les chants · details: AVANT assemblage. Petits chants d'abord, grands chants ensuite
  - ordre: 4 · action: Montage à blanc · details: Vérifier diagonales, jeux, fond et tablettes fixes
  - ordre: 5 · action: Assembler la structure · details: Joues + dessus + dessous + séparateurs/tablettes fixes
  - ordre: 6 · action: Poser le fond · details: Équerrer sur le fond. Contrôler diagonales AVANT fixation définitive
  - ordre: 7 · action: Socle, traverses, renforts
  - ordre: 8 · action: Quincaillerie intérieure · details: Coulisses, embases charnières, taquets, ferrures de suspension
  - ordre: 9 · action: Mise de niveau et fixation · details: Réglage pieds, fixation murale, liaison entre caissons
  - ordre: 10 · action: Monter portes et tiroirs · details: Régler jeux et alignement
  - ordre: 11 · action: Fixer façades rapportées tiroirs · details: Scotch double-face temporaire → ajuster → visser depuis l'intérieur
  - ordre: 12 · action: Contrôle final · details: Ouverture/fermeture, affleurements, serrage final, anti-basculement
- **regles cles** :
  - Ne JAMAIS fixer les façades tiroirs avant que le meuble soit de niveau et les coulisses réglées
  - Le fond sert d'outil d'équerrage → le poser avant de considérer le caisson comme figé
  - Meuble suspendu : installer ferrures arrière AVANT la pose au mur



---

<!-- chunk_id: conception.structure_caisson | source: corpus v3 de l'auteur -->

# Conception : Structure caisson

- **description** : Un caisson est composé de : 2 joues (côtés verticaux), 1 dessus, 1 dessous, 1 fond, + éventuellement séparateurs, tablettes, bandeaux
- **formes assemblage** :
  - **forme 1 dessous prioritaire** :
    - **description** : Le dessus et le dessous passent ENTRE les joues (joues prioritaires sur les horizontaux)
    - **avantages** :
      - Chants des joues cachés en vue de face
      - Facilite le perçage système 32 (tous les montants ont la même longueur)
    - **inconvenients** :
      - Chant du dessous visible en vue latérale → nécessite joue d'habillage ou plaquage de chant
    - **usage** : Forme la plus courante en agencement et cuisine
  - **forme 2 joues entre horizontaux** :
    - **description** : Les joues sont posées SUR le dessous et SOUS le dessus (horizontaux prioritaires)
    - **avantages** :
      - Meilleure reprise de charge sur les pieds
      - Pas de chant horizontal visible latéralement
    - **inconvenients** :
      - Perçage système 32 décalé si montants intermédiaires
    - **usage** : Bibliothèques, meubles visibles des 4 côtés
- **dimensions calcul** :
  - **hauteur interieure** :
    - **joues prioritaires** : H_int = H_ext - épaisseur_dessus - épaisseur_dessous
    - **horizontaux prioritaires** : H_int = H_ext - 0 (les joues sont ENTRE les horizontaux, pas de perte de hauteur interne)
    - **note** : En forme 1 (joues prioritaires), les horizontaux s'inscrivent entre les joues et n'ajoutent pas à la hauteur extérieure
  - **largeur interieure** : largeur_exterieure - (2 × epaisseur_panneau)
  - **profondeur interieure** : profondeur_exterieure - epaisseur_fond (si fond en rainure/feuillure, sinon = profondeur ext.)
- **joue habillage** :
  - **description** : Panneau décoratif rapporté sur le côté visible du caisson
  - **epaisseur mm** :
    - **min** : 3
    - **max** : 19
  - **avantages** :
    - Cache les chants, vis, usinages
    - Permet de visser le caisson sans se soucier de l'esthétique
    - Crée un vide sanitaire contre le mur
  - **regle** : La joue d'habillage vient au nu (affleurante) avec la face avant des portes
- **fileur** :
  - **description** : Pièce verticale entre le caisson et un mur, ou entre deux caissons
  - **largeur mm** :
    - **min** : 20
    - **max** : 50
    - **standard** : 30
  - **usage** : Compensation des faux équerrages, protection contre les murs irréguliers, facilite le montage



---

<!-- chunk_id: conception.tablettes | source: corpus v3 de l'auteur -->

# Conception : Tablettes

- **fixes** :
  - **description** : Assemblées au caisson par tourillons, lamelles, vis ou rainure
  - **role** : Structure (reprise de charge, anti-flambage des joues), séparation de zones
  - **dimensions** : largeur = largeur_interieure_caisson (joue à joue), profondeur = profondeur caisson - épaisseur fond
  - **regles** :
    - Au moins 1 tablette fixe en haut et 1 en bas du caisson pour la rigidité
    - Tablette fixe obligatoire si portée joue > 80cm (anti-flambage)
    - Assemblage par tourillons Ø8mm ou lamelles n°20 + colle
- **reglables** :
  - **description** : Posées sur taquets, repositionnables
  - **dimensions** : largeur = largeur_interieure - 2mm de jeu total, profondeur = profondeur intérieure - 2mm
  - **jeu mm** : 1
  - **percage systeme 32** :
    - **entraxe mm** : 32
    - **distance chant avant mm** : 37
    - **diametre mm** : 5
    - **profondeur mm** :
      - **min** : 10
      - **max** : 13



---

<!-- chunk_id: conception.tiroirs_multiples_empiles | source: corpus v3 de l'auteur -->

# Conception : Tiroirs multiples empiles

- **description** : Règles pour plusieurs tiroirs superposés dans une même travée
- **jeux mm** :
  - **entre facades** :
    - **min** : 2
    - **standard** : 3
    - **max** : 4
  - **peripherie haut bas** :
    - **min** : 2
    - **standard** : 3
    - **max** : 4
- **formules** :
  - **somme hauteurs facades** : H_zone - J_haut - J_bas - ((N-1) × J_entre)
  - **hauteur facade egale** : (H_zone - J_haut - J_bas - ((N-1) × J_entre)) / N
  - **hauteur derniere par reste** : H_zone - J_haut - J_bas - ((N-1) × J_entre) - somme_autres
- **repartition** :
  - **egales** : Esthétique régulière, commodes minimalistes
  - **progressive** :
    - **regle** : Augmenter du haut vers le bas
    - **pas mm** :
      - **min** : 20
      - **standard** : 32
      - **max** : 64
    - **usage** : Bas plus volumineux (linge, dossiers, casseroles)
  - **fonctionnelle** :
    - **hauteurs utiles mm** :
      - **petit objet** :
        - **min** : 60
        - **standard** : 80
        - **max** : 120
      - **linge plie** :
        - **min** : 120
        - **standard** : 160
        - **max** : 220
      - **casserolier dossiers** :
        - **min** : 180
        - **standard** : 250
        - **max** : 320
- **regles** :
  - Répartir les jeux AVANT de figer les hauteurs de façade
  - Façade la plus haute en bas
  - Ne pas compenser un défaut de coupe en variant les jeux — corriger la géométrie
  - Avec façade rapportée : poser et régler les caissons tiroirs AVANT de fixer les façades
- **exemple mm** :
  - **zone totale** : 716
  - **nb facades** : 4
  - **J haut** : 2
  - **J bas** : 2
  - **J entre** : 3
  - **somme facades** : 703
  - **repartition progressive** :
    - 131
    - 163
    - 195
    - 214



---

<!-- chunk_id: conception.tolerances_bricoleur | source: corpus v3 de l'auteur -->

# Conception : Tolerances bricoleur

- **coupe panneaux mm** :
  - **outils manuels guide** : ±1.5 à ±2
  - **electroportatif guide fiable** : ±0.5 à ±1
  - **atelier bien regle** : ±0.2 à ±0.5
- **percage mm** :
  - **charnieres coulisses** : ±0.5 (compensable par réglage 3D)
  - **systeme 32** : ±0.5
- **equerrage diagonales mm** :
  - **petit caisson** :
    - **max** : 1
  - **caisson courant** :
    - **max** : 2
  - **grand caisson** :
    - **max** : 3
- **jeux recommandes mm** :
  - **precision moyenne** : 3
  - **precision elevee** : 2
- **regles** :
  - Plus l'outillage est simple → jeux visibles plus généreux
  - 3mm de jeu souvent plus propre que 2mm si la coupe n'est pas excellente
  - Ne pas viser 1.5mm de jeu sans process de coupe très répétable



---

<!-- chunk_id: engine.edge_banding | source: corpus v3 de l'auteur -->

# Règles de plaquage de chant par type de pièce

Règles de plaquage de chant appliquées automatiquement selon le **type de pièce**. Un chant n'est plaqué que s'il est visible en utilisation.

| Type de pièce | Chants à plaquer |
|---|---|
| Joue | avant |
| Dessus | avant |
| Dessous | avant |
| Tablette fixe | avant |
| Tablette réglable | avant |
| Tablette inclinée | avant |
| Taquet d'arrêt | avant |
| **Porte** | avant, arrière, gauche, droite (4 chants) |
| **Façade de tiroir** | avant, arrière, gauche, droite (4 chants) |
| Assise (banquette) | avant |
| Devant de coffre | avant, gauche, droite |
| Fond | aucun |
| Croisillon (h/v) | aucun |
| Caisson de tiroir | aucun |
| Fond de tiroir | aucun |

## Longueur de chant à commander
Somme par côté plaqué :
- chant **avant** ou **arrière** → longueur de la pièce
- chant **gauche** ou **droite** → largeur de la pièce

Principe : les **façades visibles** (portes, façades de tiroir) sont plaquées sur les 4 chants ; les pièces **structurelles** ne reçoivent un chant que sur leur arête avant visible ; les pièces **cachées** (fonds, caissons, croisillons) ne sont pas plaquées.



---

<!-- chunk_id: engine.geometry | source: corpus v3 de l'auteur -->

# Formules de géométrie : caisson, portes, tiroirs, fond

Formules de dimensionnement utilisées par le générateur de pièces. Toutes cotes en mm.

## Dimensions intérieures
- **Largeur intérieure** = largeur_extérieure − 2 × épaisseur_panneau
- **Hauteur intérieure** = hauteur_extérieure − 2 × épaisseur_panneau

## Largeur des portes (selon la pose)
- **Recouvrement total, 1 porte** : `l = largeur_ext + 2×overlay − 2×jeu`
- **Recouvrement total, 2 portes** : `l = (largeur_ext + 2×overlay − jeu_entre) / 2`
- **Demi-recouvrement, 2 portes** (montant central) : `l = (largeur_int − jeu_entre) / 2 + demi_overlay`
- **Affleurante (inset)** : `l = largeur_int − 2×jeu`

## Hauteur de porte
`h = hauteur_zone + overlay_haut + overlay_bas − jeu_haut − jeu_bas`

## Caisson de tiroir
- **Largeur caisson** = largeur_int − 2 × jeu_coulisse (13 mm)
- **Profondeur caisson** = (profondeur − épaisseur_fond) − recul_fond (20 mm)
- **Hauteur caisson** = 0,75 × hauteur de la façade
- Côtés de caisson en **12 mm**, fond de tiroir en **5 mm**

## Hauteurs de façades de tiroir — répartition progressive
Plus petit en haut, chaque tiroir plus haut de `pas` :
```
H_utile = H_zone − (jeu_haut + jeu_bas + jeu_entre × (n − 1))
base    = (H_utile − pas × n × (n − 1) / 2) / n
h_i     = base + i × pas        (i = 0 … n−1)
```
**Exemple** : zone 900 mm, 3 tiroirs, jeux 2/2/3, pas 32 mm
→ H_utile = 900 − (2 + 2 + 3×2) = 890 ; base = (890 − 96) / 3 ≈ 265
→ façades ≈ **265, 297, 329 mm** (haut → bas).
Distribution `equal` = même calcul avec `pas = 0` (façades égales).

## Fond de caisson (panneau arrière)
- Logé **en rainure** : dimensions = **largeur_int × hauteur_int** (rainure profondeur 8 mm de chaque côté).
- En **feuillure** ou **applique** : largeur_int × hauteur_int.

## Tablettes
- Longueur = largeur intérieure
- Profondeur tablette = profondeur du caisson − épaisseur du fond

## Valeurs par défaut du moteur
| Paramètre | Valeur |
|---|---|
| Recouvrement (overlay) | 2 mm |
| Jeu périphérique porte | 2 mm |
| Jeu entre portes / tiroirs | 3 mm |
| Jeu latéral coulisse (par côté) | 13 mm (12,7 arrondi) |
| Recul du fond (câbles) | 20 mm |
| Profondeur de rainure du fond | 8 mm |
| Épaisseur côté de tiroir | 12 mm |
| Épaisseur fond de tiroir | 5 mm |
| Ratio hauteur caisson / façade | 0,75 |
| Pas progressif (défaut module) | 32 mm |
| Pas progressif (repli moteur) | 20 mm |



---

<!-- chunk_id: engine.layout | source: corpus v3 de l'auteur -->

# Agencement automatique : multicorps, portes, zones par défaut

Règles d'agencement automatique appliquées pour transformer une intention de projet en disposition concrète.

## Découpe en plusieurs corps (multicorps)
- **Largeur max d'un corps** = `maxSpan18(cm) × 10 + 2 × épaisseur` (la portée max du matériau + les deux joues).
- Si la largeur demandée dépasse ce maximum → `⌈largeur / max⌉` corps de **largeurs égales** (répartition proportionnelle, minimum 10 mm par corps).
- Exemple : 2400 mm en mélaminé chargé livres (portée ~38 cm → max corps ≈ 416 mm) → 6 corps ; en usage léger 10 kg/m (portée ~49 cm) → 5 corps.

## Portes (automatiques pour placard, armoire, cuisine, meuble de salle de bain)
- Largeur de corps **≤ 500 mm** → **1 porte**, recouvrement total.
- Largeur **> 500 mm** → **2 portes**, demi-recouvrement (montant central implicite).
- Un `door_override` explicite force (true) ou supprime (false) les portes.

## Zones par défaut (si l'utilisateur n'en définit pas)
| Type de meuble | Zones générées |
|---|---|
| Bibliothèque / étagère murale | étagères réglables ×4, espacement 300 mm |
| Placard / armoire / vestiaire | penderie courte (60 % de la hauteur) + tiroirs ou étagères (40 %) |
| Commode | bloc tiroirs, répartition progressive |
| Meuble à chaussures | range-chaussures incliné, 4 niveaux |
| Meuble TV | niche multimédia ventilée |
| Cave à vin | casier 4 × 4 |
| Banquette coffre | coffre |
| (défaut) | étagères réglables ×4 |

> Répartition penderie/rangement : `hauteur_tringle = round(hauteur × 0,6)`, le reste pour les tiroirs/étagères.

## Validation des zones
- Profondeur de la zone **< profondeur minimale du module** → **erreur bloquante**.
- Hauteur de zone < minimum recommandé du module → **avertissement**.
- Contraintes propres au module (expressions, ex. `zone_width_mm > 800 && material == 'melamine'`) évaluées et remontées.
- **Incompatibilités** entre modules d'une même zone (ex. banquette coffre incompatible avec penderie) → erreur bloquante.



