import sqlite3

# Conexão com o banco
conexao = sqlite3.connect("bd.db")
cursor = conexao.cursor()

# Inserir dados iniciais
dados_iniciais = [
    ("Admin", "coordenador@teste.com", "1234", "Coordenador"),
    ("João Silva", "professor@teste.com", "1234", "Professor"),
    ("Maria Souza", "aluno@teste.com", "1234", "Aluno"),
]

try:
    cursor.executemany("INSERT INTO usuarios (nome, email, senha, tipo_usuario) VALUES (?, ?, ?, ?)", dados_iniciais)
    conexao.commit()
    print("Dados iniciais inseridos com sucesso!")
except sqlite3.IntegrityError as e:
    print(f"Erro: {e}")
finally:
    conexao.close()
