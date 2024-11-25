import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk
from tela_login import Telalogin

class TestTelaLogin(unittest.TestCase):
    def setUp(self):
        # Criar uma janela Tk simples para o teste
        self.root = Tk()
        self.tela_login = Telalogin(self.root)

    def tearDown(self):
        # Garantir que a janela seja destruída corretamente
        self.root.quit()  # Encerra o loop principal do Tkinter
        self.root.destroy()  # Destrói a janela

    @patch('tela_login.sqlite3.connect')  # Mock do banco de dados
    @patch('tela_login.messagebox')  # Mock do messagebox
    @patch('tela_login.App')  # Mock da tela principal
    def test_login_sucesso(self, mock_app, mock_messagebox, mock_conexao):
        # Simular retorno do banco de dados (login válido)
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (1, 'Coordenador')  # Retorno válido
        mock_conexao.return_value.cursor.return_value = mock_cursor

        # Simular entrada do usuário
        self.tela_login.username.get = MagicMock(return_value="coordenador@teste.com")
        self.tela_login.senha.get = MagicMock(return_value="1234")

        # Executar o método de login
        self.tela_login.login()

        # Verificar se a consulta ao banco foi feita corretamente
        mock_cursor.execute.assert_called_with(
            "SELECT * FROM Usuario WHERE Email = ? AND Senha = ?",
            ("coordenador@teste.com", "1234")
        )

        # Verificar se a mensagem de sucesso foi exibida
        mock_messagebox.showinfo.assert_called_with("Sistema de Login", "Login feito com sucesso!")

        # Verificar se a tela principal foi chamada
        mock_app.assert_called_once()

    @patch('tela_login.sqlite3.connect')  # Mock do banco de dados
    @patch('tela_login.messagebox')  # Mock do messagebox
    @patch('tela_login.App')  # Mock da tela principal
    def test_login_falha(self, mock_app, mock_messagebox, mock_conexao):
        # Simular retorno vazio do banco de dados (login inválido)
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None  # Login inválido
        mock_conexao.return_value.cursor.return_value = mock_cursor

        # Simular entrada do usuário
        self.tela_login.username.get = MagicMock(return_value="invalido@teste.com")
        self.tela_login.senha.get = MagicMock(return_value="senha_errada")

        # Executar o método de login
        self.tela_login.login()

        # Verificar se a mensagem de erro foi exibida
        mock_messagebox.showerror.assert_called_with("Sistema de Login", "Usuário e/ou senha incorretos!")

        # Garantir que a tela principal NÃO foi chamada
        mock_app.assert_not_called()

    @patch('tela_login.messagebox')  # Mock do messagebox
    def test_campos_vazios(self, mock_messagebox):
        # Simular campos vazios
        self.tela_login.username.get = MagicMock(return_value="")
        self.tela_login.senha.get = MagicMock(return_value="")

        # Executar o método de login
        self.tela_login.login()

        # Verificar se a mensagem de aviso foi exibida
        mock_messagebox.showwarning.assert_called_with("Sistema de Login", "Por favor, preencha todos os campos.")

if __name__ == '__main__':
    unittest.main()
