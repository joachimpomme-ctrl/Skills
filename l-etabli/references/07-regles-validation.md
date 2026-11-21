# 07-regles-validation

<!-- Corpus menuiserie v3.1.0 — catégorie 07-regles-validation -->

## Sommaire du fichier
- `rules.fleche` — Formule de flèche de tablette (dimensionnement)
- `rules.imperatives` — Règles impératives de validation moteur (12 règles)
- `rules.thresholds` — Seuils numériques métier (anti-bascul., charges, ergonomie)
- `rules.transversales` — Règles transversales (15 règles métier toutes catégories)

---

<!-- chunk_id: rules.fleche | source: corpus v3 de l'auteur + Hamon & Roullat, Dunod 2022 -->

# Formule de flèche de tablette (dimensionnement)

Calcul de la flèche d'une tablette sous charge — fondamental pour le dimensionnement.

## Formule
```
f = (5 · q · L⁴) / (384 · E · I)
```
Avec :
- `f` = flèche en mm
- `q` = charge linéique en N/mm  (charge_kg_par_m × 9.81 / 1000)
- `L` = portée en mm (distance entre appuis)
- `E` = module d'élasticité réel du matériau en MPa (chunk `materiau.mecanique` du fichier 01). L'ancienne règle « flexMPa × 300 » est ABANDONNÉE : elle surestimait la rigidité du MDF ~4× et du mélaminé ~2,5×.
- `I` = moment quadratique en mm⁴

## Moment quadratique d'une tablette rectangulaire
```
I = b · h³ / 12
```
- `b` = largeur (= profondeur tablette en mm)
- `h` = épaisseur tablette en mm

## Fluage : obligatoire dans le verdict
La flèche instantanée n'est pas la flèche finale. Sous charge permanente, le panneau continue de fléchir (EN 1995-1-1 tab. 3.2, classe 1) :
`f_finale = f_inst × (1 + k_def)` avec k_def = 0,6 (massif), 0,8 (CP), 1,5 (OSB/3), 2,25 (MDF et particules).

## Critères admissibles (sur la flèche FINALE)
- **Recommandé meuble** : `f_finale ≤ L / 350` (seuil visuel).
- **Tolérance max** : `f_finale ≤ L / 200`. Au-delà, affaissement net.
Inclure le poids propre de la tablette dans q. Utiliser `scripts/calc.py` pour exécuter le calcul.

## Charges types
- Livres serrés : 30 kg/m linéaire
- Livres normaux / dossiers : 15 kg/m
- Vaisselle : 12-20 kg/m
- Vêtements pliés : 5-8 kg/m
- Décoration : 3-5 kg/m
- Charge par défaut moteur : 8 kg/m

## Exemple (recalculé v4)
Tablette CP bouleau 18 mm × 28 cm de profondeur, portée 80 cm, charge livres 25 kg/m :
- E = 9 000 MPa (retenu, sens du fil) ; k_def = 0,8
- I = 280 × 18³ / 12 = 136 080 mm⁴
- q = 25 × 9,81 / 1000 + poids propre ≈ 0,279 N/mm
- f_inst = (5 × 0,279 × 800⁴) / (384 × 9000 × 136080) ≈ 1,2 mm ; f_finale ≈ 2,2 mm
- Limite recommandée 800 / 350 = 2,3 mm → ✅ admissible (juste)
Contre-exemple : la même tablette en MDF (E = 2 200, k_def = 2,25) donne f_finale ≈ 21 mm → ❌ très largement refusée. L'ancien moteur l'aurait validée.

## Astuces de dimensionnement
- Doubler l'épaisseur multiplie la rigidité par 8 (h³).
- Doubler la portée multiplie la flèche par 16 (L⁴).
- Ajouter un séparateur vertical au milieu divise la portée et donc divise la flèche par 16.



---

<!-- chunk_id: rules.imperatives | source: corpus v3 de l'auteur -->

# Règles impératives de validation moteur (12 règles)

12 règles impératives du moteur de validation (corpus v3 de l'auteur).
Sévérités : `error` (bloquant), `warning`, `suggestion`, `info`.

## RT_004 — Portée tablette
- **Sévérité** : warning
- **Condition** : Longueur d'une tablette > maxSpan18 du matériau (×10 → mm)
- **Message** : Portée trop grande pour le matériau choisi — fléchissement probable.
- **Remédiation** : Ajouter un séparateur vertical, augmenter l'épaisseur ou choisir un matériau plus rigide (CP bouleau).
- **Formule** : `f = (5·q·L⁴) / (384·E·I), I = b·h³/12. Limite admissible f ≤ L/200. Charge q par défaut 8 kg/m.`

## VAL_ROD_DEPTH — Profondeur penderie
- **Sévérité** : warning
- **Condition** : Module penderie présent ET space.depth_mm < 550
- **Message** : Profondeur insuffisante pour une penderie cintres standard.
- **Remédiation** : Augmenter la profondeur à 550 mm OU utiliser une tringle perpendiculaire (pull-out).

## VAL_DOOR_WEIGHT — Poids porte renforcé
- **Sévérité** : warning
- **Condition** : Poids porte calculé > 15 kg
- **Message** : Charnières renforcées nécessaires.
- **Remédiation** : Choisir charnières Ø35 lourdes spéciales (Blum CLIP top BLUMOTION renforcée) ou ajouter une 4e charnière.
- **Formule** : `weight_kg = (length_mm × width_mm × thickness_mm × density) / 1e9`

## VAL_DOOR_WEIGHT_MAX — Poids porte excessif
- **Sévérité** : error (BLOQUANT)
- **Condition** : Poids porte > 25 kg
- **Message** : Trop lourd pour des charnières standard.
- **Remédiation** : Diviser en 2 portes ou réduire les dimensions.

## VAL_ANTI_TIP — Anti-basculement
- **Sévérité** : warning
- **Condition** : space.height_mm > 1500 ET meuble non suspendu ET aucune fixation murale
- **Message** : Risque de basculement — fixation murale manquante.
- **Remédiation** : Ajouter une équerre anti-basculement ou fixer au mur (obligatoire si enfants présents).

## RT_006_LOAD — Charge sur placo (warning)
- **Sévérité** : warning
- **Condition** : Meuble suspendu (étagère murale) ET wall_type = plasterboard ET poids total > 25 kg
- **Message** : Charge importante sur placo — fixation renforcée recommandée.
- **Remédiation** : Utiliser des chevilles Molly ou fixer dans les montants (ossature métallique).
- **Formule** : `totalWeight = Σ(part.length × width × thickness × density × qty) / 1e9`

## RT_006_LOAD_MAX — Charge suspendue excessive
- **Sévérité** : error (BLOQUANT)
- **Condition** : Meuble suspendu ET poids total > 50 kg
- **Message** : Trop lourd pour une fixation murale standard.
- **Remédiation** : Ajouter des pieds (transfert au sol) ou réduire les dimensions.

## ERGO_ZONE_ACTIVE — Zone ergonomique active
- **Sévérité** : info
- **Condition** : Tablettes réglables présentes ET hauteur > 1800 mm
- **Message** : Zone active 400-1400 mm : placez les objets fréquents dans cette zone.
- **Remédiation** : Réorganiser les tablettes pour mettre l'usage quotidien à hauteur de bras.

## RT_009 — Meuble d'entrée encombrant
- **Sévérité** : warning
- **Condition** : type ∈ {vestiaire_entree, meuble_chaussures, banquette_coffre} ET depth > 400
- **Message** : Profondeur > 400 mm — vérifier la circulation (80 cm min).
- **Remédiation** : Réduire la profondeur ou s'assurer du dégagement libre devant.

## RT_013 — Charge cave à vin
- **Sévérité** : warning
- **Condition** : Module wine_rack ET (columns × rows) × 1.3 > 30 kg
- **Message** : Charge bouteilles importante — vérifier la structure porteuse.
- **Remédiation** : Renforcer les tablettes fixes encadrant le casier ou réduire le nombre de bouteilles.
- **Formule** : `weight_kg = bottles × 1.3 (1 bouteille bordelaise pleine ≈ 1.3 kg)`

## RT_010 — Aération chaussures/textiles
- **Sévérité** : suggestion
- **Condition** : type ∈ {meuble_chaussures, banquette_coffre} ET portes présentes
- **Message** : Stockage fermé chaussures/textiles — prévoir des aérations.
- **Remédiation** : Ajouter des grilles de ventilation ou perforations dans le fond / portes.

## VAL_WALL_TYPE_SUSPENDED — Mur inconnu pour suspendu
- **Sévérité** : warning
- **Condition** : Meuble suspendu (rail) ET wall_type = unknown
- **Message** : Type de mur inconnu — fixation potentiellement inadaptée.
- **Remédiation** : Identifier béton/placo/brique pour choisir les chevilles. Placo creux nécessite Molly ou expansion.



---

<!-- chunk_id: rules.thresholds | source: corpus v3 de l'auteur -->

# Seuils numériques métier (anti-bascul., charges, ergonomie)

Seuils numériques utilisés par les règles de validation du moteur. Source : corpus v3 de l'auteur.

| Constante | Valeur | Règle | Source / Justification |
|---|---|---|---|
| `ANTI_TIP_HEIGHT_MM` | 1500 mm | RT_001 / VAL_ANTI_TIP | Au-delà, fixation murale anti-basculement obligatoire (norme sécurité enfants). |
| `WARDROBE_ROD_MIN_DEPTH_MM` | 550 mm | VAL_ROD_DEPTH | Profondeur min pour cintres standard ; en-dessous, tringle perpendiculaire (pull-out). |
| `DOOR_WEIGHT_REINFORCE_KG` | 15 kg | VAL_DOOR_WEIGHT | Au-delà, charnières renforcées nécessaires. |
| `SUSPENDED_PLACO_WARN_KG` | 25 kg | RT_006 | Charge meuble suspendu sur placo : warning, fixation renforcée requise. |
| `SUSPENDED_MAX_KG` | 50 kg | RT_006 | Charge max absolue meuble suspendu, au-delà ajouter pieds. |
| `WINE_RACK_WARN_KG` | 30 kg | RT_013 | Cave à vin >30 kg : vérifier la structure porteuse. |
| `ERGO_ZONE_LOW_MM` | 400 mm | ERGO_ZONE_ACTIVE | Borne basse zone ergonomique active. |
| `ERGO_ZONE_HIGH_MM` | 1400 mm | ERGO_ZONE_ACTIVE | Borne haute zone ergonomique active. |
| `ENTRY_MAX_DEPTH_MM` | 400 mm | RT_009 | Profondeur max meuble d'entrée sans warning circulation (80 cm libre min). |

## Application
Ces valeurs sont la source de vérité pour les règles métier. Elles ont été choisies à partir de :
- Normes industrielles (charnières Ø35, cintres standard).
- Guides ergonomiques (zone active, zone basse/haute).
- Bonnes pratiques DIY (fixation placo, anti-basculement).



---

<!-- chunk_id: rules.transversales | source: corpus v3 de l'auteur -->

# Règles transversales (15 règles métier toutes catégories)

### RT_001 — sévérité critique
**Règle :** Tout meuble > 150cm de hauteur non intégré = anti-basculement obligatoire
**Types concernés :** bibliotheque, armoire, placard, chiffonnier

### RT_002 — sévérité critique
**Règle :** Matériaux résistants à l'humidité obligatoires en pièce humide
**Types concernés :** sdb, cuisine

### RT_003 — sévérité importante
**Règle :** Ventilation obligatoire pour appareils électroniques
**Types concernés :** meuble_tv

### RT_004 — sévérité importante
**Règle :** Vérifier la portée de toute tablette sans support intermédiaire

### RT_005 — sévérité recommandation
**Règle :** Toujours proposer une façade de tiroir rapportée (ajustement post-montage)

### RT_006 — sévérité critique
**Règle :** Meuble suspendu : fond en rainure/feuillure + contreventement obligatoire

### RT_007 — sévérité critique
**Règle :** Sécurité enfant : espacement max entre barreaux 6.5cm (norme NF EN 747)
**Types concernés :** lit_cabane_mezzanine, garde_corps

### RT_008 — sévérité critique
**Règle :** Lit mezzanine : assemblage par boulons traversants M8/M10, jamais vis seules
**Types concernés :** lit_cabane_mezzanine

### RT_009 — sévérité importante
**Règle :** Meuble en entrée : profondeur ≤ 35-40cm pour conserver la circulation (80cm min)
**Types concernés :** vestiaire_entree, meuble_chaussures, banquette_coffre, console_entree

### RT_010 — sévérité importante
**Règle :** Ventilation obligatoire pour stockage chaussures ou textiles en milieu fermé
**Types concernés :** meuble_chaussures, banquette_coffre, placard

### RT_011 — sévérité critique
**Règle :** Sous-escalier : ne jamais modifier la structure porteuse sans validation
**Types concernés :** sous_escalier

### RT_012 — sévérité importante
**Règle :** PMR : hauteur libre sous plan de travail ≥ 70cm, espace rotation Ø150cm
**Types concernés :** cuisine, bureau, sdb

### RT_013 — sévérité importante
**Règle :** Meuble contenant des bouteilles : vérifier charge totale (1 bouteille ≈ 1.3kg)
**Types concernés :** cave_vin, buffet

### RT_014 — sévérité importante
**Règle :** Tiroir enfant : amortisseur obligatoire + anti-pincement
**Types concernés :** commode, lit_cabane_mezzanine

### RT_015 — sévérité critique
**Règle :** Tout meuble à tiroirs multiples : anti-basculement + système anti-ouverture simultanée recommandé
**Types concernés :** commode, chiffonnier, buffet



