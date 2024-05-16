import streamlit as st
import sqlite3
import pandas as pd
consulta_animal =  """
SELECT
a.nome as nome,
DATE('now') - a.data_nascimento as idade,
r.name as raça, 
e.name as animal,
p.nome as dono
FROM animal a
left join racas r on
	a.id_raca = r.id
LEFT join especies e on
	r.id_especie = e.id
left join pessoas p on
    p.id = a.id_pessoa    

"""
def mostrar_animais():
    with sqlite3.connect('24-04-29\\db_pet.db') as conexao:
        return pd.read_sql_query(consulta_animal, conexao)


df = mostrar_animais()

# Adiciona a opção 'Mostrar todos'
opcoes = df['animal'].unique().tolist()
opcoes.append('Mostrar todos')
opcoes2 = df['raça'].unique().tolist()
opcoes2.append('Mostrar todos')


# Seleciona o animal usando um selectbox
col1, col2 = st.columns(2)
animal_selecionado = col1.selectbox('Selecione o animal', opcoes)
raca_selecionada = col2.selectbox('Selecione a raça', opcoes2)

# Filtra o DataFrame com base no animal selecionado
if animal_selecionado == 'Mostrar todos':
    df_filtrado = df
else:
    df_filtrado = df.loc[df['animal'] == animal_selecionado]

# Exibe o DataFrame filtrado

st.dataframe(df_filtrado)