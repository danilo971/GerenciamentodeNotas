import sqlite3

# Nome do arquivo do banco de dados
banco = "bd.db"

# Conexão com o banco de dados (será criado automaticamente se não existir)
conexao = sqlite3.connect(banco)

# Código SQL para criar as tabelas
sql_criacao = """
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    tipo_usuario TEXT NOT NULL CHECK (tipo_usuario IN ('Coordenador', 'Professor', 'Aluno'))
);

CREATE TABLE IF NOT EXISTS cursos (
    id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_curso TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS disciplinas (
    id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_disciplina TEXT NOT NULL,
    id_curso INTEGER NOT NULL,
    FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);

CREATE TABLE IF NOT EXISTS notas (
    id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    nota REAL NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES usuarios (id_usuario),
    FOREIGN KEY (id_disciplina) REFERENCES disciplinas (id_disciplina)
);

CREATE TABLE IF NOT EXISTS faltas (
    id_falta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    quantidade_faltas INTEGER NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES usuarios (id_usuario),
    FOREIGN KEY (id_disciplina) REFERENCES disciplinas (id_disciplina)
);
"""

# Execução do código SQL
try:
    cursor = conexao.cursor()
    cursor.executescript(sql_criacao)
    print("Banco de dados e tabelas criados com sucesso!")
except sqlite3.Error as erro:
    print("Erro ao criar o banco de dados:", erro)
finally:
    # Fechar a conexão
    conexao.close()
