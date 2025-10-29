import tkinter as tk
from tkinter import messagebox
import defLivros
import defLogin
import csv


janela = tk.Tk()
janela.title('Biblioteca - Cadastro de livros')
janela.geometry('500x400')

tk.Label(janela, text='Nome do Usuário:').pack(pady=5)
nomeUsuario = tk.Entry(janela)
nomeUsuario.pack(pady=5)

tk.Label(janela, text='Nome do Livro:').pack(pady=5)
nomeLivro = tk.Entry(janela)
nomeLivro.pack(pady=5)


tk.Button(janela, text="Cadastrar Empréstimo", command=defLivros.cadastrar_emprestimo).pack(pady=10)

emprestimosLabel = tk.Label(janela, text='')
emprestimosLabel.pack(pady=10)



janela.mainloop()
