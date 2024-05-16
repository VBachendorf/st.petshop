import sqlite3
conexao = sqlite3.connect('24-04-29\\db_pet.db') 
c = conexao.cursor()
def criar_tabelas():
    c.execute('''
    CREATE TABLE IF NOT EXISTS especies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        is_mamifero INTEGER,
        familia TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS racas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_especie INTEGER,
        name TEXT,
        name_cientifico TEXT,
        CONSTRAINT especies_FK FOREIGN KEY (id_especie) REFERENCES especies(id)
    )
    ''')

    conexao.commit()


def edit():
    c.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        data_nascimento DATE,
        sexo TEXT,
        contato INTEGER,
        cidade TEXT,
        data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);
    ''')
    c.execute('''
              drop table animal;
              ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS animal (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        id_raca INTEGER,
        id_pessoa INTEGER,
        data_nascimento DATE,
        sexo TEXT,
        peso REAL,
        altura REAL,
        CONSTRAINT racas_FK FOREIGN KEY (id_raca) REFERENCES racas(id)
        CONSTRAINT pessoas_fk FOREIGN KEY (id_pessoa) REFERENCES pessoas(id)
    );
              ''')
    
    conexao.commit()

edit()
