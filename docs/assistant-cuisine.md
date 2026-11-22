# Assistant cuisine

Dossier du skill : [`assistant-cuisine/`](../assistant-cuisine). Installation et licence : voir le [README](../README.md).

Un skill pour Claude qui répond comme un cuisinier domestique expérimenté : idées de plats, recettes, techniques, rattrapage d'un plat raté, menus de la semaine, substitutions, conservation.

## Ce qu'il sait faire

- Corriger un plat fade, trop salé, sec ou déséquilibré, avec un repère chiffré.
- Expliquer pourquoi une préparation a raté et quoi faire tout de suite.
- Proposer un plat à partir de ce qu'il y a dans le frigo.
- Rédiger une recette complète ou les menus d'une semaine, relus sur le sel, l'acide, le gras et la texture.
- Donner les seuils de cuisson et de conservation. Le fichier sécurité fait autorité sur les repères de texture.
- Remplacer un ingrédient, adapter à un régime, convertir des quantités.

## Contenu

| Fichier | Sujet |
|---|---|
| `gem-1-regles-gout.md` | Goût : sel, gras, acide, chaleur, rattrapage |
| `gem-2-science.md` | Science culinaire : causes, effets, seuils, viande |
| `gem-3-securite-conservation.md` | Sécurité alimentaire et conservation |
| `gem-4-structure-fonds.md` | Sauces, fonds, bouillons, liaisons |
| `gem-5-cuissons-equipement.md` | Protocoles de cuisson et équipement domestique |
| `gem-6-patterns-menus.md` | Architectures de plats et planification de menus |
| `gem-7-associations-saveurs.md` | Associations d'ingrédients |
| `gem-8-poissons-grains.md` | Poissons, céréales, légumineuses |
| `gem-9-substitutions-conversions-boulangerie.md` | Substitutions, conversions, pain et pâtisserie |
| `gem-10-kenwood-cooking-chef.md` | Robot Kenwood Cooking Chef KM080 / KM099 |

## Google Drive (facultatif)

Sans Drive, le skill répond à toutes les questions de cuisine.

Si tu connectes ton propre Google Drive à Claude, il peut aussi tenir un inventaire et une bibliothèque de recettes. Il s'appuie sur quatre conventions de nommage, dans ton Drive à toi :

- `Inventaire_Cuisine_Dynamique_Actuel` : un document avec quatre sections (Frigo & frais, Épices & aromates séchés, Huiles, vinaigres & condiments, Placard & épicerie).
- `Recette : [nom] — [produit] — [cuisson]` : une fiche par recette validée.
- `Profil_Cuisinier_AAAA-MM-JJ` : une synthèse de tes habitudes, générée à la demande.
- `Plats_Valides` : un Google Sheet des plats que la famille a aimés, avec deux onglets. **Plats** liste chaque plat avec son type, sa saison, une note sur 3, son temps de préparation, la dernière fois qu'il a été servi et une remarque. **Recettes** garde la version cuisinée de chaque plat. Quand tu demandes les menus de la semaine, le skill pioche d'abord dans les plats bien notés, puis met le Sheet à jour quand tu lui dis ce qui a plu. Si ton Sheet porte un autre nom, donne son ID à Claude ou remplace `<ID_DU_SHEET_PLATS_VALIDES>` dans `SKILL.md`.

Le skill ne contient aucun lien vers un Drive. Il ne lit que les documents du compte que tu connectes.

## Sources et attribution

Les fichiers de références sont des notes de lecture : des règles reformulées en français pour guider un assistant. Ils ne reproduisent ni le texte ni les recettes des ouvrages. Les idées et le travail de fond appartiennent à leurs auteurs. Si ce skill t'est utile, achète leurs livres.

| Fichier | Sources principales |
|---|---|
| `gem-1` | Samin Nosrat, *Salt, Fat, Acid, Heat*, 2017 |
| `gem-2` | Harold McGee, *On Food and Cooking* |
| `gem-4` | Auguste Escoffier, codification classique des sauces et garnitures |
| `gem-5` | Michel Maincent-Morel, *La Cuisine de Référence*, BPI |
| `gem-6` | Yotam Ottolenghi, *Simple*, 2018. En complément : *Plenty* du même auteur, Alain Ducasse |
| `gem-7` | Karen Page et Andrew Dornenburg, *The Flavor Bible*, 2008. Niki Segnit, *The Flavor Thesaurus* |
| `gem-3`, `gem-8`, `gem-9` | Repères publics USDA, FDA, FSA et ANSES. Règlement (UE) n° 1169/2011 pour les allergènes |
| `gem-10` | Notice Kenwood KM080 series |

Ce projet n'est ni affilié à ces auteurs, éditeurs et marques, ni approuvé par eux.

Tu es auteur ou ayant droit et tu souhaites une correction ou un retrait ? Ouvre une issue sur ce dépôt.

## Limites

- Les seuils de sécurité alimentaire sont des repères grand public. Plusieurs durées de conservation sont marquées « à confirmer » dans les fichiers. Vérifie auprès d'une source officielle avant de t'y fier.
- Ce skill n'est pas un avis médical, en particulier pour les allergies et la maladie cœliaque.
- `gem-10` ne sert qu'aux propriétaires du robot concerné.
