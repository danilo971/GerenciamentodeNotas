import customtkinter as ctk
from PIL import Image
from cadastrarAluno import AplicativoRegistro

class MenuCoordenador(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(pady=20, padx=20, fill="both", expand=True)

        # Configuração do grid
        self.grid_columnconfigure((0, 4), weight=1)  # Colunas externas
        self.grid_columnconfigure((1, 2, 3), weight=0)  # Colunas dos botões
        self.grid_rowconfigure(1, weight=1)  # Linha 1 se expande

        # Botões
        self.imagem_aluno = self.adicionar_aluno()
        self.botao = ctk.CTkButton(self, image=self.imagem_aluno, text="    Adicionar Aluno    ", compound="left", command=AplicativoRegistro)
        self.botao.grid(row=1, column=1, padx=20, pady=10)

        self.imagem_professor = self.adicionar_professor()
        self.botaoProfessor = ctk.CTkButton(self, image=self.imagem_professor, text="Adicionar Professor", compound="left", command=self.acao_professor)
        self.botaoProfessor.grid(row=1, column=2, padx=20, pady=10)

        self.imagem_disciplina = self.adicionar_disciplina()
        self.botaoDisciplina = ctk.CTkButton(self, image=self.imagem_disciplina, text="Adicionar Disciplina", compound="left", command=self.acao_disciplina)
        self.botaoDisciplina.grid(row=1, column=3, padx=20, pady=10)

        # Atualizar imagens ao mudar tema
        self.bind("<Configure>", self.atualizar_imagem)

    def adicionar_aluno(self):
        if ctk.get_appearance_mode() == 'Dark':
            return ctk.CTkImage(Image.open("add_user_light.png"), size=(50, 50))
        else:
            return ctk.CTkImage(Image.open("add_user_dark.png"), size=(50, 50))

    def adicionar_professor(self):
        if ctk.get_appearance_mode() == "Dark":
            return ctk.CTkImage(Image.open("add_user_light.png"), size=(50, 50))
        else:
            return ctk.CTkImage(Image.open("add_user_dark.png"), size=(50, 50))


    def adicionar_disciplina(self):
        if ctk.get_appearance_mode() == "Dark":
            return ctk.CTkImage(Image.open("icon_white-removebg-preview.png"), size=(50, 50))
        else:
            return ctk.CTkImage(Image.open("icon_black-removebg-preview.png"), size=(50, 50))

    def acao_aluno(self):
        print("Adicionar Aluno clicado!")

    def acao_professor(self):
        print("Adicionar Professor clicado!")

    def acao_disciplina(self):
        print("Adicionar Disciplina clicado!")

    def atualizar_imagem(self, event=None):
        self.imagem_disciplina = self.adicionar_disciplina()
        self.imagem_professor = self.adicionar_professor()
        self.imagem_aluno = self.adicionar_aluno()
        self.botao.configure(image=self.imagem_aluno)
        self.botaoProfessor.configure(image=self.imagem_professor)
        self.botaoDisciplina.configure(image=self.imagem_disciplina)