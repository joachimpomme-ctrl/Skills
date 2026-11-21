# Édition publique — 21/11/2026
- Prix indicatifs retirés du corpus (16 montants). Le skill renvoie vers une recherche web datée.
- Référence bibliographique complète pour « Dunod 2022 » (Hamon & Roullat).
- Commentaires de provenance réécrits : `corpus v3 de l'auteur` remplace les chemins de fichiers de l'application d'origine.
- Corrections mineures : textes restés en anglais, une source imprécise sur l'anti-basculement.
- Aucun changement de calcul : `scripts/calc.py` et les valeurs des evals sont identiques à la v4.0.0.

# v4.0.0 — 30/08/2026
- Moteur de flèche corrigé : abandon de « E = flexion × 300 » (surestimait la rigidité MDF ~4×, mélaminé ~2,5×). Modules E normatifs (EN 622-5, EN 312 P2, EN 300) et plages fabricants, chunk `materiau.mecanique`.
- Fluage intégré (k_def, EN 1995-1-1 tab. 3.2) : verdicts sur la flèche FINALE. Critères L/350 recommandé, L/200 max.
- Charges de référence par usage (livres 25 kg/m) au lieu du 8 kg/m unique. Portées max recalculées partout (01, 03, 05, 06, 10).
- Script exécutable `scripts/calc.py` : flèche, portée max, poids de porte, charnières, table de référence. Source unique des chiffres.
- Nouveau module `references/12-exterieur.md` : classes d'emploi EN 335, essences EN 350, panneaux ext., inox A2/A4, colles D4/PU, terrasse DTU 51.4, pergola/jardinière, finitions ext., limites structurelles fermes.
- Provenance à 4 niveaux (norme / fabricant / règle de l'art / hors corpus) annoncée avec chaque donnée.
- Jeu de tests `references/13-evals.md` (24 cas, valeurs vérifiées au script).
# v3.1.0 — 07/2025 : version initiale (126 chunks, intérieur seul).
