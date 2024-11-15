import tkinter as tk

# Cria a janela principal
root = tk.Tk()

# Obtém a largura e altura da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Define o tamanho da janela para ocupar toda a tela
root.geometry(f"{largura_tela}x{altura_tela}")

# Define a janela como não redimensionável
root.resizable(False, False)

# Executa o loop principal da aplicação
root.mainloop()
