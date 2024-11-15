import customtkinter as ctk

class TelaPrincipal:
    def __init__(self):
        self.janela_principal = None

    def criar_nova_janela(self):
        self.janela_principal = ctk.CTk()
        largura_janela = self.janela_principal.winfo_screenwidth()
        altura_janela = self.janela_principal.winfo_screenheight()
        self.janela_principal.geometry(f'{largura_janela}x{altura_janela}')
        self.janela_principal.resizable(False, False)
        self.janela_principal.mainloop()
