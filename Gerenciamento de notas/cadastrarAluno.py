import customtkinter as ctk


class AplicativoRegistro:
    def __init__(self):
        # Configuração principal
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        # Inicializa a janela principal
        self.janela = ctk.CTk()
        self.janela.title("Aplicativo de Registro")
        self.janela.geometry("600x500")

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
        """Cria o frame para informações do usuário."""
        frame_usuario = ctk.CTkFrame(parent)
        frame_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        titulo_usuario = ctk.CTkLabel(frame_usuario, text="Informações do Usuário",
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
        self.combobox_cpf = ctk.CTkEntry(frame_usuario)
        self.combobox_cpf.grid(row=2, column=2, padx=5, pady=5)

        ctk.CTkLabel(frame_usuario, text="Idade").grid(row=3, column=0, padx=5, pady=5)
        self.spinbox_idade = ctk.CTkEntry(frame_usuario, placeholder_text="17 - 110")
        self.spinbox_idade.grid(row=4, column=0, padx=5, pady=5)

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
        ctk.CTkLabel(frame_cursos, text="Nome do Curso").grid(row=1, column=0, padx=5, pady=5)
        self.spinbox_cursos = ctk.CTkEntry(frame_cursos)
        self.spinbox_cursos.grid(row=2, column=0, padx=5, pady=5)

        ctk.CTkLabel(frame_cursos, text="Semestres").grid(row=1, column=1, padx=5, pady=5)
        self.spinbox_semestres = ctk.CTkEntry(frame_cursos, placeholder_text="0+")
        self.spinbox_semestres.grid(row=2, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_cursos, text="Status da Matrícula").grid(row=1, column=2, padx=5, pady=5)
        check_matricula = ctk.CTkCheckBox(frame_cursos, text="Matriculado", variable=self.status_var,
                                          onvalue="Matriculado", offvalue="Não Matriculado")
        check_matricula.grid(row=2, column=2, padx=5, pady=5)

    def criar_frame_termos(self, parent):
        """Cria o frame para os termos e condições."""
        frame_termos = ctk.CTkFrame(parent)
        frame_termos.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        titulo_termos = ctk.CTkLabel(frame_termos, text="Termos e Condições",
                                     font=ctk.CTkFont(size=16, weight="bold"))
        titulo_termos.grid(row=0, column=0, pady=(0, 10))

        check_termos = ctk.CTkCheckBox(frame_termos, text="Aceito os Termos e Condições.",
                                       variable=self.aceitar_var, onvalue="Aceito", offvalue="Não Aceito")
        check_termos.grid(row=1, column=0, padx=5, pady=5)

    def salvar_dados(self):
        """Lógica para salvar os dados inseridos pelo usuário."""
        aceito = self.aceitar_var.get()
        if aceito == "Aceito":
            primeiro_nome = self.entrada_primeiro_nome.get()
            ultimo_nome = self.entrada_ultimo_nome.get()
            if primeiro_nome and ultimo_nome:
                cpf = self.combobox_cpf.get()
                idade = self.spinbox_idade.get()
                nacionalidade = self.combobox_nacionalidade.get()
                nome_curso = self.spinbox_cursos.get()
                semestres = self.spinbox_semestres.get()
                status_matricula = self.status_var.get()

                dados = (f"Primeiro Nome: {primeiro_nome}\nÚltimo Nome: {ultimo_nome}\n"
                         f"CPF: {cpf}\nIdade: {idade}\nNacionalidade: {nacionalidade}\n"
                         f"Nome do Curso: {nome_curso}\nSemestres: {semestres}\n"
                         f"Status da Matrícula: {status_matricula}\n{'-' * 40}\n")

                print(dados)
                with open("dados_matricula.txt", "a+") as f:
                    f.write(dados)
            else:
                ctk.CTkMessageBox(title="Erro no Nome", message="Nome e sobrenome são obrigatórios.")
        else:
            ctk.CTkMessageBox(title="Erro nos Termos", message="Por favor, aceite os Termos e Condições.")


if __name__ == "__main__":
    app = AplicativoRegistro()
