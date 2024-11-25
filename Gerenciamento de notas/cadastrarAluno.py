import customtkinter as ctk
from tkinter import messagebox
import sqlite3

class backEnd:
    def connect_db(self):
        self.conn = sqlite3.connect("bd.db")
        self.cursor = self.conn.cursor()

    def disconnect_db(self):
        self.conn.close()

class AplicativoRegistro(backEnd):
    def __init__(self):
        # Configuração principal
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Inicializa a janela principal
        self.janela = ctk.CTk()
        self.janela.title("Aplicativo de Registro")
        self.janela.geometry("600x500")
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

        # Frame para informações do curso
        self.criar_frame_cursos(frame)

        # Frame para termos e condições
        self.criar_frame_termos(frame)

        # Botão enviar
        botao_enviar = ctk.CTkButton(frame, text="Enviar", command=self.salvar_dados)
        botao_enviar.grid(row=3, column=0, padx=10, pady=10)

    def criar_frame_usuario(self, parent):
        """Cria o frame para informações do aluno."""
        frame_usuario = ctk.CTkFrame(parent)
        frame_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        titulo_usuario = ctk.CTkLabel(frame_usuario, text="Informações do Aluno",
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

    def criar_frame_cursos(self, parent):
        """Cria o frame para informações do curso."""
        frame_cursos = ctk.CTkFrame(parent)
        frame_cursos.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        titulo_cursos = ctk.CTkLabel(frame_cursos, text="Informações do Curso",
                                     font=ctk.CTkFont(size=16, weight="bold"))
        titulo_cursos.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # Campos de entrada para o curso
        ctk.CTkLabel(frame_cursos, text="Turma do Curso").grid(row=1, column=0, padx=5, pady=5)
        self.spinbox_cursos = ctk.CTkComboBox(frame_cursos, values=["1 - Sistema de Informação", "2 - Sistema de Informação", "3 - Sistema de Informação", "4 - Sistema de Informação", "5 - Sistema de Informação", "6 - Sistema de Informação", "7 - Sistema de Informação", "8 - Sistema de Informação"])
        self.spinbox_cursos.grid(row=2, column=0, padx=5, pady=5)

    def salvar_dados(self):
        """Lógica para salvar os dados inseridos pelo usuário."""
        try:
            # Captura os dados
            self.nome = self.entrada_primeiro_nome.get()
            self.sobrenome = self.entrada_ultimo_nome.get()
            self.cpf = self.entrada_cpf.get()
            self.dataNascimento = self.entrada_data_nascimento.get()
            self.nacionalidade = self.combobox_nacionalidade.get()
            self.semestre_selecionado = int(self.spinbox_cursos.get().split(" ")[0])

            # Verifica os campos obrigatórios
            if not self.nome or not self.sobrenome or not self.cpf or not self.dataNascimento or not self.nacionalidade:
                messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")
                return

            # Conecta ao banco e insere os dados
            self.connect_db()
            self.cursor.execute(
                """
                INSERT INTO alunos (nome, sobrenome, cpf, data_nascimento, nacionalidade, semestre_ingresso)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (self.nome, self.sobrenome, self.cpf, self.dataNascimento, self.nacionalidade, self.semestre_selecionado)
            )
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Aluno registrado com sucesso!")

        except sqlite3.Error as erro:
            if "UNIQUE constraint failed: alunos.cpf" in str(erro):
                messagebox.showerror("Erro", "CPF já cadastrado!")
            else:
                print(f"Erro: {erro}")
                messagebox.showerror("Erro no Banco de Dados", f"Erro ao adicionar aluno: {erro}")
        finally:
            self.disconnect_db()

    def criar_frame_termos(self, parent):
        """Cria o frame para os termos e condições."""
        print("Método criar_frame_termos foi chamado")
        frame_termos = ctk.CTkFrame(parent)
        ...

if __name__ == "__main__":
    app = AplicativoRegistro()
