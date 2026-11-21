# Skills

Des skills pour Claude et pour les agents qui lisent le format ouvert Agent Skills. Chaque dossier à la racine est un skill autonome : un fichier `SKILL.md`, des références, parfois des scripts.

## Catalogue

| Skill | Ce qu'il fait | Fiche |
|---|---|---|
| [`assistant-cuisine`](assistant-cuisine) | Cuisine domestique : goût, science, cuissons, sécurité, menus, substitutions. Inventaire et fiches recettes dans ton Google Drive, en option. | [docs/assistant-cuisine.md](docs/assistant-cuisine.md) |
| [`l-etabli`](l-etabli) | Conception et fabrication de meubles et d'ouvrages en bois sur mesure, intérieur et extérieur non structurel. Corpus technique sourcé et script de calcul de flèche. | [docs/l-etabli.md](docs/l-etabli.md) |

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
