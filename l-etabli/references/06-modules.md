# 06-modules

<!-- Corpus menuiserie v3.1.0 — catégorie 06-modules -->

## Sommaire du fichier
- `module.bench_storage` — Module : 🪑 Banquette coffre
- `module.drawer_stack` — Module : 🗃️ Bloc tiroirs
- `module.hanging_rod_long` — Module : 🧥 Penderie longue (manteaux/robes)
- `module.hanging_rod_short` — Module : 👔 Penderie courte (chemises/vestes)
- `module.shelf_adjustable` — Module : 📚 Étagères réglables
- `module.shoe_rack_inclined` — Module : 👟 Range-chaussures incliné
- `module.tv_niche` — Module : 📺 Niche multimédia (TV)
- `module.wine_rack` — Module : 🍷 Casier à bouteilles

---

<!-- chunk_id: module.bench_storage | source: corpus v3 de l'auteur -->

# Module : 🪑 Banquette coffre

Banquette d'entrée avec coffre intégré. Couvercle relevé par charnière piano + vérin à gaz. Hauteur d'assise idéale : 420-480 mm.

## Paramètres configurables
| Nom | Type | Description | Plage |
|---|---|---|---|
| `has_backrest` | boolean | Dossier | défaut false |

## Pièces produites
`assise`, `coffre-fond`, `coffre-cotes`

## Quincaillerie produite
vérin à gaz, charnière piano

## Impact structurel
- Tablette fixe au-dessus requise : non
- Tablette fixe en-dessous requise : non
- Fond requis : oui
- Séparateur vertical requis : non
- Profondeur min : 400 mm
- Affecte la charge structurelle : oui
- **Incompatibilités** : hanging_rod_short, hanging_rod_long

## Contraintes de validation
- **warning** : Hauteur d'assise hors plage 420-480 mm : ergonomie inadaptée.



---

<!-- chunk_id: module.drawer_stack | source: corpus v3 de l'auteur -->

# Module : 🗃️ Bloc tiroirs

Bloc empilé de tiroirs entre deux tablettes fixes. Distribution progressive = tiroir du bas plus haut (pour grands ustensiles), du haut plus bas (couverts).

## Paramètres configurables
| Nom | Type | Description | Plage |
|---|---|---|---|
| `count` | integer | Nombre de tiroirs | 1-6, défaut 3 |
| `distribution` | enum | Répartition des hauteurs | equal | progressive | custom (défaut: progressive) |
| `progressive_step_mm` | integer | Pas progressif (si distribution=progressive) | défaut 32 mm |

## Pièces produites
`tiroir-facade`, `tiroir-caisson`, `tiroir-fond`

## Quincaillerie produite
coulisses billes sortie totale, poignées

## Impact structurel
- Tablette fixe au-dessus requise : oui
- Tablette fixe en-dessous requise : oui
- Fond requis : oui
- Séparateur vertical requis : non
- Profondeur min : 300 mm
- Affecte la charge structurelle : oui
- **Dépendances** : coulisses latérales ou invisibles

## Contraintes de validation
- **warning** : Tiroirs > 800 mm de large : coulisses renforcées recommandées.



---

<!-- chunk_id: module.hanging_rod_long | source: corpus v3 de l'auteur -->

# Module : 🧥 Penderie longue (manteaux/robes)

Tringle pour manteaux, robes longues, pantalons sur cintre. Hauteur min 1600 mm sous tringle.

## Paramètres configurables
_(aucun paramètre)_

## Pièces produites
_(aucune)_

## Quincaillerie produite
supports tringle Ø25, tringle chromée Ø25

## Impact structurel
- Tablette fixe au-dessus requise : oui
- Tablette fixe en-dessous requise : non
- Fond requis : non
- Séparateur vertical requis : non
- Profondeur min : 550 mm
- Hauteur min : 1600 mm
- Affecte la charge structurelle : oui

## Contraintes de validation
_(aucune)_



---

<!-- chunk_id: module.hanging_rod_short | source: corpus v3 de l'auteur -->

# Module : 👔 Penderie courte (chemises/vestes)

Tringle horizontale pour chemises, vestes, jupes, pantalons pliés. Hauteur min 1100 mm sous tringle.

## Paramètres configurables
_(aucun paramètre)_

## Pièces produites
_(aucune)_

## Quincaillerie produite
supports tringle Ø25, tringle chromée Ø25

## Impact structurel
- Tablette fixe au-dessus requise : oui
- Tablette fixe en-dessous requise : non
- Fond requis : non
- Séparateur vertical requis : non
- Profondeur min : 550 mm
- Hauteur min : 1100 mm
- Affecte la charge structurelle : oui

## Contraintes de validation
- **error** : Profondeur < 550 mm : insuffisant pour cintres standard. → Augmenter la profondeur ou utiliser une tringle perpendiculaire (pull-out).



---

<!-- chunk_id: module.shelf_adjustable | source: corpus v3 de l'auteur -->

# Module : 📚 Étagères réglables

Étagères posées sur taquets, repositionnables. Module le plus simple, polyvalent.

## Paramètres configurables
| Nom | Type | Description | Plage |
|---|---|---|---|
| `count` | integer | Nombre d'étagères | 1-12, défaut 4 |
| `spacing_mm` | integer | Espacement vertical entre étagères | 150-500 mm, défaut 300 |

## Pièces produites
`tablette-reglable`

## Quincaillerie produite
taquets Ø5 mm, perçages système 32

## Impact structurel
- Tablette fixe au-dessus requise : non
- Tablette fixe en-dessous requise : non
- Fond requis : non
- Séparateur vertical requis : non
- Profondeur min : 150 mm
- Affecte la charge structurelle : non

## Contraintes de validation
- **warning** : Portée > ~400 mm chargée en mélaminé (~550 mm OSB) : fléchissement à terme probable (fluage). → Ajouter un séparateur vertical ou choisir CP/MDF.



---

<!-- chunk_id: module.shoe_rack_inclined | source: corpus v3 de l'auteur -->

# Module : 👟 Range-chaussures incliné

Tablettes inclinées (~15°) pour ranger chaussures debout, talon vers l'avant.

## Paramètres configurables
| Nom | Type | Description | Plage |
|---|---|---|---|
| `tiers` | integer | Nombre de niveaux | 2-8, défaut 4 |

## Pièces produites
`tablette-inclinee`

## Quincaillerie produite
taquets Ø5 mm

## Impact structurel
- Tablette fixe au-dessus requise : non
- Tablette fixe en-dessous requise : oui
- Fond requis : oui
- Séparateur vertical requis : non
- Profondeur min : 250 mm
- Affecte la charge structurelle : non

## Contraintes de validation
_(aucune)_



---

<!-- chunk_id: module.tv_niche | source: corpus v3 de l'auteur -->

# Module : 📺 Niche multimédia (TV)

Compartiment ouvert à l'avant pour TV ou box. Profondeur min 350 mm, ventilation arrière obligatoire si box/ampli.

## Paramètres configurables
| Nom | Type | Description | Plage |
|---|---|---|---|
| `ventilated_back` | boolean | Fond ventilé / aération arrière | défaut true |

## Pièces produites
_(aucune)_

## Quincaillerie produite
passe-câbles Ø60

## Impact structurel
- Tablette fixe au-dessus requise : oui
- Tablette fixe en-dessous requise : oui
- Fond requis : non
- Séparateur vertical requis : non
- Profondeur min : 350 mm
- Hauteur min : 150 mm
- Affecte la charge structurelle : non

## Contraintes de validation
- **warning** : Ventilation arrière désactivée : risque de surchauffe des appareils (box, console, ampli).



---

<!-- chunk_id: module.wine_rack | source: corpus v3 de l'auteur -->

# Module : 🍷 Casier à bouteilles

Croisillons en X formant des alvéoles pour bouteilles couchées. Profondeur min 340 mm (longueur bouteille bordelaise).

## Paramètres configurables
| Nom | Type | Description | Plage |
|---|---|---|---|
| `columns` | integer | Colonnes | 1-10, défaut 4 |
| `rows` | integer | Rangées | 1-10, défaut 4 |

## Pièces produites
`croisillon`

## Quincaillerie produite
_(aucune)_

## Impact structurel
- Tablette fixe au-dessus requise : oui
- Tablette fixe en-dessous requise : oui
- Fond requis : oui
- Séparateur vertical requis : non
- Profondeur min : 340 mm
- Affecte la charge structurelle : oui

## Contraintes de validation
- **warning** : > 30 bouteilles (~40 kg) : vérifier la structure porteuse et la fixation murale si suspendu.



