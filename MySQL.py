import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter as tk

def janela2():
    
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
        xa = str(x).split()
        xb1 = xa[0]
        xc1 = [int(xb1[1])]
        xb2 = xa[1]
        xc2 = str(xb2[1:-2])
        xb3 = xa[2]
        xc3 = int(xb3[:-1])
        if xc2 == str(entry_user.get()) and xc3 == int(entry_senha.get()):

            print('1')
            janela2 = Tk()
            janela2.geometry('300x200')
            lista1 = Listbox(janela2)
            lista2 = Listbox(janela2)
            lista3 = Listbox(janela2)

            lista1.insert(END, xc1)
            lista2.insert(END, xc2)
            lista3.insert(END, xc3)

            lista1.place(x=20, y=20, width=30)
            lista2.place(x=70, y=20, width=100)
            lista3.place(x=190, y=20, width=50)


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