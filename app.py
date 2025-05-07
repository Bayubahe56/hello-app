import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")
# Exemple : ton DataFrame
df = pd.read_csv("Dadoseducationais/population.csv")

# Affiche le DataFrame pour déboguer
st.write(df)

 
