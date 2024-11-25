import sqlite3

# Nome do arquivo do banco de dados
banco = "bd.db"

# Conexão com o banco de dados
conexao = sqlite3.connect(banco)

# Código SQL para criar a tabela diretamente
sql_criacao = """
CREATE TABLE IF NOT EXISTS alunos (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    data_nascimento TEXT NOT NULL,
    nacionalidade TEXT NOT NULL CHECK (nacionalidade IN ('Brasileiro', 'Estrangeiro')),
    semestre_ingresso INTEGER NOT NULL CHECK (semestre_ingresso BETWEEN 1 AND 8)
);
"""

# Execução do código SQL
try:
    cursor = conexao.cursor()
    cursor.execute(sql_criacao)
    print("Tabela 'alunos' criada com sucesso!")
except sqlite3.Error as erro:
    print("Erro ao criar a tabela 'alunos':", erro)
finally:
    # Fechar a conexão
    conexao.close()
