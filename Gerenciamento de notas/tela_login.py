from tkinter import PhotoImage
from tkinter import messagebox
import customtkinter as ctk
import sqlite3
from tela_principal import App  # Certifique-se de que tela_principal.py existe e é funcional.

class backEnd:
    def conecta_db(self):
        self.conn = sqlite3.connect("bd.db")
        self.cursor = self.conn.cursor()

    def desconecta_db(self):
        self.conn.close()

class Telalogin(backEnd):
    def __init__(self, janela):
        self.janela = janela
        self.criar_tela_login()

    def criar_tela_login(self):
        self.image = PhotoImage(file="unifimes.png")
        self.label_image = ctk.CTkLabel(master=self.janela, image=self.image, text="")
        self.label_image.place(x=-50, y=-65)

        self.login_frame = ctk.CTkFrame(self.janela, width=350, height=396)
        self.login_frame.pack(side="right")

        texto = ctk.CTkLabel(self.login_frame, text="Sistema de Login", font=("Roboto", 20))
        texto.place(x=25, y=5)

        self.username = ctk.CTkEntry(self.login_frame, placeholder_text="Username", width=300, font=("Roboto", 14))
        self.username.place(x=25, y=105)

        self.senha = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=300, font=("Roboto", 14))
        self.senha.place(x=25, y=175)

        checkbox = ctk.CTkCheckBox(self.login_frame, text="Lembrar login")
        checkbox.place(x=25, y=235)

        login_botao = ctk.CTkButton(self.login_frame, text="Login", width=300, command=self.login)
        login_botao.place(x=25, y=285)

    def login(self):
        self.Email = self.username.get()
        self.Senha = self.senha.get()

        self.conecta_db()

        self.cursor.execute("SELECT * FROM Usuario WHERE Email = ? AND Senha = ?", (self.Email, self.Senha))
        self.verifica_dados = self.cursor.fetchone()

        if not self.Email or not self.Senha:
            messagebox.showwarning("Sistema de Login", "Por favor, preencha todos os campos.")
        elif self.verifica_dados:
            #messagebox.showinfo("Sistema de Login", "Login feito com sucesso!")
            self.desconecta_db()
            self.janela.destroy()

            app = App()
            app.mainloop()
        else:
            messagebox.showerror("Sistema de Login", "Usuário e/ou senha incorretos!")
            self.desconecta_db()
