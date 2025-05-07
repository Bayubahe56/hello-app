
  GNU nano 7.2                                                                                    app.py                                                                                              
st.write("""
# My first app
Hello *world!*
""")

#import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titre
st.title("Escolas por Região e Ano do Censo")

# Charger les données
df = pd.read_csv("Dadoseducationais/My_data.csv")

# Convertir les années en type entier (juste au cas où)
df["NU_ANO_CENSO"] = df["NU_ANO_CENSO"].astype(int)

# Sélecteur d'année
anos = sorted(df["NU_ANO_CENSO"].unique())
ano_selecionado = st.selectbox("Sélectionnez l'année du censo :", anos)

# Filtrer les données
df_filtrado = df[df["NU_ANO_CENSO"] == ano_selecionado]

# Afficher les données filtrées
st.write(f"Nombre d'écoles par région en {ano_selecionado}")
st.dataframe(df_filtrado)

# Créer le graphique
fig, ax = plt.subplots()
ax.bar(df_filtrado["NO_REGIAO"], df_filtrado["Numero_Escolas"], color='skyblue')
ax.set_xlabel("Région")
ax.set_ylabel("Nombre d'écoles")
ax.set_title(f"Nombre d'écoles par région - {ano_selecionado}")
plt.xticks(rotation=45)

# Afficher le graphique
st.pyplot(fig)
