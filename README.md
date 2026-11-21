# Skills

Des skills pour Claude et pour les agents qui lisent le format ouvert Agent Skills. Chaque dossier à la racine est un skill autonome : un fichier `SKILL.md`, des références, parfois des scripts.

## Catalogue

| Skill | Ce qu'il fait | Fiche |
|---|---|---|
| [`assistant-cuisine`](assistant-cuisine) | Cuisine domestique : goût, science, cuissons, sécurité, menus, substitutions. Inventaire et fiches recettes dans ton Google Drive, en option. | [docs/assistant-cuisine.md](docs/assistant-cuisine.md) |
| [`expert-presentation`](expert-presentation) | Pitch, présentation, slides, prise de parole : cadrer, produire, auditer un support existant. | [docs/expert-presentation.md](docs/expert-presentation.md) |
| [`l-etabli`](l-etabli) | Conception et fabrication de meubles et d'ouvrages en bois sur mesure, intérieur et extérieur non structurel. Corpus technique sourcé et script de calcul de flèche. | [docs/l-etabli.md](docs/l-etabli.md) |
| [`parentalite`](parentalite) | Questions éducatives de 3 à 18 ans, à partir de la recherche : colères, confiance, fratrie, sexualité, écrans, adolescence, quand consulter. | [docs/parentalite.md](docs/parentalite.md) |

### Hébergés dans un autre dépôt

Ces deux skills vivent dans [joachimpomme-ctrl/comptable](https://github.com/joachimpomme-ctrl/comptable), avec leur documentation, leurs tests, leurs avertissements et leur propre licence (CC BY-NC 4.0). Ils ne sont pas copiés ici pour éviter deux versions qui divergent.

| Skill | Ce qu'il fait |
|---|---|
| `assistant-fiscal-comptable` | Fiscalité et comptabilité françaises : BNC, BIC, location meublée, revenus fonciers, transmission. Règles tracées et paramètres chiffrés sourcés. |
| `conseiller-patrimoine` | Aide à la décision patrimoniale pour un particulier : placements, crédit, immobilier, retraite. Pas un conseil en investissement. |

## Installation

Dans Claude (web, bureau, mobile) :

1. Télécharge ce dépôt.
2. Zippe le dossier du skill voulu, par exemple `l-etabli/`. Le zip doit contenir le dossier, pas seulement son contenu.
3. Importe le zip dans les réglages de Claude, rubrique Skills.

Dans Claude Code : copie le dossier du skill dans `~/.claude/skills/`.

## Avertissement

Ces skills sont des aides. Ils ne remplacent ni un professionnel, ni un bureau d'études, ni la notice d'un fabricant. Un modèle de langage peut se tromper, même appuyé sur un corpus. Vérifie ce qui engage ta sécurité ou ton argent avant d'agir. Les limites propres à chaque skill sont décrites dans sa fiche.

## Contribuer

Les corrections sont bienvenues. Une correction de fond doit citer sa source : norme, fiche fabricant ou ouvrage avec la page.

## Licence

MIT. Voir [`LICENSE`](LICENSE). La licence couvre les textes et le code de ce dépôt. Elle ne couvre ni les normes ni les ouvrages cités. Les marques citées appartiennent à leurs propriétaires.
