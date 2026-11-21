# Expert présentation

Dossier du skill : [`expert-presentation/`](../expert-presentation). Installation et licence : voir le [README](../README.md).

Un skill pour Claude qui aide à préparer un pitch, une présentation, des slides, une note de synthèse ou une prise de parole, et à auditer un support existant. Il produit des livrables utilisables : message essentiel, plan, titres de slides, script oral, réponses aux objections.

## Ce qu'il sait faire

- Cadrer une idée floue : public, objectif, décision attendue, message essentiel, angle.
- Construire une intervention complète, du diagnostic au plan de slides et à la préparation orale.
- Préparer une recommandation devant un décideur, la décision en tête.
- Auditer une présentation : vue d'ensemble d'abord, puis slide par slide, puis une note et trois priorités de correction.
- Réécrire un titre, un objectif ou une conclusion, avec la formulation prête à l'emploi.
- Préparer les questions difficiles et une routine contre le trac.

Exemples de demandes : voir [`references/prompts-exemples.md`](../expert-presentation/references/prompts-exemples.md).

## Contenu

| Fichier | Sujet |
|---|---|
| `SKILL.md` | Rôle, modes de travail, chaîne de raisonnement, protocole d'analyse, erreurs courantes |
| `references/knowledge-base.md` | 17 blocs : auditoire, PDFR, profils, CAB et SONCAS, scénarios, pitch, design de slides, oral, données chiffrées, objections, réécriture |
| `references/prompts-exemples.md` | Demandes types à copier |

## Sources

Le corpus est une synthèse de l'auteur. Les outils qu'il mobilise (SONCAS, CAB, pyramide inversée, règle des trois, pitch en quatre temps) sont des classiques de la vente et de la communication. Les citations sont attribuées quand leur auteur est connu.

Deux garde-fous sont écrits dans le corpus :

- La règle « 7 % mots, 38 % voix, 55 % corps » attribuée à Mehrabian n'est pas présentée comme une loi générale.
- Les chiffres non sourcés ont été retirés. Les maximes sur la préparation et la respiration sont données comme des repères de travail, pas comme des mesures.

## Limites

- Le skill ne juge la forme d'une présentation (police, contraste, alignement) que s'il dispose du fichier ou d'images. Sur une simple description, il s'en tient au fond.
- Les profils comportementaux et les leviers de motivation sont des grilles de lecture pratiques, pas des résultats scientifiques établis.
