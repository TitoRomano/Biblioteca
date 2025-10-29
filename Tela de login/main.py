import tkinter as tk
from tkinter import messagebox
import defLogin
import csv

main = tk.Tk()
main.title('Login')
main.geometry('250x150')

tk.Label(main, text='E-mail:').place(x=0, y=0, height=20)
email = tk.Entry(main)
email.place(x=50, y=0, width=180)


tk.Label(main, text='Senha:').place(x=0, y=30)
senha = tk.Entry(main)
senha.place(x=50, y=30, width=180)


tk.Button(main, text="Entrar", bg='#59b390', fg='white', command=defLogin.fazerLogin).place(x=100, y=60, width=50, height=30) #Botão de login


tk.Button(main, text='Criar nova conta', bg='#e32d40', fg='white').place(x=75, y=100, width=100, height=30) #Botão de criar conta







main.mainloop()