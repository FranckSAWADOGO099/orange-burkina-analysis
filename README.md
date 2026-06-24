# 📊 Analyse des Abonnés Orange Burkina Faso

Projet d'analyse de données réalisé avec **Python** et **pandas**, simulant le travail d'un data analyst junior dans un opérateur télécom burkinabè.

---

## 🎯 Objectif

Analyser un dataset d'abonnés fictifs d'Orange Burkina Faso pour produire des insights business :
- Nettoyer et préparer les données brutes
- Identifier les segments d'abonnés selon leur solde et leur activité
- Mesurer la performance par ville et par forfait
- Calculer un score client et classer les abonnés
- Exporter les résultats dans des fichiers CSV propres

---

## 🗂️ Structure du projet

```
orange-burkina-analysis/
│
├── data/
│   ├── abonnes.csv          # Dataset principal — 15 abonnés fictifs
│   ├── forfaits.csv         # Table des forfaits disponibles
│   └── transactions.csv     # Historique des transactions Orange Money
│
├── scripts/
│   └── analyse_orange.py    # Script principal d'analyse
│
├── output/
│   ├── rapport_final.csv        # Rapport complet par abonné
│   ├── performance_villes.csv   # Agrégations par ville
│   └── performance_forfaits.csv # Agrégations par forfait
│
└── README.md
```

---

## 🛠️ Compétences démontrées

| Compétence | Détail |
|---|---|
| **Chargement de données** | `pd.read_csv()`, exploration avec `info()`, `describe()`, `shape` |
| **Nettoyage de données** | Suppression doublons, valeurs manquantes, types incorrects, noms invalides avec `re` |
| **Filtrage** | Filtres simples et combinés avec `&`, `|`, `~`, `isin()`, `between()`, `str.contains()` |
| **Agrégations** | `groupby()`, `agg()` avec statistiques multiples par segment |
| **Fusion de tables** | `merge()` inner et left join sur plusieurs tables |
| **Colonnes calculées** | `np.where()`, `apply()`, `pd.cut()` pour créer de nouvelles variables |
| **Export** | `to_csv()` pour partager les résultats |

---

## 📁 Description des données

### abonnes.csv
| Colonne | Type | Description |
|---|---|---|
| id_abonne | int | Identifiant unique |
| nom | str | Nom de l'abonné |
| ville | str | Ville de résidence |
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

## 🚀 Comment exécuter le projet

### Prérequis
```
Python 3.12+
pandas
numpy
```

### Installation
```bash
git clone https://github.com/TON_USERNAME/orange-burkina-analysis.git
cd orange-burkina-analysis
pip install pandas numpy
```

### Exécution
```bash
cd scripts
python analyse_orange.py
```

Le script crée automatiquement les fichiers CSV dans `data/` et exporte les résultats dans `output/`.

---

## 📈 Résultats principaux

### Segmentation des abonnés par solde
| Segment | Critère solde | Abonnés |
|---|---|---|
| Premium | ≥ 8 000 FCFA | 2 |
| Standard | 3 000 – 8 000 FCFA | 5 |
| Faible | 1 000 – 3 000 FCFA | 4 |
| Critique | < 1 000 FCFA | 4 |

### Performance par ville
| Ville | Abonnés | Solde moyen |
|---|---|---|
| Ouaga | 6 | 6 450 FCFA |
| Koudougou | 3 | 2 433 FCFA |
| Banfora | 3 | 2 767 FCFA |
| Bobo | 3 | 900 FCFA |

### Classement par score client
| Rang | Nombre d'abonnés |
|---|---|
| Platine | 3 |
| Or | 5 |
| Argent | 4 |
| Bronze | 3 |

---

## 💡 Observations

- **Bobo** a le solde moyen le plus faible et le plus fort taux d'inactifs
- **Ouaga** concentre les abonnés avec les soldes les plus élevés
- Les abonnés **Orange Max 10Go** ont en moyenne plus d'appels et plus de data consommée
- Les abonnés anciens (fidèles) sont plus actifs que les nouveaux

---

## 👤 Auteur

**Franck SAWADOGO**
Étudiant GEI — IST Ouagadougou
En formation Data Analytics

---

## 📚 Technologies utilisées

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green)
![NumPy](https://img.shields.io/badge/NumPy-1.24-orange)
