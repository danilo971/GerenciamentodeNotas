import customtkinter as ctk
from tela_login import Telalogin

class Application:
    def __init__(self):
        self.janela = ctk.CTk(fg_color="white")
        self.tema()
        self.tela()
        self.tela_login = Telalogin(self.janela)  # Instancia a tela de login
        self.janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.geometry("700x400")
        self.janela.title("Gerenciamento de notas")
        self.janela.resizable(False, False)

if __name__ == "__main__":
    Application()
