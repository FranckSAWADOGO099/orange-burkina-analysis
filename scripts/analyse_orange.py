# ============================================================
# PROJET 1 - ANALYSE DES ABONNÉS ORANGE BURKINA FASO
# Auteur: Franck SAWADOGO
# Outils: Python, pandas, numpy
# Données: Dataset fictif abonnés Orange Burkina (9600 abonnés générés)
# ============================================================

import pandas as pd
import numpy as np
import os
import re

# Configuration
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("../data", exist_ok=True)
os.makedirs("../output", exist_ok=True)

print("=" * 60)
print("  ANALYSE ABONNÉS ORANGE BURKINA FASO")
print("=" * 60)


# ============================================================
# ETAPE 1 - CRÉATION DES DONNÉES (9600 abonnés générés)
# ============================================================

def creer_donnees():
    rng = np.random.default_rng(42)  # seed fixe -> résultats reproductibles

    NB_ABONNES = 5000

    prenoms = [
        "Aminata", "Seydou", "Mariam", "Ibrahim", "Fatima", "Kofi", "Salif",
        "Amina", "Adama", "Safi", "Binta", "Moussa", "Aissata", "Rasmane",
        "Clarisse", "Issa", "Awa", "Boukary", "Hawa", "Yacouba", "Rokia",
        "Hamidou", "Bintou", "Drissa", "Mamadou", "Assita", "Idrissa",
        "Korotoumou", "Lassina", "Nathalie", "Ousmane", "Ramata", "Sibiri",
        "Tenin", "Wendpouire", "Zalissa", "Abdoulaye", "Djeneba", "Karim",
        "Madina",
    ]

    noms = [
        "Ouedraogo", "Traore", "Sawadogo", "Kone", "Coulibaly", "Ouattara",
        "Zongo", "Diallo", "Bambara", "Ouoba", "Kabore", "Tapsoba", "Nana",
        "Ilboudo", "Toe", "Sanou", "Kafando", "Compaore", "Nikiema", "Yameogo",
        "Bationo", "Sankara", "Some", "Kaboret", "Dabire", "Zoungrana",
        "Kientega", "Bayala", "Tiendrebeogo", "Sib", "Ouili", "Konate",
        "Diarra", "Sidibe", "Barry", "Maiga",
    ]

    villes = ["Ouaga", "Bobo", "Koudougou", "Banfora", "Ouahigouya", "Kaya",
              "Tenkodogo", "Fada N'Gourma", "Dedougou", "Gaoua"]

    forfaits_def = [
        {"id_forfait": 1, "nom_forfait": "Orange Liberté",  "prix_fcfa": 1500, "data_incluse_go": 2.0,  "appels_inclus": 30},
        {"id_forfait": 2, "nom_forfait": "Orange Max 5Go",  "prix_fcfa": 3500, "data_incluse_go": 5.0,  "appels_inclus": 60},
        {"id_forfait": 3, "nom_forfait": "Orange Max 10Go", "prix_fcfa": 6000, "data_incluse_go": 10.0, "appels_inclus": 120},
    ]
    forfait_par_id = {f["id_forfait"]: f for f in forfaits_def}

    abonnes = []
    for i in range(1, NB_ABONNES + 1):
        id_forfait = int(rng.choice([1, 2, 3], p=[0.35, 0.35, 0.30]))
        actif = bool(rng.random() < 0.75)

        # Solde corrélé au forfait + un peu de hasard (et parfois 0)
        base_solde = {1: 2000, 2: 4500, 3: 8000}[id_forfait]
        solde = max(0, int(rng.normal(base_solde, base_solde * 0.6)))
        if rng.random() < 0.10:
            solde = 0

        anciennete_mois = int(rng.integers(1, 60))

        # Appels/data cohérents avec le forfait inclus, sauf si inactif
        appels_inclus = forfait_par_id[id_forfait]["appels_inclus"]
        data_incluse = forfait_par_id[id_forfait]["data_incluse_go"]

        if actif:
            appels_mois = max(0, int(rng.normal(appels_inclus * 0.7, appels_inclus * 0.3)))
            data_go = round(max(0.0, rng.normal(data_incluse * 0.6, data_incluse * 0.3)), 1)
        else:
            appels_mois = int(rng.integers(0, 5))
            data_go = round(float(rng.uniform(0, 0.5)), 1)

        abonnes.append({
            "id_abonne": i,
            "nom": f"{rng.choice(prenoms)} {rng.choice(noms)}",
            "ville": rng.choice(villes),
            "solde": solde,
            "forfait": forfait_par_id[id_forfait]["nom_forfait"],
            "actif": actif,
            "appels_mois": appels_mois,
            "data_go": data_go,
            "anciennete_mois": anciennete_mois,
            "id_forfait": id_forfait,
        })

    forfaits = forfaits_def

    # Transactions Orange Money : ~40% des abonnés en ont 1 à 3
    transactions = []
    for ab in abonnes:
        if rng.random() < 0.40:
            nb_trans = int(rng.integers(1, 4))
            for _ in range(nb_trans):
                transactions.append({
                    "id_abonne": ab["id_abonne"],
                    "montant": int(rng.integers(500, 30000)),
                    "type": str(rng.choice(["envoi", "retrait"], p=[0.6, 0.4])),
                })

    pd.DataFrame(abonnes).to_csv("../data/abonnes.csv",      index=False, encoding="utf-8")
    pd.DataFrame(forfaits).to_csv("../data/forfaits.csv",     index=False, encoding="utf-8")
    pd.DataFrame(transactions).to_csv("../data/transactions.csv", index=False, encoding="utf-8")
    print(f"Fichiers CSV créés dans data ({len(abonnes)} abonnés, {len(transactions)} transactions)")

creer_donnees()


# ============================================================
# ÉTAPE 2 - CHARGEMENT ET EXPLORATION
# ============================================================

print("\n" + "-" * 60)
print("ÉTAPE 2 - CHARGEMENT ET EXPLORATION")
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
print("\n" + "-" * 60)
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
print("\n" + "-" * 60)
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
print(a_risque[["nom", "ville", "solde", "anciennete_mois"]].head(10).to_string())
print("..." if len(a_risque) > 10 else "")
print()

# Abonnés premium
premium = df[df["actif"] & (df["solde"] >= 8000)]
print(f"Abonnés premium (solde >= 8000 FCFA) : {len(premium)}")
print(premium[["nom", "ville", "solde", "forfait"]].head(10).to_string())
print("..." if len(premium) > 10 else "")


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
    nb_abonnes =("nom", "count"),
    solde_moyen =("solde","mean"),
    solde_total =("solde","sum"),
    appels_moyens =("appels_mois","mean"),
    data_moyenne =("data_go", "mean"),
    taux_actifs =("actif","mean")
).round(2).reset_index()

perf_ville["taux_actifs"] = (perf_ville["taux_actifs"] * 100).round(1)
perf_ville = perf_ville.sort_values("solde_total", ascending=False)
print(perf_ville.to_string())
print()

# Performance par forfait
print("=== PERFORMANCE PAR FORFAIT ===")
perf_forfait = df.groupby("forfait").agg(
    nb_abonnes = ("nom","count"),
    solde_moyen = ("solde","mean"),
    appels_moyens = ("appels_mois","mean"),
    data_moyenne = ("data_go","mean")
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
    if mois >= 36:   return "Fidèle"
    elif mois >= 12: return "Régulier"
    else:            return "Nouveau"

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
        ligne["solde"]/ 1000 +
        ligne["anciennete_mois"] * 0.5,
        2
    )

df["score_client"] = df.apply(calculer_score, axis=1)

# Rang
df["rang"] = pd.cut(
    df["score_client"],
    bins=[0, 25, 50, 75, np.inf],
    labels=["Bronze", "Argent", "Or", "Platine"]
)

print("=== SCORES ET RANGS CLIENTS (TOP 15) ===")
df_scores = df.sort_values("score_client", ascending=False)
print(df_scores[["nom", "ville", "niveau_solde",
                  "fidelite", "score_client", "rang"]].head(15).to_string())
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
print("  SYNTHÈSE - ORANGE BURKINA FASO")
print("=" * 60)
print(f"Total abonnés      : {len(df)}")
print(f"Abonnés actifs     : {len(df[df['actif']])} ({round(df['actif'].mean()*100,1)}%)")
print(f"Solde moyen        : {round(df['solde'].mean(),2):,} FCFA")
print(f"Solde total        : {int(df['solde'].sum()):,} FCFA")
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
print(f"1. {nb_critique} abonnés en zone critique — campagne recharge urgente")
print(f"2. {nb_inactifs} abonnés inactifs — programme réactivation ciblé")
print(f"3. Ouaga concentre la valeur — priorité upselling Orange Max 10Go")

# Export
rapport_final = df[[
    "nom", "ville", "solde", "forfait", "actif",
    "appels_mois", "data_go", "anciennete_mois",
    "niveau_solde", "fidelite", "score_client", "rang"
]].sort_values("score_client", ascending=False)

rapport_final.to_csv("../output/rapport_final.csv", index=False, encoding="utf-8")
perf_ville.to_csv("../output/performance_villes.csv", index=False, encoding="utf-8")
perf_forfait.to_csv("../output/performance_forfaits.csv", index=False, encoding="utf-8")

print()
print("Fichiers exportés dans output/")
print("rapport_final.csv")
print("performance_villes.csv")
print("performance_forfaits.csv")
print()
print("=" * 60)
print("ANALYSE TERMINÉE")
print("=" * 60)
