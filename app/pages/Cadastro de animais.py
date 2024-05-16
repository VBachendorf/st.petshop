import streamlit as st
import pandas as pd
import sqlite3
conn = sqlite3.connect('24-04-29\\db_pet.db')
def db_cadastro_especie(nome,is_mamifero,nome_familia):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO especies
        (name, is_mamifero, familia)
        VALUES (?, ?, ?)""",
        (nome, is_mamifero, nome_familia))
        conn.commit()
    except Exception as e:
        st.error(f"Erro ao cadastrar a espécie: {e}")
    finally:
        conn.close()

def db_cadastro_raca(nome,id_especie,nome_cientifico):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO racas
        (id_especie, name, name_cientifico)
        VALUES (?, ?, ?)""",
        (id_especie, nome, nome_cientifico))
        conn.commit()
    except Exception as e:
        st.error(f"Erro ao cadastrar a espécie: {e}")
    finally:
        conn.close()

def db_cadastro_animal(nome,id_raca,id_pessoa,data_nascimento,sexo,peso,altura):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO animal
        (nome, id_raca, id_pessoa, data_nascimento, sexo, 
        peso, altura)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (nome,id_raca,id_pessoa,data_nascimento,sexo,peso,altura))
        conn.commit()
    except Exception as e:
        st.error(f"Erro ao cadastrar a espécie: {e}")
    finally:
        conn.close()

def mostrar_especies():
    with sqlite3.connect('24-04-29\\db_pet.db') as conexao:
        return pd.read_sql_query("SELECT id, name  FROM especies", conexao)
especies=mostrar_especies()

def mostrar_racas():
    with sqlite3.connect('24-04-29\\db_pet.db') as conexao:
        return pd.read_sql_query("SELECT id_especie as id, name  FROM racas", conexao)
racas=mostrar_racas()

def mostrar_pessoa():
    with sqlite3.connect('24-04-29\\db_pet.db') as conexao:
        return pd.read_sql_query("SELECT id, nome as name  FROM pessoas", conexao)
pessoa=mostrar_pessoa()


st.title('Cadastro de Animais !')
tab1,tab2,tab3 = st.tabs(['Animal','Espécie','Raça'])
#---------------------------PRIMEIRA ABA
with tab3:
    col1,col2,col3=st.columns(3)
    a=col1.text_input('digite o nome da Espécie')
    b=col2.radio('o animal é mamífero',['Sim','Não'])
    c=col3.text_input('nome de familia do animal',key='ass')
    if col2.button('cadastro especie'):
        if b=='Não':
            b=0
        else:
            b=1
        st.write(b)
        db_cadastro_especie(a,b,c)

#---------------------------SEGUNDA ABA
with tab2:
    col1,col2,col3=st.columns(3)
    a=col1.text_input('digite o nome da Raça')
    b=col2.selectbox('selecione a Espécie',especies['name'])
    c=col3.text_input('nome cientifico do',key='asss')
    if col2.button('cadastro'):
        id_especie=int(especies.loc[especies['name'] == b, 'id'].values[0])
        db_cadastro_raca(a,id_especie,c)
        st.success('Raça cadastrada')
#-------------------------PRIMEIRA ABA
with tab1:
    col1,col2,col3=st.columns(3)
    a=col1.text_input('digite o nome do animal')
    b=col2.selectbox('selecione a Raca',racas['name'])
    c=col3.selectbox('Priprietário do animal',pessoa['name'],key='s')
    d=col1.date_input('Data de nascimento')
    e=col2.radio('Sexo do animal',['Masc','Fem'])
    f=col3.number_input('Peso do Animal',min_value=0.1)
    g=col1.number_input('Altura do Pet em cm')
    if st.button("cadastrar Animal"):
        id_raca=int(racas.loc[racas['name'] == b, 'id'].values[0])
        id_pessoa=int(pessoa.loc[pessoa['name'] == c, 'id'].values[0])
        if e=='Fem':
            b=0
        else:
            b=1
        st.write(a,id_raca,id_pessoa,d,e,f,g)
        db_cadastro_animal(a,id_raca,id_pessoa,d,e,f,g)