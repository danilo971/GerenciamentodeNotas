import customtkinter as ctk
import sqlite3
from tkinter import ttk

class ListAlunos(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(pady=20, padx=20, fill="both", expand=True)

        # Configurar layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Criar tabela
        self.tabela = ttk.Treeview(self, columns=("Nome Completo", "Semestre"), show="headings", height=15)
        self.tabela.heading("Nome Completo", text="Nome Completo")
        self.tabela.heading("Semestre", text="Periodo")
        self.tabela.column("Nome Completo", width=200, anchor="center")
        self.tabela.column("Semestre", width=150, anchor="center")
        self.tabela.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Scrollbar para a tabela
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Carregar dados do banco
        self.carregar_dados()

    def carregar_dados(self):
        try:
            # Conectar ao banco de dados
            conexao = sqlite3.connect("bd.db")
            cursor = conexao.cursor()

            # Consultar dados
            cursor.execute("SELECT nome, sobrenome, semestre_ingresso FROM alunos")
            resultados = cursor.fetchall()

            # Adicionar dados à tabela
            for linha in resultados:
                nome_completo = f"{linha[0]} {linha[1]}"
                self.tabela.insert("", "end", values=(nome_completo, linha[2]))

            # Fechar conexão
            conexao.close()
        except sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados: {e}")
