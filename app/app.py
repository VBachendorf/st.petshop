import streamlit as st
import sqlite3
import pandas as pd
from cadastro import inserir_animal
image_dir='images/cat.png'
# Função para inserir um novo animal no banco de dados
x=st.container()
x.title('🐈 PetShop CuidaBicho ✅')
st.write(" Seu animal pode matar a fome na china 🍖")
st.write('confira algumas receitas da culinária chinesa')
