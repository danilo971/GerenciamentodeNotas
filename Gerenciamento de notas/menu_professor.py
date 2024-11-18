import customtkinter as ctk
from PIL import Image

class MenuProfessor(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(pady=20, padx=20, fill="both", expand=True)

        # Configuração do grid
        self.grid_columnconfigure((0, 4), weight=1)  # Colunas externas
        self.grid_columnconfigure((1, 2, 3), weight=0)  # Colunas dos botões
        self.grid_rowconfigure(1, weight=1)  # Linha 1 se expande

        #self.grid_columnconfigure(1, weight=1)
        #self.grid_columnconfigure((2, 3), weight=0)
        #self.grid_rowconfigure((0, 1, 2), weight=1)

        # Adicione mais widgets para o menu do professor aqui
        self.imagem_nota = self.adicionar_notas()
        self.botaoNota = ctk.CTkButton(self, image=self.imagem_nota, text="Adicionar Notas", compound="left", command=self.acao_nota)
        self.botaoNota.grid(row=1, column=1, padx=20, pady=10)

        #self.botao_voltar = customtkinter.CTkButton(self.painel_lateral, text="VOLTAR")
        #self.botao_voltar.grid(row=1, column=0, padx=20, pady=10)
        #self.botao_coordenador = customtkinter.CTkButton(self.painel_lateral, text="MENU COORDENADOR", command=self.menu_coordenador)
        #self.botao_coordenador.grid(row=3, column=0, padx=20, pady=10)
        #self.botao_desativado = customtkinter.CTkButton(self.painel_lateral, text="ANOTAÇÕES")
        #self.botao_desativado.grid(row=4, column=0, padx=20, pady=10)
        #self.botao_professor = customtkinter.CTkButton(self.painel_lateral, text="MENU PROFESSOR", command=self.menu_professor)
        #self.botao_professor.grid(row=2, column=0, padx=20, pady=10)

        # Atualizar imagens ao mudar tema
        self.bind("<Configure>", self.atualizar_imagem)

    def adicionar_notas(self):
        if ctk.get_appearance_mode() == "Dark":
            return ctk.CTkImage(Image.open("icon_white-removebg-preview.png"), size=(50, 50))
        else:
            return ctk.CTkImage(Image.open("icon_black-removebg-preview.png"), size=(50, 50))

    def acao_nota(self):
        print("Clicado no botão de notas")

    def atualizar_imagem(self, evento=None):
        self.imagem_nota = self.adicionar_notas()
        self.botaoNota.configure(image=self.imagem_nota)
    