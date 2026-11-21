# 01-materiaux

<!-- Corpus menuiserie v3.1.0 — catégorie 01-materiaux -->

## Sommaire du fichier
- `materiau.cp_bouleau` — Matériau panneau : Contreplaqué bouleau
- `materiau.cp_okoume` — Matériau panneau : Contreplaqué okoumé
- `materiau.cp_peuplier` — Matériau panneau : Contreplaqué peuplier
- `materiau.essences_massif` — Essences de bois massif : propriétés mécaniques (7 essences)
- `materiau.formaldehyde` — Émissions de formaldéhyde : classes E1 / E0.5
- `materiau.mdf` — Matériau panneau : MDF (Medium)
- `materiau.mecanique` — Bases mécaniques : modules E, fluage k_def, charges de référence, critères de flèche
- `materiau.melamine` — Matériau panneau : Mélaminé (particules)
- `materiau.orientation_debit` — Orientation de débit selon le matériau (5 cas)
- `materiau.osb` — Matériau panneau : OSB3
- `materiau.retrait_gonflement` — Retrait et gonflement du bois massif
- `materiau.synthese` — Synthèse comparative des 6 panneaux courants en menuiserie intérieure

---

<!-- chunk_id: materiau.mecanique | source: EN 622-5, EN 312, EN 300, EN 1995-1-1 tab. 3.2, plages fabricants (v4.0.0, vérifié 08/2026) -->

# Bases mécaniques : E, fluage, charges de référence

Chunk de référence pour tout calcul de flèche. Remplace l'ancienne règle « E = résistance flexion × 300 », erronée (elle surestimait la rigidité du MDF ~4× et du mélaminé ~2,5×).

## Modules d'élasticité retenus (MPa, flexion EN 310, ép. ~18 mm)

| Matériau | E retenu (calculs) | E typique | Provenance | Confiance |
|---|---|---|---|---|
| CP bouleau | 9 000 | 9 000-12 000 (sens du fil) | plages fabricants/handbooks | probable |
| CP okoumé | 4 500 | 4 500-6 000 | littérature CTBX | hypothèse prudente |
| CP peuplier | 3 500 | 3 500-4 500 | littérature | hypothèse prudente |
| MDF | 2 200 | 2 700-3 200 | EN 622-5 tab. 3 (min. normatif 12-19 mm) | sûr (minimum) |
| Mélaminé (particules P2) | 1 600 | 1 800-2 500 | EN 312 P2 (min. normatif 13-20 mm) | sûr (minimum) |
| OSB3 | 3 500 (axe majeur) | — | EN 300 | probable |
| Massif | 12 000-14 000 selon essence | — | Hamon & Roullat, Dunod 2022 tab. 3.2 | sûr |

Le calcul par défaut prend la valeur « retenue » (côté sécurité). Contreplaqués : E vaut dans le sens du fil des faces ; en travers, compter grossièrement la moitié.

## Fluage (déformation qui continue dans le temps)

Un panneau chargé en continu fléchit bien au-delà de sa flèche initiale. EN 1995-1-1 (Eurocode 5) tab. 3.2, classe de service 1 (intérieur sec) :

| Matériau | k_def | Flèche finale = f_inst × (1 + k_def) |
|---|---|---|
| Bois massif | 0,6 | ×1,6 |
| Contreplaqué | 0,8 | ×1,8 |
| OSB/3 | 1,5 | ×2,5 |
| Particules, MDF | 2,25 | ×3,25 |

Note : les MDF et particules « meuble » ne sont pas des panneaux structuraux ; ces k_def sont repris des familles EC5 les plus proches, à traiter comme ordre de grandeur (probable). Conséquence pratique : une tablette MDF acceptable au montage peut tripler sa flèche en quelques années. C'est le fluage, pas un défaut du panneau.

## Charges linéiques de référence (kg par mètre de tablette, prof. 250-300 mm)

Estimations d'usage courant (hypothèses, à ajuster au cas réel) :

| Usage | kg/m |
|---|---|
| Déco, objets légers | 5 |
| Vêtements pliés | 10 |
| Livres de poche, cuisine | 15 |
| Vaisselle empilée | 20 |
| Livres reliés, BD (référence « bibliothèque ») | 25 |
| Classeurs, dossiers | 30 |
| Atelier, outillage | 35 |

L'ancienne référence unique de 8 kg/m sous-estimait fortement une bibliothèque : ne plus l'utiliser.

## Critères de flèche

- **Recommandé (meuble)** : flèche finale ≤ L/350 — en dessous du seuil visuellement gênant.
- **Tolérance max** : flèche finale ≤ L/200 — au-delà, affaissement net.
- Tablette prise en rainure ou vissée dans les joues aux deux extrémités : appui semi-encastré, flèche réelle entre 1× (encastrement parfait, ÷5) et 5× (appui simple). Garder le calcul en appui simple comme marge de sécurité.

## Comment calculer

Exécuter `python3 scripts/calc.py fleche <mat> <L> <b> <h> <kg_m>` ou `portee <mat> <h> <b> <kg_m>` plutôt que de refaire le calcul à la main. Le script inclut le poids propre et le fluage.

---

<!-- chunk_id: materiau.cp_bouleau | source: corpus v3 de l'auteur -->

# Matériau panneau : Contreplaqué bouleau

**Nom commercial** : Contreplaqué bouleau (CP bouleau)

## Propriétés physiques
- **Densité** : 680 kg/m³
- **Résistance à la rupture en flexion (MOR)** : 40 MPa [indicatif, plage publiée 50-70 sens du fil]
- **Module d'élasticité E (calcul de flèche)** : 9 000 retenu (typ. 9 000-12 000, sens du fil des faces) MPa [plages fabricants/handbooks CP bouleau — probable]
- **k_def fluage (EC5 tab. 3.2, classe 1)** : 0,8
- **Portée max indicative 18 mm, prof. 300 mm, critère f_finale ≤ L/350** : ~106 cm à 10 kg/m ; ~83 cm à 25 kg/m (livres). Recalculer via `scripts/calc.py` pour tout autre cas
- **Tenue des vis** : excellent
- **Compatible tourillons** : oui
- **Bande de chant requise** : non

## Formats commerciaux
- **Épaisseurs disponibles** : 6 mm, 10 mm, 12 mm, 15 mm, 18 mm, 22 mm, 25 mm
- **Épaisseur par défaut** : 18 mm
- **Panneaux standard** :
  - 250×125 cm
  - 305×152 cm

## Assemblage recommandé
- Tourillons Ø8 + colle vinylique D3
- Vis 4×40 en renfort
- Fond agrafé CP peuplier 6 mm

## Usinage
- **Défonçage** : Excellent — fraise droite Ø12, passes de 4 mm max
- **Finition de chant** : Ponçage 120→180, vernis ou huile

## Finitions compatibles
- Vernis PU mat
- Huile dure
- Peinture (après sous-couche)
- Teinte + vernis

## Notes
Référence meuble sur mesure. Chant esthétique sans placage.



---

<!-- chunk_id: materiau.cp_okoume | source: corpus v3 de l'auteur -->

# Matériau panneau : Contreplaqué okoumé

**Nom commercial** : Contreplaqué okoumé (CP okoumé)

## Propriétés physiques
- **Densité** : 500 kg/m³
- **Résistance à la rupture en flexion (MOR)** : 30 MPa [indicatif]
- **Module d'élasticité E (calcul de flèche)** : 4 500 retenu (typ. 4 500-6 000) MPa [estimation littérature CTBX — hypothèse prudente]
- **k_def fluage (EC5 tab. 3.2, classe 1)** : 0,8
- **Portée max indicative 18 mm, prof. 300 mm, critère f_finale ≤ L/350** : ~86 cm à 10 kg/m ; ~66 cm à 25 kg/m (livres). Recalculer via `scripts/calc.py` pour tout autre cas
- **Tenue des vis** : bon
- **Compatible tourillons** : oui
- **Bande de chant requise** : non

## Formats commerciaux
- **Épaisseurs disponibles** : 4 mm, 5 mm, 6 mm, 8 mm, 10 mm, 12 mm, 15 mm, 18 mm, 22 mm, 25 mm
- **Épaisseur par défaut** : 18 mm
- **Panneaux standard** :
  - 250×122 cm
  - 310×153 cm

## Assemblage recommandé
- Tourillons Ø8 + colle D3
- Vis 4×40
- Fond agrafé

## Usinage
- **Défonçage** : Bon — bois tendre, avance régulière
- **Finition de chant** : Ponçage 120→180, vernis marin ou huile

## Finitions compatibles
- Vernis marin
- Huile dure
- Lasure
- Peinture

## Notes
Bel aspect chaud. Résistance humidité (avec traitement).



---

<!-- chunk_id: materiau.cp_peuplier | source: corpus v3 de l'auteur -->

# Matériau panneau : Contreplaqué peuplier

**Nom commercial** : Contreplaqué peuplier (CP peuplier)

## Propriétés physiques
- **Densité** : 450 kg/m³
- **Résistance à la rupture en flexion (MOR)** : 25 MPa [indicatif]
- **Module d'élasticité E (calcul de flèche)** : 3 500 retenu (typ. 3 500-4 500) MPa [estimation littérature — hypothèse prudente]
- **k_def fluage (EC5 tab. 3.2, classe 1)** : 0,8
- **Portée max indicative 18 mm, prof. 300 mm, critère f_finale ≤ L/350** : ~80 cm à 10 kg/m ; ~61 cm à 25 kg/m (livres). Recalculer via `scripts/calc.py` pour tout autre cas
- **Tenue des vis** : bon
- **Compatible tourillons** : oui
- **Bande de chant requise** : non

## Formats commerciaux
- **Épaisseurs disponibles** : 3 mm, 5 mm, 6 mm, 8 mm, 10 mm, 12 mm, 15 mm, 18 mm
- **Épaisseur par défaut** : 18 mm
- **Panneaux standard** :
  - 250×122 cm

## Assemblage recommandé
- Tourillons Ø8 + colle
- Vis 4×40
- Fond agrafé

## Usinage
- **Défonçage** : Bon — contre-plaque en sortie pour éviter éclats
- **Finition de chant** : Ponçage 120→180, vernis ou peinture

## Finitions compatibles
- Peinture
- Vernis
- Huile

## ⚠️ Avertissements
- Résistance flexion inférieure au bouleau — réduire la portée libre

## Notes
Plus léger, moins résistant. Bon pour fonds et étagères peu chargées.



---

<!-- chunk_id: materiau.essences_massif | source: Hamon & Roullat, Dunod 2022, p9 tab. 3.2 -->

# Essences de bois massif : propriétés mécaniques (7 essences)

Propriétés mécaniques en MPa pour les 7 essences de bois massif courantes en menuiserie.
Source : Hamon & Roullat, Dunod 2022, p. 9 tableau 3.2.

| Essence | Compression axiale | Traction axiale | Flexion statique | Module élasticité |
|---|---|---|---|---|
| Chêne pédonculé | 56 | 80 | 102 | 13 000 |
| Hêtre | 53 | 78 | 118 | 14 000 |
| Frêne | 49 | 75 | 110 | 13 000 |
| Noyer | 52 | 70 | 110 | 12 000 |
| Sapin | 41 | 58 | 68 | 12 000 |
| Pin sylvestre | 45 | 65 | 79 | 12 000 |
| Douglas | 49 | 69 | 85 | 12 500 |

## Lecture rapide
- **Plus dur** : hêtre (flexion 118 MPa, module 14 000 MPa) — choix pour pieds, traverses.
- **Moyennement dur** : chêne, frêne, noyer (flexion 102-110 MPa).
- **Plus tendre** : sapin (68 MPa). Convient pour ossatures cachées, pas pour mobilier visible portant.

## Application
Le module d'élasticité E sert au calcul de la flèche sous charge :
`f = (5·q·L⁴) / (384·E·I)` avec `I = b·h³/12`
Limite admissible : `L/200`.



---

<!-- chunk_id: materiau.formaldehyde | source: Hamon & Roullat, Dunod 2022 -->

# Émissions de formaldéhyde : classes E1 / E0.5

Le formaldéhyde est un composé volatil irritant émis par les colles des panneaux à base de bois (CP, MDF, particules, OSB).

## Classes (Hamon & Roullat, Dunod 2022, p41-42, fiche 18)

| Classe | Détails |
|---|---|
| **E1** | Classe minimale obligatoire en France depuis 2006 (≤ 8 mg/100g, ≤ 0.1 ppm). |
| **E0.5** | ≤ 4 mg pour particules/OSB, ≤ 5 mg pour MDF. Préférable en intérieur, en particulier chambres d'enfants. |

## Règle de choix
- **Logement neuf, chambre, cuisine, salle de bain** : exiger E0.5 ou supérieur.
- **Atelier, garage, dépendances** : E1 acceptable.
- Vérifier le marquage **CE + classe E** sur le panneau ou la facture.



---

<!-- chunk_id: materiau.mdf | source: corpus v3 de l'auteur -->

# Matériau panneau : MDF (Medium)

**Nom commercial** : MDF (Medium) (MDF)

## Propriétés physiques
- **Densité** : 750 kg/m³
- **Résistance à la rupture en flexion (MOR)** : 20 MPa [EN 622-5 tab. 3, ép. 12-19 mm — sûr]
- **Module d'élasticité E (calcul de flèche)** : 2 200 minimum normatif (typ. fabricant 2 700-3 200) MPa [EN 622-5 tab. 3, essai EN 310 — sûr]
- **k_def fluage (EC5 tab. 3.2, classe 1)** : 2,25 (ordre de grandeur, famille fibres EC5)
- **Portée max indicative 18 mm, prof. 300 mm, critère f_finale ≤ L/350** : ~54 cm à 10 kg/m ; ~42 cm à 25 kg/m (livres). Recalculer via `scripts/calc.py` pour tout autre cas
- **Tenue des vis** : moyen
- **Compatible tourillons** : oui
- **Bande de chant requise** : non

## Formats commerciaux
- **Épaisseurs disponibles** : 3 mm, 6 mm, 10 mm, 12 mm, 16 mm, 18 mm, 19 mm, 22 mm, 25 mm
- **Épaisseur par défaut** : 18 mm
- **Panneaux standard** :
  - 280×207 cm
  - 244×122 cm

## Assemblage recommandé
- Vis + colle obligatoire (vis seules = arrachement)
- Pré-perçage systématique
- Tourillons Ø8 + colle
- Excentriques recommandés
- Fond cloué ou agrafé

## Usinage
- **Défonçage** : Très bon — finition nette, masque FFP2 obligatoire (poussière fine)
- **Finition de chant** : Ponçage fin + apprêt obligatoire avant peinture

## Finitions compatibles
- Peinture (idéal)
- Laque
- Placage + vernis

## ⚠️ Avertissements
- Vis dans les chants : tenue médiocre, pré-perçage + colle obligatoire
- Ne supporte pas l'humidité
- Poids élevé (~750 kg/m³)

## Notes
Homogène, facile à usiner. Surface idéale pour peinture laquée.



---

<!-- chunk_id: materiau.melamine | source: corpus v3 de l'auteur -->

# Matériau panneau : Mélaminé (particules)

**Nom commercial** : Mélaminé (particules) (Mélaminé)

## Propriétés physiques
- **Densité** : 650 kg/m³
- **Résistance à la rupture en flexion (MOR)** : 11 MPa [EN 312 P2, ép. 13-20 mm — sûr]
- **Module d'élasticité E (calcul de flèche)** : 1 600 minimum normatif (typ. 1 800-2 500) MPa [EN 312 P2 tab. 3, essai EN 310 — sûr]
- **k_def fluage (EC5 tab. 3.2, classe 1)** : 2,25 (particules EC5)
- **Portée max indicative 18 mm, prof. 300 mm, critère f_finale ≤ L/350** : ~49 cm à 10 kg/m ; ~38 cm à 25 kg/m (livres). Recalculer via `scripts/calc.py` pour tout autre cas
- **Tenue des vis** : faible
- **Compatible tourillons** : non
- **Bande de chant requise** : oui

## Formats commerciaux
- **Épaisseurs disponibles** : 8 mm, 16 mm, 18 mm, 22 mm, 25 mm
- **Épaisseur par défaut** : 18 mm
- **Panneaux standard** :
  - 280×207 cm
  - 244×122 cm

## Assemblage recommandé
- Excentriques + tourillons (JAMAIS de vis dans le chant)
- Pré-perçage 3 mm face
- Colle contact en renfort
- Fond HDF 3 mm en rainure

## Usinage
- **Défonçage** : Médiocre — éclats fréquents, fraise spéciale stratifié
- **Finition de chant** : Chant mélaminé thermocollant obligatoire (fer à repasser)

## Finitions compatibles
- Aucune (fini d'usine)
- Chant thermocollant assorti

## ⚠️ Avertissements
- INTERDIT : vis dans les chants (arrachement garanti)
- Flexion importante au-delà de 60 cm sans renfort
- Chant thermocollant obligatoire sur tranches visibles

## Notes
Économique, fini d'usine. Assemblage par excentriques uniquement.



---

<!-- chunk_id: materiau.orientation_debit | source: Hamon & Roullat, Dunod 2022 -->

# Orientation de débit selon le matériau (5 cas)

Règles d'orientation pour le calepinage des panneaux. Source : Hamon & Roullat, Dunod 2022, p43-44, fiche 19.

| Matériau | Règle | Impact |
|---|---|---|
| Contreplaqué | Tenir compte du sens du fil apparent (dernier pli de surface). | Aspect visuel et orientation des pièces. |
| Latté | Respecter le sens des lattes (résistance mécanique). | Résistance mécanique fortement affectée. |
| OSB | Copeaux orientés dans la longueur pour meilleure résistance. | Résistance supérieure dans la longueur. |
| Panneaux à décor | Respecter le sens du motif apparent. | Esthétique et nombre de pièces calepinables. |
| MDF / panneau de particules | Pas de sens de débit structurel. | Facilite l'optimisation de débit. |

## Synthèse
- Si **MDF** ou **mélaminé** : aucune contrainte d'orientation, le calepinage peut tourner librement les pièces.
- Si **CP** : le sens du fil de surface affecte l'esthétique mais peu la résistance (croisement des plis).
- Si **OSB** : chercher à orienter les longues pièces dans le sens des copeaux pour la résistance.



---

<!-- chunk_id: materiau.osb | source: corpus v3 de l'auteur -->

# Matériau panneau : OSB3

**Nom commercial** : OSB3 (OSB)

## Propriétés physiques
- **Densité** : 600 kg/m³
- **Résistance à la rupture en flexion (MOR)** : 20 MPa [EN 300 OSB/3 axe majeur — probable]
- **Module d'élasticité E (calcul de flèche)** : 3 500 axe majeur (1 400 axe mineur) MPa [EN 300 OSB/3 — probable]
- **k_def fluage (EC5 tab. 3.2, classe 1)** : 1,5 (OSB/3 EC5)
- **Portée max indicative 18 mm, prof. 300 mm, critère f_finale ≤ L/350** : ~70 cm à 10 kg/m ; ~54 cm à 25 kg/m (livres). Recalculer via `scripts/calc.py` pour tout autre cas
- **Tenue des vis** : moyen
- **Compatible tourillons** : non
- **Bande de chant requise** : non

## Formats commerciaux
- **Épaisseurs disponibles** : 9 mm, 12 mm, 15 mm, 18 mm, 22 mm
- **Épaisseur par défaut** : 18 mm
- **Panneaux standard** :
  - 250×125 cm

## Assemblage recommandé
- Vis à bois 4×50
- Colle PU pour joints
- Pas de tourillons (structure hétérogène)

## Usinage
- **Défonçage** : Médiocre — copeaux arrachés, finition grossière
- **Finition de chant** : Chant brut — ponçage grossier, pas de finition fine

## Finitions compatibles
- Vernis mat (industriel)
- Peinture (ponçage + apprêt)
- Brut

## ⚠️ Avertissements
- Esthétique industrielle uniquement
- Chants grossiers non plaquables

## Notes
Style industriel assumé. Économique.



---

<!-- chunk_id: materiau.retrait_gonflement | source: Hamon & Roullat, Dunod 2022 -->

# Retrait et gonflement du bois massif

Le bois massif change de dimensions selon son humidité. Les formules de retrait/gonflement permettent d'anticiper le jeu à prévoir entre pièces.

## Formules (Hamon & Roullat, Dunod 2022, p17, fiche 8)

**Retrait radial** : `(r × L × ΔH) / 100`
- `r` = coefficient de retrait radial (% par % d'humidité)
- `L` = dimension en mm
- `ΔH` = variation d'humidité en %

**Retrait tangentiel** : `(t × L × ΔH) / 100`
- `t` = coefficient de retrait tangentiel

## Règle pratique
- En menuiserie intérieure, viser une humidité du bois **entre 10 et 12 %** (Hamon & Roullat, Dunod 2022, p14, fiche 7).
- Le retrait tangentiel est ~2× le retrait radial pour la plupart des essences.
- Sur 1 m de chêne, une variation de 5 % d'humidité produit ~1 cm de mouvement tangentiel.
- Conséquence : les grandes pièces de bois massif doivent intégrer du jeu de retrait (panneaux flottants en cadre, jeu d'expansion).



---

<!-- chunk_id: materiau.synthese | source: corpus v3 de l'auteur -->

# Synthèse comparative des 6 panneaux courants en menuiserie intérieure

Tableau comparatif des 6 panneaux les plus utilisés en menuiserie intérieure.

| Matériau | Densité | E (MPa) | k_def | Portée 18 mm à 25 kg/m | Tenue vis | Tourillons | Chant requis |
|---|---|---|---|---|---|---|---|
| Contreplaqué bouleau | 680 | 9 000 | 0,8 | ~83 cm | excellent | oui | non |
| Contreplaqué peuplier | 450 | 3 500 | 0,8 | ~61 cm | bon | oui | non |
| Contreplaqué okoumé | 500 | 4 500 | 0,8 | ~66 cm | bon | oui | non |
| MDF (Medium) | 750 | 2 200 | 2,25 | ~42 cm | moyen | oui | non |
| Mélaminé (particules) | 650 | 1 600 | 2,25 | ~38 cm | faible | non | oui |
| OSB3 | 600 | 3 500 | 1,5 | ~54 cm | moyen | non | non |

Portées : appuis simples, prof. 300 mm, charge livres 25 kg/m, poids propre inclus, critère flèche finale (fluage compris) ≤ L/350. Source de calcul : `scripts/calc.py`.

## Critères de choix
- **Esthétique meuble sur mesure** : CP bouleau (chant beau brut, sans placage).
- **Économie maximale, fini d'usine** : mélaminé (assemblage excentriques obligatoire).
- **Peinture laquée** : MDF (surface homogène, idéale).
- **Salle de bain / humidité** : CP okoumé (résistance + traitement vernis marin).
- **Style industriel assumé** : OSB.
- **Fonds et tablettes peu chargées** : CP peuplier (économique, léger).

## Règles structurelles
- Mélaminé : INTERDIT de visser dans les chants (arrachement garanti). Excentriques + tourillons uniquement.
- MDF : pré-perçage systématique + colle obligatoire (vis seules ne tiennent pas).
- Au-delà de ~40 cm de portée libre chargée en mélaminé ou MDF (~55 cm en OSB), prévoir un séparateur vertical, doubler l'épaisseur ou passer au CP/massif.



