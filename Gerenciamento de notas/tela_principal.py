import tkinter
import customtkinter
from menu_professor import MenuProfessor
from menu_coordenador import MenuCoordenador
from anotacoes import Anotacoes

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Gerenciamento de Notas")
        self.geometry(f"{1100}x{580}")

        # Configurar o layout da grade (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Criar o painel lateral com widgets
        self.painel_lateral = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.painel_lateral.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.painel_lateral.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.painel_lateral, text="UNIFIMES", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Botão Voltar
        self.botao_voltar = customtkinter.CTkButton(self.painel_lateral, text="VOLTAR", command=self.voltar_inicial)
        self.botao_voltar.grid(row=1, column=0, padx=20, pady=10)
        self.botao_voltar.grid_forget()  # Inicialmente esconder

        # Botões do menu lateral
        self.botao_professor = customtkinter.CTkButton(self.painel_lateral, text="MENU PROFESSOR", command=self.menu_professor)
        self.botao_professor.grid(row=2, column=0, padx=20, pady=10)
        self.botao_coordenador = customtkinter.CTkButton(self.painel_lateral, text="MENU COORDENADOR", command=self.menu_coordenador)
        self.botao_coordenador.grid(row=3, column=0, padx=20, pady=10)
        self.botao_desativado = customtkinter.CTkButton(self.painel_lateral, text="ANOTAÇÕES")
        self.botao_desativado.grid(row=4, column=0, padx=20, pady=10)

        # Configurações de tema e zoom
        self.rotulo_tema = customtkinter.CTkLabel(self.painel_lateral, text="Esquema de Cores:", anchor="w")
        self.rotulo_tema.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.menu_opcoes_tema = customtkinter.CTkOptionMenu(self.painel_lateral, values=["Light", "Dark", "System"], command=self.alterar_tema_evento)
        self.menu_opcoes_tema.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.rotulo_zoom = customtkinter.CTkLabel(self.painel_lateral, text="Zoom da Janela:", anchor="w")
        self.rotulo_zoom.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.menu_opcoes_zoom = customtkinter.CTkOptionMenu(self.painel_lateral, values=["80%", "90%", "100%", "110%", "120%"], command=self.alterar_zoom_evento)
        self.menu_opcoes_zoom.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Criar o espaço principal onde as telas serão trocadas
        self.tela_principal = customtkinter.CTkFrame(self)
        self.tela_principal.grid(row=0, column=1, columnspan=3, sticky="nsew")

        # Definir valores padrão
        self.menu_opcoes_tema.set("Dark")
        self.menu_opcoes_zoom.set("100%")

    def alterar_tema_evento(self, novo_tema: str):
        customtkinter.set_appearance_mode(novo_tema)

    def alterar_zoom_evento(self, novo_zoom: str):
        novo_zoom_float = int(novo_zoom.replace("%", "")) / 100
        customtkinter.set_widget_scaling(novo_zoom_float)
        
    def menu_professor(self):
        self.rotulo_tema.grid_forget()
        self.menu_opcoes_tema.grid_forget()
        # Limpar o conteúdo da tela principal antes de exibir o novo conteúdo
        self.limpar_tela_principal()

        # Exibir o botão "Voltar"
        self.botao_voltar.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Exibir o menu do professor
        menu_professor = MenuProfessor(self.tela_principal)
        menu_professor.pack(fill="both", expand=True)

    def menu_coordenador(self):
        self.rotulo_tema.grid_forget()
        self.menu_opcoes_tema.grid_forget()
        # Limpar o conteúdo da tela principal antes de exibir o novo conteúdo
        self.limpar_tela_principal()
        
        self.botao_voltar.grid(row=0, column=0, padx=20, pady=(20,10))

        # Exibir o menu coordenador
        texto = customtkinter.CTkLabel(self.tela_principal, text="Menu Coordenador", font=customtkinter.CTkFont(size=24))
        texto.pack(pady=20)
        
        menu_coordenador = MenuCoordenador(self.tela_principal)
        menu_coordenador.pack(fill="both", expand=True)

    def anotacoes(self):
        self.limpar_tela_principal()
        
        self.botao_voltar.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        anotacoes = Anotacoes(self.tela_principal)
        anotacoes.pack(fill="both", expand=True)

    def voltar_inicial(self):
        # Limpar o conteúdo da tela principal antes de voltar à tela inicial
        self.limpar_tela_principal()

        # Esconder o botão "Voltar"
        self.botao_voltar.grid_forget()
        self.rotulo_tema.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.menu_opcoes_tema.grid(row=6, column=0, padx=20, pady=(10, 10))

        # Exibir o conteúdo inicial (sem menus)
        texto_inicial = customtkinter.CTkLabel(self.tela_principal, text="Tela Inicial", font=customtkinter.CTkFont(size=24))
        texto_inicial.pack(pady=20)

    def limpar_tela_principal(self):
        # Remove todos os widgets da tela principal
        for widget in self.tela_principal.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
