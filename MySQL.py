import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter as tk

def janela2():
    janela2 = Tk()


    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        password='17032005',
        database='pizzaria'
    )
    mc = mybd.cursor()
    mc.execute('SELECT * FROM admins')

    mr = mc.fetchall()
    for x in mr:
        print(x)
    tree = ttk.Treeview(janela2, columns=('id', 'login', 'senha'), show='headings')
    tree.column('id', width=30, minwidth=0)
    tree.column('login', width=80, minwidth=0)
    tree.column('senha', width=50, minwidth=0)
    tree.heading('id', text='ID')
    tree.heading('login', text='LOGIN')
    tree.heading('senha', text='SENHA')
    tree.insert('', END, values='oi')
    janela2.mainloop()


janela = Tk()
janela.geometry('400x500')
imagem = PhotoImage(file= 'C:/Users/hugot/OneDrive/Imagens/Saved Pictures/pizza.png')
lbl_imagem = Label(janela, image=imagem)
lbl_imagem.place(x=0, y=0)
lbl_user = Label(janela, text='Insira um user admin', background='#ffffff', font='arial 10')
lbl_user.place(x=123, y=70 )
lbl_senha = Label(janela, text='Inseira sua senha', background='#ffffff', font='arial 10')
lbl_senha.place(x=123, y=120)


entry_user = Entry(janela)
entry_user.place(x=125, y=90, width=150)
entry_senha = Entry(janela)
entry_senha.place(x=125, y=140, width=150)

btn_entrar = Button(janela, background='#a72300', command=janela2)
btn_entrar.place(x=150, y=200, width=100)

janela.mainloop()