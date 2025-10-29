import csv




def fazerLogin():
    #Verifica as credenciais e faz login
    email_val = email.get().strip()
    senha_val = senha.get()
    
    if not email_val or not senha_val:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return
    
    sucesso, mensagem = defLogin.verificar_login(email_val, senha_val)
    
    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        livrosEmprestados(email_val)
    else:
        messagebox.showerror("Erro", mensagem)






def criar_conta():
    #Abre janela para criar nova conta
    def cadastrar():
        email_val = email_cadastro.get().strip()
        senha_val = senha_cadastro.get()
        confirmar_val = confirmar_senha.get()
        
        if not email_val or not senha_val or not confirmar_val:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if senha_val != confirmar_val:
            messagebox.showerror("Erro", "Senhas não coincidem!")
            return
        
        sucesso, mensagem = defLogin.cadastrar_usuario(email_val, senha_val)
        
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            janela_cadastro.destroy()
        else:
            messagebox.showerror("Erro", mensagem)
    
    # Janela de cadastro
    janela_cadastro = tk.Toplevel(main)
    janela_cadastro.title('Criar Conta')
    janela_cadastro.geometry('250x200')
    
    tk.Label(janela_cadastro, text='E-mail:').place(x=10, y=20)
    email_cadastro = tk.Entry(janela_cadastro)
    email_cadastro.place(x=80, y=20, width=160)
    
    tk.Label(janela_cadastro, text='Senha:').place(x=10, y=60)
    senha_cadastro = tk.Entry(janela_cadastro, show='*')
    senha_cadastro.place(x=80, y=60, width=160)
    
    tk.Label(janela_cadastro, text='Confirmar:').place(x=10, y=100)
    confirmar_senha = tk.Entry(janela_cadastro, show='*')
    confirmar_senha.place(x=80, y=100, width=160)
    
    tk.Button(janela_cadastro, text='Cadastrar', command=cadastrar,
              bg='#59b390', fg='white').place(x=90, y=140, width=70)