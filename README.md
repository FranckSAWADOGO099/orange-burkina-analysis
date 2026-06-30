#  Analyse des Abonnés Orange Burkina Faso

Projet d'analyse de données réalisé avec **Python** et **pandas**, simulant le travail d'un data analyst junior dans un opérateur télécom.

---

##  Objectif

Analyser un dataset d'abonnés fictifs d'Orange Burkina Faso pour produire des insights business :
- Générer un dataset réaliste à grande échelle (9 600 abonnés)
- Nettoyer et préparer les données brutes
- Identifier les segments d'abonnés selon leur solde et leur activité
- Mesurer la performance par ville et par forfait
- Calculer un score client et classer les abonnés
- Exporter les résultats dans des fichiers CSV propres

---

##  Structure du projet

```
orange-burkina-analysis/
│
├── data/
<<<<<<< HEAD
│   ├── abonnes.csv          # Dataset principal — 9 600 abonnés générés
=======
│   ├── abonnes.csv          # Dataset principal - 15 abonnés fictifs
>>>>>>> 03f462cf304ec53cb3647b9b2b4d7a0787b38450
│   ├── forfaits.csv         # Table des forfaits disponibles
│   └── transactions.csv     # Historique des transactions Orange Money
│
├── scripts/
│   └── analyse_orange.py    # Script principal (génération + analyse)
│
├── output/
│   ├── rapport_final.csv        # Rapport complet par abonné
│   ├── performance_villes.csv   # Agrégations par ville
│   └── performance_forfaits.csv # Agrégations par forfait
│
└── README.md
```

---

## Compétences démontrées

| Compétence | Détail |
|---|---|
| **Génération de données** | `numpy.random.default_rng()` avec seed fixe pour un dataset reproductible à grande échelle |
| **Chargement de données** | `pd.read_csv()`, exploration avec `info()`, `describe()`, `shape` |
| **Nettoyage de données** | Suppression doublons, valeurs manquantes, types incorrects, noms invalides avec `re` |
| **Filtrage** | Filtres simples et combinés avec `&`, `|`, `~`, `isin()`, `between()`, `str.contains()` |
| **Agrégations** | `groupby()`, `agg()` avec statistiques multiples par segment |
| **Fusion de tables** | `merge()` inner et left join sur plusieurs tables |
| **Colonnes calculées** | `np.where()`, `apply()`, `pd.cut()` pour créer de nouvelles variables |
| **Export** | `to_csv()` pour partager les résultats |

---

## Description des données

### abonnes.csv (9 600 lignes générées)
| Colonne | Type | Description |
|---|---|---|
| id_abonne | int | Identifiant unique |
| nom | str | Nom de l'abonné (prénom + nom burkinabè, tirés aléatoirement) |
| ville | str | Ville de résidence (10 villes possibles) |
| solde | float | Solde en FCFA |
| forfait | str | Type de forfait souscrit |
| actif | bool | Statut actif/inactif |
| appels_mois | int | Nombre d'appels ce mois |
| data_go | float | Data consommée en Go |
| anciennete_mois | int | Ancienneté en mois |

### forfaits.csv
| Colonne | Type | Description |
|---|---|---|
| id_forfait | int | Identifiant du forfait |
| nom_forfait | str | Nom commercial |
| prix_fcfa | int | Prix mensuel en FCFA |
| data_incluse_go | float | Data incluse en Go |
| appels_inclus | int | Appels inclus par mois |

### transactions.csv
| Colonne | Type | Description |
|---|---|---|
| id_abonne | int | Référence abonné |
| montant | int | Montant en FCFA |
| type | str | Type : envoi ou retrait |

---

<<<<<<< HEAD
## 🧬 Génération du dataset

Le dataset n'est plus écrit en dur : `creer_donnees()` génère 9 600 abonnés via `numpy.random.default_rng(42)` (seed fixe → résultats reproductibles d'une exécution à l'autre). Le forfait, le solde, les appels et la consommation data sont tirés de façon cohérente entre eux (ex. un abonné avec un gros forfait a un solde moyen plus élevé, un abonné inactif consomme presque rien). Environ 40 % des abonnés se voient attribuer 1 à 3 transactions Orange Money.

---

## 🚀 Comment exécuter le projet
=======
## Comment exécuter le projet
>>>>>>> 03f462cf304ec53cb3647b9b2b4d7a0787b38450

### Prérequis
```
Python 3.12+
pandas
numpy
```

### Installation
```bash
git clone https://github.com/FranckSAWADOGO099/orange-burkina-analysis.git
cd orange-burkina-analysis
pip install pandas numpy
```

### Exécution
```bash
cd scripts
python analyse_orange.py
```

Le script crée automatiquement les dossiers `data/` et `output/` s'ils n'existent pas, génère les CSV bruts dans `data/`, puis exporte les résultats d'analyse dans `output/`.

---

## Résultats principaux

### Segmentation des abonnés par solde
| Segment | Critère solde | Abonnés |
|---|---|---|
| Standard | 3 000 – 8 000 FCFA | 3 343 |
| Faible | 1 000 – 3 000 FCFA | 2 557 |
| Critique | < 1 000 FCFA | 2 087 |
| Premium | ≥ 8 000 FCFA | 1 613 |

### Performance par ville (solde moyen)
| Ville | Abonnés | Solde moyen |
|---|---|---|
| Tenkodogo | 976 | 4 509 FCFA |
| Kaya | 911 | 4 390 FCFA |
| Dedougou | 960 | 4 353 FCFA |
| Koudougou | 981 | 4 297 FCFA |
| Ouaga | 923 | 4 289 FCFA |
| Banfora | 939 | 4 276 FCFA |
| Fada N'Gourma | 985 | 4 201 FCFA |
| Gaoua | 984 | 4 155 FCFA |
| Ouahigouya | 964 | 4 122 FCFA |
| Bobo | 977 | 4 113 FCFA |

### Classement par score client
| Rang | Nombre d'abonnés |
|---|---|
| Argent | 3 356 |
| Platine | 2 703 |
| Bronze | 1 796 |
| Or | 1 745 |

### Synthèse globale
- **Total abonnés** : 9 600
- **Abonnés actifs** : 7 158 (74,6 %)
- **Abonnés inactifs** : 2 442
- **Forfait le plus souscrit** : Orange Liberté

---

## Observations

- Les villes affichent des soldes moyens assez proches (~4 100 à 4 500 FCFA), reflet d'une génération de données équilibrée plutôt que d'un déséquilibre marqué entre grandes et petites villes
- Près d'un quart des abonnés (2 442) sont inactifs, ce qui justifie une campagne de réactivation ciblée
- Plus de 2 000 abonnés sont en zone critique (solde < 1 000 FCFA) — opportunité de campagne de recharge
- Les abonnés **Orange Max 10Go** ont en moyenne plus d'appels et plus de data consommée que les autres forfaits

---

## Auteur

**Franck Marie Ghislain SAWADOGO**
Étudiant GEI - IST Ouagadougou
En formation Data Analyst

---

## Technologies utilisées

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green)
![NumPy](https://img.shields.io/badge/NumPy-1.24-orange)
