import customtkinter as ctk
from tkinter import messagebox
import sqlite3

class BackEnd:
    def connect_db(self):
        """Conecta ao banco de dados."""
        self.conn = sqlite3.connect("bd.db")
        self.cursor = self.conn.cursor()

    def disconnect_db(self):
        """Desconecta do banco de dados."""
        self.conn.close()

class AplicativoDisciplina(BackEnd):
    def __init__(self):
        # Configuração principal
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Inicializa a janela principal
        self.janela = ctk.CTk()
        self.janela.title("Cadastro de Disciplinas")
        self.janela.geometry("400x300")
        self.janela.resizable(False, False)

        # Elementos da interface
        self.criar_interface()

        # Inicia o loop principal
        self.janela.mainloop()

    def criar_interface(self):
        """Cria os elementos da interface do usuário."""
        frame = ctk.CTkFrame(self.janela)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        titulo = ctk.CTkLabel(frame, text="Cadastro de Disciplinas",
                              font=ctk.CTkFont(size=18, weight="bold"))
        titulo.pack(pady=10)

        # Campo para nome da disciplina
        ctk.CTkLabel(frame, text="Nome da Disciplina").pack(pady=5)
        self.entrada_nome_disciplina = ctk.CTkEntry(frame, placeholder_text="Ex: POO")
        self.entrada_nome_disciplina.pack(pady=5)

        # Botão para salvar disciplina
        botao_salvar = ctk.CTkButton(frame, text="Salvar Disciplina", command=self.salvar_disciplina)
        botao_salvar.pack(pady=10)

    def salvar_disciplina(self):
        try:
        
            self.nome_disciplina = self.entrada_nome_disciplina.get().strip()

            if not self.nome_disciplina:
                messagebox.showwarning("Erro", "O nome da disciplina não pode estar vazio.")
                return

        
            self.connect_db()
            self.cursor.execute(
                """
                INSERT INTO disciplinas (nome_disciplina)
                VALUES (?)
                """,
                (self.nome_disciplina,)
            )
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Disciplina cadastrada com sucesso!")

        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Essa disciplina já foi cadastrada.")
        except sqlite3.Error as erro:
            print(f"Erro no banco de dados: {erro}")
            messagebox.showerror("Erro no Banco de Dados", f"Erro ao salvar disciplina: {erro}")

        self.janela.destroy()

if __name__ == "__main__":
    app = AplicativoDisciplina()
