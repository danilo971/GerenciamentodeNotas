import customtkinter as ctk

class AdicionarNotas(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(pady=20, padx=20, fill="both", expand=True)


        # Campo de entrada para ID do aluno
        rotulo_aluno = ctk.CTkLabel(self, text="ID do Aluno:", anchor="w", font=ctk.CTkFont(size=14))
        rotulo_aluno.pack(fill="x", padx=20, expand=True)
        entrada_aluno = ctk.CTkEntry(self, placeholder_text="Digite o ID do aluno")
        entrada_aluno.pack(fill="x", padx=20, pady=(5, 15), expand=True)

        # Campo de entrada para a nota
        rotulo_nota = ctk.CTkLabel(self, text="Nota:", anchor="w", font=ctk.CTkFont(size=14))
        rotulo_nota.pack(fill="x", padx=20, expand=True)
        entrada_nota = ctk.CTkEntry(self, placeholder_text="Digite a nota do aluno")
        entrada_nota.pack(fill="x", padx=20, pady=(5, 15), expand=True)

        # Campo de entrada para descrição
        rotulo_descricao = ctk.CTkLabel(self, text="Descrição:", anchor="w", font=ctk.CTkFont(size=14))
        rotulo_descricao.pack(fill="x", padx=20, expand=True)
        entrada_descricao = ctk.CTkEntry(self, placeholder_text="Digite uma breve descrição")
        entrada_descricao.pack(fill="x", padx=20, pady=(5, 15), expand=True)

        # Botão para salvar
        botao_salvar = ctk.CTkButton(self, text="Salvar Nota", command=self.salvar_nota)
        botao_salvar.pack(pady=(20, 10), expand=True)

    def salvar_nota(self):
        print("Nota salva com sucesso!")
