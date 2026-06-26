# ============================================================
# PROJET 1 : ANALYSE DES ABONNÉS ORANGE BURKINA FASO
# Auteur   : Franck SAWADOGO
# Outils   : Python, pandas, numpy
# Données  : Dataset fictif abonnés Orange Burkina
# ============================================================

import pandas as pd
import numpy as np
import os
import re

# Configuration
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("  ANALYSE ABONNÉS ORANGE BURKINA FASO")
print("=" * 60)

# ============================================================
# ÉTAPE 1 - CRÉATION DES DONNÉES
# ============================================================

def creer_donnees():
    abonnes = [
        {"id_abonne": 1,  "nom": "Aminata Ouedraogo", "ville": "Ouaga",     "solde": 3750,  "forfait": "Orange Max 5Go",  "actif": True,  "appels_mois": 45,  "data_go": 3.2, "anciennete_mois": 24, "id_forfait": 2},
        {"id_abonne": 2,  "nom": "Seydou Traore",     "ville": "Bobo",      "solde": 1200,  "forfait": "Orange Liberté",  "actif": False, "appels_mois": 12,  "data_go": 0.5, "anciennete_mois": 6,  "id_forfait": 1},
        {"id_abonne": 3,  "nom": "Mariam Sawadogo",   "ville": "Ouaga",     "solde": 5000,  "forfait": "Orange Max 10Go", "actif": True,  "appels_mois": 67,  "data_go": 7.5, "anciennete_mois": 18, "id_forfait": 3},
        {"id_abonne": 4,  "nom": "Ibrahim Kone",      "ville": "Koudougou", "solde": 0,     "forfait": "Orange Liberté",  "actif": True,  "appels_mois": 23,  "data_go": 1.2, "anciennete_mois": 12, "id_forfait": 1},
        {"id_abonne": 5,  "nom": "Fatima Coulibaly",  "ville": "Bobo",      "solde": 0,     "forfait": "Orange Max 5Go",  "actif": False, "appels_mois": 0,   "data_go": 0.0, "anciennete_mois": 3,  "id_forfait": 2},
        {"id_abonne": 6,  "nom": "Kofi Ouattara",     "ville": "Ouaga",     "solde": 12000, "forfait": "Orange Max 10Go", "actif": True,  "appels_mois": 102, "data_go": 9.8, "anciennete_mois": 48, "id_forfait": 3},
        {"id_abonne": 7,  "nom": "Salif Zongo",       "ville": "Banfora",   "solde": 2500,  "forfait": "Orange Liberté",  "actif": True,  "appels_mois": 34,  "data_go": 2.1, "anciennete_mois": 15, "id_forfait": 1},
        {"id_abonne": 8,  "nom": "Amina Diallo",      "ville": "Ouaga",     "solde": 650,   "forfait": "Orange Max 5Go",  "actif": False, "appels_mois": 8,   "data_go": 0.3, "anciennete_mois": 2,  "id_forfait": 2},
        {"id_abonne": 9,  "nom": "Adama Bambara",     "ville": "Ouaga",     "solde": 9500,  "forfait": "Orange Max 10Go", "actif": True,  "appels_mois": 95,  "data_go": 9.1, "anciennete_mois": 42, "id_forfait": 3},
        {"id_abonne": 10, "nom": "Safi Ouoba",        "ville": "Banfora",   "solde": 0,     "forfait": "Orange Liberté",  "actif": False, "appels_mois": 0,   "data_go": 0.0, "anciennete_mois": 1,  "id_forfait": 1},
        {"id_abonne": 11, "nom": "Binta Kabore",      "ville": "Koudougou", "solde": 4200,  "forfait": "Orange Max 5Go",  "actif": True,  "appels_mois": 51,  "data_go": 3.9, "anciennete_mois": 30, "id_forfait": 2},
        {"id_abonne": 12, "nom": "Moussa Tapsoba",    "ville": "Ouaga",     "solde": 7800,  "forfait": "Orange Max 10Go", "actif": True,  "appels_mois": 88,  "data_go": 8.5, "anciennete_mois": 36, "id_forfait": 3},
        {"id_abonne": 13, "nom": "Aissata Nana",      "ville": "Bobo",      "solde": 1500,  "forfait": "Orange Liberté",  "actif": True,  "appels_mois": 19,  "data_go": 0.8, "anciennete_mois": 8,  "id_forfait": 1},
        {"id_abonne": 14, "nom": "Rasmane Ilboudo",   "ville": "Koudougou", "solde": 3100,  "forfait": "Orange Max 5Go",  "actif": True,  "appels_mois": 42,  "data_go": 2.8, "anciennete_mois": 20, "id_forfait": 2},
        {"id_abonne": 15, "nom": "Clarisse Toe",      "ville": "Banfora",   "solde": 5800,  "forfait": "Orange Max 10Go", "actif": True,  "appels_mois": 73,  "data_go": 6.2, "anciennete_mois": 28, "id_forfait": 3},
    ]

    forfaits = [
        {"id_forfait": 1, "nom_forfait": "Orange Liberté",  "prix_fcfa": 1500,  "data_incluse_go": 2.0,  "appels_inclus": 30},
        {"id_forfait": 2, "nom_forfait": "Orange Max 5Go",  "prix_fcfa": 3500,  "data_incluse_go": 5.0,  "appels_inclus": 60},
        {"id_forfait": 3, "nom_forfait": "Orange Max 10Go", "prix_fcfa": 6000,  "data_incluse_go": 10.0, "appels_inclus": 120},
    ]

    transactions = [
        {"id_abonne": 1,  "montant": 5000,  "type": "envoi"},
        {"id_abonne": 1,  "montant": 2500,  "type": "retrait"},
        {"id_abonne": 3,  "montant": 15000, "type": "envoi"},
        {"id_abonne": 3,  "montant": 8000,  "type": "retrait"},
        {"id_abonne": 6,  "montant": 25000, "type": "envoi"},
        {"id_abonne": 7,  "montant": 3000,  "type": "envoi"},
        {"id_abonne": 9,  "montant": 12000, "type": "retrait"},
        {"id_abonne": 11, "montant": 4500,  "type": "envoi"},
        {"id_abonne": 12, "montant": 18000, "type": "envoi"},
        {"id_abonne": 15, "montant": 9000,  "type": "envoi"},
        {"id_abonne": 15, "montant": 3500,  "type": "retrait"},
    ]

    pd.DataFrame(abonnes).to_csv("../data/abonnes.csv",      index=False, encoding="utf-8")
    pd.DataFrame(forfaits).to_csv("../data/forfaits.csv",     index=False, encoding="utf-8")
    pd.DataFrame(transactions).to_csv("../data/transactions.csv", index=False, encoding="utf-8")
    print("Fichiers CSV créés dans data")

creer_donnees()

# ============================================================
# ÉTAPE 2 - CHARGEMENT ET EXPLORATION
# ============================================================

print("-" * 60)
print("ÉTAPE 2 — CHARGEMENT ET EXPLORATION")
print("-" * 60)

df = pd.read_csv("../data/abonnes.csv")
df_forfaits = pd.read_csv("../data/forfaits.csv")
df_trans = pd.read_csv("../data/transactions.csv")

print(f"Abonnés chargés : {len(df)} lignes, {len(df.columns)} colonnes")
print(f"Forfaits chargés : {len(df_forfaits)} lignes")
print(f"Transactions chargées : {len(df_trans)} lignes")
print()
print("Aperçu des données :")
print(df.head(3).to_string())
print()
print("Types et valeurs manquantes :")
print(df.info())


# ============================================================
# ÉTAPE 3 - NETTOYAGE DE DONNÉES
# ============================================================

print("-" * 60)
print("ÉTAPE 3 - NETTOYAGE DE DONNÉES")
print("-" * 60)

def nom_invalid(valeur):
    if pd.isna(valeur): 
        return True
    valeur = str(valeur).strip()
    if valeur == "": 
        return True
    if valeur.isnumeric(): 
        return True
    if re.match(r'^[#\[&@?!]', valeur): 
        return True
    if valeur.lower() in ["null", "n/a", "none", "-", "???"]: 
        return True
    return False

def solde_invalid(valeur):
    if pd.isna(valeur): 
        return True
    try:
        return float(str(valeur).strip()) < 0
    except:
        return True

def pipeline_nettoyage(df):
    print(f"Avant nettoyage : {len(df)} lignes")

    # Doublons
    df = df.drop_duplicates()
    print(f"Après doublons : {len(df)} lignes")

    # Types
    df["solde"] = pd.to_numeric(df["solde"], errors="coerce")

    # Valeurs manquantes
    df["ville"]  = df["ville"].fillna("Inconnue")
    df["solde"]  = df["solde"].fillna(0)

    # Valeurs impossibles
    df = df[df["solde"] >= 0]
    print(f"Après nettoyage : {len(df)} lignes")

    # Standardisation texte
    df["nom"] = df["nom"].apply(lambda x: "Inconnu" if nom_invalid(x) else str(x).title())
    df["ville"] = df["ville"].str.strip().str.capitalize()
    df["forfait"] = df["forfait"].str.strip().str.title()

    print(f"Valeurs manquantes : {df.isnull().sum().sum()}")
    return df

df = pipeline_nettoyage(df)


# ============================================================
# ÉTAPE 4 - FILTRAGE ET SEGMENTATION
# ============================================================

print("-" * 60)
print("ÉTAPE 4 - FILTRAGE ET SEGMENTATION")
print("-" * 60)

# Abonnés actifs
actifs = df[df["actif"] == True]
print(f"Abonnés actifs : {len(actifs)}")
print(f"Abonnés inactifs : {len(df) - len(actifs)}")
print(f"Taux d'activité : {round(len(actifs)/len(df)*100, 1)}%")
print()

# Abonnés à risque - actifs avec solde faible
a_risque = df[df["actif"] & (df["solde"] < 1000)]
print(f"Abonnés à risque (actifs solde < 1000 FCFA) : {len(a_risque)}")
print(a_risque[["nom", "ville", "solde", "anciennete_mois"]].to_string())
print()

# Abonnés premium
premium = df[df["actif"] & (df["solde"] >= 8000)]
print(f"Abonnés premium (solde >= 8000 FCFA) : {len(premium)}")
print(premium[["nom", "ville", "solde", "forfait"]].to_string())


# ============================================================
# ÉTAPE 5 - AGRÉGATIONS ET KPIs PAR VILLE ET FORFAIT
# ============================================================

print("\n" + "-" * 60)
print("ÉTAPE 5 - AGRÉGATIONS ET KPIs")
print("-" * 60)

# KPIs globaux
print("=== KPIs GLOBAUX ===")
print(f"Solde moyen : {round(df['solde'].mean(), 2):,} FCFA")
print(f"Solde total : {int(df['solde'].sum()):,} FCFA")
print(f"Appels moyens/mois : {round(df['appels_mois'].mean(), 1)}")
print(f"Data moyenne : {round(df['data_go'].mean(), 2)} Go")
print(f"Ancienneté moyenne : {round(df['anciennete_mois'].mean(), 1)} mois")
print()

# Performance par ville
print("=== PERFORMANCE PAR VILLE ===")
perf_ville = df.groupby("ville").agg(
    nb_abonnes = ("nom", "count"),
    solde_moyen = ("solde", "mean"),
    solde_total = ("solde", "sum"),
    appels_moyens = ("appels_mois", "mean"),
    data_moyenne = ("data_go", "mean"),
    taux_actifs = ("actif", "mean")
).round(2).reset_index()

perf_ville["taux_actifs"] = (perf_ville["taux_actifs"] * 100).round(1)
perf_ville = perf_ville.sort_values("solde_total", ascending=False)
print(perf_ville.to_string())
print()

# Performance par forfait
print("=== PERFORMANCE PAR FORFAIT ===")
perf_forfait = df.groupby("forfait").agg(
    nb_abonnes = ("nom", "count"),
    solde_moyen = ("solde", "mean"),
    appels_moyens = ("appels_mois", "mean"),
    data_moyenne = ("data_go", "mean")
).round(2).reset_index()

perf_forfait = perf_forfait.sort_values("solde_moyen", ascending=False)
print(perf_forfait.to_string())


# ============================================================
# ÉTAPE 6 - FUSION DES TABLES
# ============================================================

print("\n" + "-" * 60)
print("ÉTAPE 6 - FUSION DES TABLES")
print("-" * 60)

# Abonnés + Forfaits
df_complet = pd.merge(df, df_forfaits, on="id_forfait", how="left")

# Abonnés + Transactions
df_complet = pd.merge(df_complet, df_trans, on="id_abonne", how="left")

print(f"Colonnes après fusion : {df_complet.columns.tolist()}")
print()

# Transactions par abonné
trans_par_abonne = df_complet.groupby("nom")["montant"].sum().reset_index()
trans_par_abonne.columns = ["nom", "total_transactions"]
trans_par_abonne = trans_par_abonne.sort_values("total_transactions", ascending=False)

print("=== TOP 5 ABONNÉS PAR TRANSACTIONS ORANGE MONEY ===")
print(trans_par_abonne.head(5).to_string())
print()

# Transactions par type
print("=== TRANSACTIONS PAR TYPE ===")
print(df_complet.groupby("type")["montant"].agg(total="sum", moyenne="mean", nombre="count").round(2))

# ============================================================
# ÉTAPE 7 - COLONNES CALCULÉES ET SCORE CLIENT
# ============================================================

print("\n" + "-" * 60)
print("ÉTAPE 7 - COLONNES CALCULÉES ET SCORE CLIENT")
print("-" * 60)

# Niveau de solde
df["niveau_solde"] = np.where(
    df["solde"] >= 8000, "Premium",
    np.where(df["solde"] >= 3000, "Standard",
    np.where(df["solde"] >= 1000, "Faible", "Critique"))
)

# Catégorie fidélité
def categorie_fidelite(mois):
    if mois >= 36:   
        return "Fidèle"
    elif mois >= 12: 
        return "Régulier"
    else:            
        return "Nouveau"

df["fidelite"] = df["anciennete_mois"].apply(categorie_fidelite)

# Statut activité
def statut_activite(ligne):
    if ligne["actif"]:
        return f"Actif depuis {ligne['anciennete_mois']} mois"
    else:
        return f"Inactif depuis {ligne['anciennete_mois']} mois"

df["statut"] = df.apply(statut_activite, axis=1)

# Score client
def calculer_score(ligne):
    return round(
        ligne["appels_mois"] * 0.4 +
        ligne["data_go"] * 10 +
        ligne["solde"]/1000 +
        ligne["anciennete_mois"] * 0.5,
        2
    )

df["score_client"] = df.apply(calculer_score, axis=1)

# Rang
df["rang"] = pd.cut(
    df["score_client"],
    bins=[0, 25, 50, 75, 200],
    labels=["Bronze", "Argent", "Or", "Platine"]
)

print("=== SCORES ET RANGS CLIENTS ===")
df_scores = df.sort_values("score_client", ascending=False)
print(df_scores[["nom", "ville", "niveau_solde",
                  "fidelite", "score_client", "rang"]].to_string())
print()

# Score moyen par niveau
print("Score moyen par niveau de solde :")
print(df.groupby("niveau_solde")["score_client"].mean().round(2))


# ============================================================
# ÉTAPE 8 - RAPPORT FINAL ET EXPORT
# ============================================================

print("\n" + "-" * 60)
print("ÉTAPE 8 - RAPPORT FINAL")
print("-" * 60)

print("=" * 60)
print("SYNTHÈSE - ORANGE BURKINA FASO ")
print("=" * 60)
print(f"Total abonnés : {len(df)}")
print(f"Abonnés actifs : {len(df[df['actif']])} ({round(df['actif'].mean()*100,1)}%)")
print(f"Solde moyen : {round(df['solde'].mean(),2):,} FCFA")
print(f"Solde total : {int(df['solde'].sum()):,} FCFA")
print()
print("Répartition par rang :")
print(df["rang"].value_counts())
print()
print("Répartition par fidélité :")
print(df["fidelite"].value_counts())
print()
print(f"Ville la plus rentable : {perf_ville.iloc[0]['ville']}")
print(f"Forfait le plus souscrit : {df['forfait'].value_counts().index[0]}")
print()

# Recommandations 
print("=== RECOMMANDATIONS ===")
nb_critique = len(df[df["niveau_solde"] == "Critique"])
nb_inactifs = len(df[~df["actif"]])
print(f"1. {nb_critique} abonnés en zone critique - campagne recharge urgente")
print(f"2. {nb_inactifs} abonnés inactifs - programme réactivation ciblé")
print(f"3. Ouaga concentre la valeur - priorité upselling Orange Max 10Go")

# Export
rapport_final = df[[
    "nom", "ville", "solde", "forfait", "actif",
    "appels_mois", "data_go", "anciennete_mois",
    "niveau_solde", "fidelite", "score_client", "rang"
]].sort_values("score_client", ascending=False)

rapport_final.to_csv("../output/rapport_final.csv", index=False, encoding="utf-8")
perf_ville.to_csv("../output/performance_villes.csv",    index=False, encoding="utf-8")
perf_forfait.to_csv("../output/performance_forfaits.csv", index=False, encoding="utf-8")

print()
print("Fichiers exportés dans output/")
print("rapport_final.csv")
print("performance_villes.csv")
print("performance_forfaits.csv")
print()
print("=" * 60)
print("  ANALYSE TERMINÉE")
print("=" * 60)
