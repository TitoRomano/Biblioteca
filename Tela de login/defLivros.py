
emprestimos = []

def cadastrar_emprestimo(usuario, livro):
    livro = nomeLivro.get()
    usuario = nomeUsuario.get()
    if livro and usuario:
        emprestimos.append({"livro": livro, "usuario": usuario})
        messagebox.showinfo("Sucesso", f"Empréstimo registrado: {livro} para {usuario}")
        nomeLivro.delete(0, tk.END)
        nomeUsuario.delete(0, tk.END) 
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")




def atualizar_emprestimos():
    texto = "\n".join([f"{e['livro']} - {e['usuario']}" for e in emprestimos])
    emprestimosLabel.config(text=texto)