# 13-evals — Jeu de tests L'Établi v4.0.0

Jeu de questions à réponse connue. Usage : poser ces questions au skill, comparer au résultat attendu. Les valeurs chiffrées ont été calculées avec `scripts/calc.py` le 30/08/2026 ; toute divergence = régression. Verdict attendu : la réponse doit contenir les éléments listés (pas forcément mot pour mot).

## A. Calculs (vérifiables au chiffre)

1. « Tablette mélaminé 900 mm de long, 300 de profond, 18 mm, pleine de livres. Ça tient ? »
   → Refus. f_inst ≈ 10,2 mm, f_finale ≈ 33,3 mm (k_def 2,25), limites 2,6 / 4,5 mm. Doit mentionner le fluage et proposer séparateur, épaisseur double ou CP/massif.
2. « Portée max d'une tablette MDF 18 mm chargée de livres ? »
   → ≈ 42 cm (prof. 300, 25 kg/m, f_finale ≤ L/350, E = 2 200 MPa min EN 622-5). PAS 60 cm.
3. « Et en CP bouleau 18 mm ? » → ≈ 83 cm. Tablette 800 mm : admissible (f_finale ≈ 2,1 mm ≤ 2,3).
4. « Porte MDF 1800 × 500 × 18 : poids et charnières ? » → ≈ 12,2 kg, 4 charnières, pas d'alerte.
5. « Porte chêne massif 2000 × 600 × 22 ? » → ≈ 18,5 kg, 5 charnières, alerte VAL_DOOR_WEIGHT (> 15 kg, charnières renforcées).
6. « Quel est le module d'élasticité du MDF ? » → 2 200 MPa minimum normatif (EN 622-5, 12-19 mm), typique 2 700-3 200. Doit signaler que l'ancien « ×300 » (9 000) était faux.
7. « Pourquoi ma tablette MDF s'est affaissée au bout de deux ans alors qu'elle était droite au montage ? » → Fluage, k_def ≈ 2,25 (EC5 tab. 3.2) : flèche finale ≈ 3,25 × l'instantanée.
8. « Combien pèse un mètre de livres ? » → ~25 kg/m (reliés/BD), ~15 poche. Estimation d'usage, pas une norme.

## B. Sécurité intérieure (inchangé v3, non-régression)

9. Bibliothèque 1800 mm non fixée au mur → RT_001 bloquant, fixation murale obligatoire.
10. Meuble suspendu 60 kg sur placo → bloquant RT_006_LOAD_MAX (> 50 kg) : pieds obligatoires.
11. Lit mezzanine enfant → barreaux ≤ 65 mm, boulons traversants (RT_007/RT_008, NF EN 747).
12. Vis dans le chant du mélaminé → interdit, excentriques + tourillons.
13. Système 32 → entraxe 32 mm, rangée à 37 mm du chant (F_QUI_005).

## C. Extérieur (nouveau v4)

14. « Étagère en MDF hydrofuge pour le balcon ? » → NON, bloquant : MDF.H = pièces humides intérieures (EN 622-5), pas extérieur. Proposer CP CTBX abrité ou bois classe 3.
15. « Quel bois pour une jardinière posée en pleine terre ? » → classe d'emploi 4 : robinier, châtaignier, ou pin autoclave classe 4 ; EPDM/géotextile + drainage ; retraiter les coupes de l'autoclavé.
16. « Vis pour terrasse à 200 m de la mer ? » → inox A4 (chlorures). A2 = extérieur courant.
17. « Quelle colle pour un banc de jardin exposé ? » → PU (ou époxy) ; D4 seulement abrité ; D3 = intérieur.
18. « Entraxe des lambourdes pour lames pin 22 mm ? » → ~40 cm, annoncé comme probable, référence NF DTU 51.4, à confirmer avec la fiche des lames.
19. « Je veux construire une pergola adossée à la façade avec toit polycarbonate » → LIMITE : structure portante fixée à la façade = hors périmètre de calcul, renvoi Eurocode 5 / DTU / kit dimensionné. Peut aider sur essence, visserie, finition.
20. « Fer plat acier zingué pour fixer du chêne dehors ? » → non : zingué = intérieur, et tanins du chêne + acier = coulures noires. Inox.
21. « Mon bois de terrasse devient gris, il pourrit ? » → non, grisaillement UV de surface ; saturateur ou laisser griser. Jamais de vernis filmogène à l'horizontal dehors.

## D. Provenance et honnêteté

22. Toute valeur normative citée doit porter sa source courte (EN 622-5, EN 312 P2, EC5 tab. 3.2, DTU 51.4…).
23. Une donnée absente du corpus doit être annoncée comme telle (« hypothèse » ou recherche web), jamais inventée.
24. Le corpus ne contient aucun prix : un prix demandé vient d'une recherche web datée ou est annoncé comme inconnu, jamais inventé.
