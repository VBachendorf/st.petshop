import streamlit as st
import sqlite3
import pandas as pd
consulta_cliente =  """
SELECT 
p.nome,
p.contato,
p.cidade,
p.sexo,
p.data_nascimento
from pessoas p 
"""
def mostrar_cliente():
    with sqlite3.connect('24-04-29\\db_pet.db') as conexao:
        return pd.read_sql_query(consulta_cliente, conexao)


df = mostrar_cliente()

# Adiciona a opção 'Mostrar todos'
opcoes = df['nome'].unique().tolist()
opcoes.append('Mostrar todos')



# Seleciona o animal usando um selectbox
col1, col2 = st.columns(2)
select_cliente = col1.selectbox('Selecione o Cliente', opcoes)

# Filtra o DataFrame com base no animal selecionado
if select_cliente == 'Mostrar todos':
    df_filtrado = df
else:
    df_filtrado = df.loc[df['nome'] == select_cliente]

# Exibe o DataFrame filtrado

st.dataframe(df_filtrado)