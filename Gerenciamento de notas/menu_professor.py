import customtkinter as ctk
from adicionar_notas import AdicionarNotas
from PIL import Image

class MenuProfessor(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(pady=20, padx=20, fill="both", expand=True)

        # Configuração do grid
        self.grid_columnconfigure((0, 4), weight=1)  # Colunas externas
        self.grid_columnconfigure((1, 2, 3), weight=0)  # Colunas dos botões
        self.grid_rowconfigure(1, weight=1)  # Linha 1 se expande

        # Inicializar imagem do botão
        self.imagem_nota = self.obter_imagem_nota()
        self.botaoNota = ctk.CTkButton(self, image=self.imagem_nota, text="Adicionar Notas", compound="left", command=self.exibir_tela_adicionar_notas)
        self.botaoNota.grid(row=1, column=1, padx=20, pady=10)

    def obter_imagem_nota(self):
        """Retorna a imagem correta com base no tema."""
        if ctk.get_appearance_mode() == "Dark":
            return ctk.CTkImage(Image.open("icon_white-removebg-preview.png"), size=(50, 50))
        else:
            return ctk.CTkImage(Image.open("icon_black-removebg-preview.png"), size=(50, 50))

    def exibir_tela_adicionar_notas(self):
        """Exibe a interface para adicionar notas."""
        self.limparMenuProfessor()

        # Adiciona o título "Adicionar Notas"
        texto = ctk.CTkLabel(self, text="Adicionar Notas", font=ctk.CTkFont(size=24))
        texto.pack(pady=20)

        # Cria o widget para adicionar notas
        adicionar_notas = AdicionarNotas(self)
        adicionar_notas.pack(fill="both", expand=True)

    def limparMenuProfessor(self):
        """Remove todos os widgets da interface principal."""
        for widget in self.winfo_children():
            widget.destroy()
