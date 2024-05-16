import streamlit as st
import sqlite3
import pandas as pd

from cadastro import inserir_animal

# Função para inserir um novo animal no banco de dados

# Ler os dados da tabela animal e exibi-los em um DataFrame
def mostrar_animais():
    with sqlite3.connect('24-04-29\\db_pet.db') as conexao:
        return pd.read_sql_query("SELECT * FROM animal", conexao)

def mostrar_racas():
    with sqlite3.connect('24-04-29\\db_pet.db') as conexao:
        return pd.read_sql_query("SELECT id,name from racas r", conexao)


# Layout da interface
st.title('Cadastro de Animais')

# Exibir os animais atualmente cadastrados
animais = mostrar_animais()
st.table(animais)

racas=mostrar_racas()


# Formulário para adicionar um novo animal
col1, col2, col3 = st.columns(3)
raca = col1.selectbox('Selecione a raça',racas['name'], key='raça')
nome = col2.text_input('Digite o nome do animal', key='nome')
data_nascimento = col3.date_input('Selecione a data de nascimento', key='nascimento')
sexo = col1.number_input('Informe o Sexo do animal', key='sexo', min_value=0)
peso = col2.number_input('Informe o peso', key='peso', min_value=0)
altura = col3.number_input('Informe a altura', key='altura', min_value=0)

# Botão para enviar os dados
if st.button('Enviar dados'):
    id_raca=int(racas.loc[racas['name'] == raca, 'id'].values[0])
    print(id_raca)
    inserir_animal(nome, id_raca, data_nascimento, sexo, peso, altura)   
    st.success('Animal cadastrado com sucesso!')
    