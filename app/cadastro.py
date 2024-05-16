import sqlite3
import pandas as pd
conexao = sqlite3.connect('24-04-29\\db_pet.db') 
c = conexao.cursor()

def inserir_animal(nome, id_raca, data_nascimento, sexo, peso, altura):
    try:
        with sqlite3.connect('24-04-29\\db_pet.db') as conexao:
            cursor = conexao.cursor()
            sql = '''INSERT INTO animal(nome, id_raca, data_nascimento, sexo, peso, altura)
                     VALUES (?, ?, ?, ?, ?, ?)'''
            cursor.execute(sql, (nome, id_raca, data_nascimento, sexo, peso, altura))
            conexao.commit()
        return True
    except Exception as e:
        #st.error(f'Ocorreu um erro ao inserir o animal: {e}')
        return False