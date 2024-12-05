import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class BackEnd:
    def connect_db(self):
        """Conecta ao banco de dados."""
        self.conn = sqlite3.connect("bd.db")
        self.cursor = self.conn.cursor()

    def disconnect_db(self):
        """Desconecta do banco de dados."""
        self.conn.close()

class AplicativoCadastroProfessor(BackEnd):
    def __init__(self):
        # Configuração principal
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Inicializa a janela principal
        self.janela = ctk.CTk()
        self.janela.title("Aplicativo de Registro")
        self.janela.geometry("500x400")
        self.janela.resizable(False, False)

        # Variáveis
        self.aceitar_var = ctk.StringVar(value="Não Aceito")
        self.status_var = ctk.StringVar(value="Não Matriculado")

        # Elementos da interface
        self.criar_interface()

        # Inicia o loop principal
        self.janela.mainloop()

    def criar_interface(self):
        """Cria os elementos da interface do usuário."""
        frame = ctk.CTkFrame(self.janela)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Frame para informações do usuário
        self.criar_frame_usuario(frame)

        # Botão enviar
        botao_enviar = ctk.CTkButton(frame, text="Enviar", command=self.salvar_dados)
        botao_enviar.grid(row=3, column=0, padx=10, pady=10)

    def criar_frame_usuario(self, parent):
        """Cria o frame para informações do aluno."""
        frame_usuario = ctk.CTkFrame(parent)
        frame_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        titulo_usuario = ctk.CTkLabel(frame_usuario, text="Informações do Professor",
                                      font=ctk.CTkFont(size=16, weight="bold"))
        titulo_usuario.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # Campos de entrada para o usuário
        ctk.CTkLabel(frame_usuario, text="Primeiro Nome").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_primeiro_nome = ctk.CTkEntry(frame_usuario)
        self.entrada_primeiro_nome.grid(row=2, column=0, padx=5, pady=5)

        ctk.CTkLabel(frame_usuario, text="Último Nome").grid(row=1, column=1, padx=5, pady=5)
        self.entrada_ultimo_nome = ctk.CTkEntry(frame_usuario)
        self.entrada_ultimo_nome.grid(row=2, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_usuario, text="CPF").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_cpf = ctk.CTkEntry(frame_usuario)
        self.entrada_cpf.grid(row=2, column=2, padx=5, pady=5)

        ctk.CTkLabel(frame_usuario, text="Data de Nascimento").grid(row=3, column=0, padx=5, pady=5)
        self.entrada_data_nascimento = ctk.CTkEntry(frame_usuario, placeholder_text="DD/MM/AAAA")
        self.entrada_data_nascimento.grid(row=4, column=0, padx=5, pady=5)

        ctk.CTkLabel(frame_usuario, text="Nacionalidade").grid(row=3, column=1, padx=5, pady=5)
        self.combobox_nacionalidade = ctk.CTkComboBox(frame_usuario, values=["Brasileiro", "Estrangeiro"])
        self.combobox_nacionalidade.grid(row=4, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_usuario, text="Selecione a Disciplina").grid(row=3, column=2, padx=5, pady=5)
        self.combo_disciplina = ttk.Combobox(frame_usuario, state="readonly", values=self.carregar_disciplinas())
        self.combo_disciplina.grid(row=4, column=2, padx=5, pady=5)

    def carregar_disciplinas(self):
        """Carrega as disciplinas do banco de dados para a combobox."""
        self.connect_db()
        self.cursor.execute("SELECT nome_disciplina FROM disciplinas")
        disciplinas = [linha[0] for linha in self.cursor.fetchall()]
        self.disconnect_db()
        return disciplinas

    def salvar_dados(self):
        """Lógica para salvar os dados inseridos pelo usuário."""
        try:
            # Captura os dados
            self.nome = self.entrada_primeiro_nome.get()
            self.sobrenome = self.entrada_ultimo_nome.get()
            self.cpf = self.entrada_cpf.get()
            self.dataNascimento = self.entrada_data_nascimento.get()
            self.nacionalidade = self.combobox_nacionalidade.get()
            self.disciplina = self.combo_disciplina.get()

            # Verifica os campos obrigatórios
            if not self.nome or not self.sobrenome or not self.cpf or not self.dataNascimento or not self.nacionalidade:
                messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")
                return

            if not self.disciplina:
                messagebox.showwarning("Erro", "Você deve selecionar uma disciplina.")
                return

            self.connect_db()

            # Verifica se o professor já existe no banco
            self.cursor.execute(
                """
                INSERT INTO professores (nome, sobrenome, cpf, data_nascimento, nacionalidade, disciplina)
                VALUES (?, ?, ?, ?, ?, ?)
                """, 
                (self.nome, self.sobrenome, self.cpf, self.dataNascimento, self.nacionalidade, self.disciplina))
            id_professor = self.cursor.lastrowid

            # Relaciona o professor com a disciplina
            self.cursor.execute("SELECT id_disciplina FROM disciplinas WHERE nome_disciplina = ?", (self.disciplina,))
            id_disciplina = self.cursor.fetchone()[0]

            self.cursor.execute(
                "INSERT INTO professores_disciplinas (id_professor, id_disciplina) VALUES (?, ?)",
                (id_professor, id_disciplina)
            )

            self.conn.commit()
            messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")

        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Esse professor ou relação já foi cadastrada.")
        except sqlite3.Error as erro:
            print(f"Erro no banco de dados: {erro}")
            messagebox.showerror("Erro no Banco de Dados", f"Erro ao salvar professor: {erro}")
        finally:
            self.disconnect_db()

        self.janela.destroy()

if __name__ == "__main__":
    app = AplicativoCadastroProfessor()
