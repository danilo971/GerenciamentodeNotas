import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

# Cria a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores_disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_professor INTEGER NOT NULL,
        id_disciplina INTEGER NOT NULL,
        FOREIGN KEY (id_professor) REFERENCES professores (id),
        FOREIGN KEY (id_disciplina) REFERENCES disciplinas (id)
    );
''')

# Confirma a operação e fecha a conexão
conn.commit()
conn.close()
