import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter as tk

def exportar_dados():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='17032005',
        database='pizzaria'
    )
    mc = mydb.cursor()
    ins = 'INSERT INTO produtos (nome, preço) VALUES (%s, %s)'
    val = f'{str(entry_1.get())}', f' {float(entry_2.get())}'
    mc.execute(ins, val)

    mydb.commit()

def excluir_dados():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='17032005',
        database='pizzaria'
    )
    mc = mydb.cursor()

    if entry_4.get() == '':
        mc.execute(f'DELETE FROM produtos WHERE id_produto = {int(entry_3.get())}')
        mydb.commit()
    elif entry_3.get() == '':
        mc.execute(f'DELETE FROM produtos WHERE nome = "{str(entry_4.get())}"')
        mydb.commit()

def janela2():
    janela2 = Tk()
    janela2.geometry('400x500')
    janela2.withdraw()
    mybd = mysql.connector.connect(
        host='localhost',
        user='root',
        password='17032005',
        database='pizzaria'
    )
    mc = mybd.cursor()
    mc.execute('SELECT * FROM admins')  #SELECIONA/MOSTRA OS DADOS DA TABELA ADMINS
    #A TABELA NO MYSQL CONSITE EM 3 COLUNAS; ID, LOGIN E SENHA RESPECTIVAMENTE
    #OS DADOS DA TABELA SÃO GUARDADOS EM UMA LISTA []

    mr = mc.fetchall()                  #GUARDA OS DADOS DA TABELA ADMINS
    for x in mr:                        #PARA CADA ELEMENTO...
        #SEPARA SOMENTE O ID DA TABELA MYSQL
        xa = str(x).split()             #XA<- DIVIDI OS ELEMETO DA TABELA E GUARDA EM UMA LISTA
        xb1 = xa[0]                     #XB1<- GUARDA O 1° ELEMENTO DE XA
        xc1 = [int(xb1[1])]             #XC1<- GUARDARÁ O ID
        #SEPARA SOMENTE O LOGIN DA TABELA MYSQL
        xb2 = xa[1]                     #XB2<- GUARDA O 2° ELEMENTO DE XA
        xc2 = str(xb2[1:-2])            #XC2<- GUARDARÁ O LOGIN
        #SEPARA SOMENTE A SENHA DA TABELA MYSQL
        xb3 = xa[2]                     #XB3<- GUARDA 0 3° ELEMENTO DE XA
        xc3 = int(xb3[:-1])             #XC3<- GUARDARÁ A SENHA

        if xc2 == str(entry_user.get()) and xc3 == int(entry_senha.get()):
            janela2.deiconify()
            janela2.title(string='Cadastrar produtos')
            janela.withdraw()
            janela.destroy()
            global entry_1
            global entry_2
            global entry_3
            global entry_4
            entry_1 = Entry(janela2)
            entry_1.place(x=20, y=40, width=150)
            entry_2 = Entry(janela2)
            entry_2.place(x=20, y=100, width=150)
            entry_3 = Entry(janela2)
            entry_3.place(x=225, y=40, width=150)
            entry_4 = Entry(janela2)
            entry_4.place(x=225, y=100, width=150)
            lbl1 = Label(janela2, text='Qual o nome do produto?')
            lbl1.place(x=20, y=10)
            lbl2 = Label(janela2, text='Qual é o preço do produto?')
            lbl2.place(x=20, y=70)
            lbl3 = Label(janela2, text='ID do produto')
            lbl3.place(x=225, y=10)
            lbl4 = Label(janela2, text='Nome do produto')
            lbl4.place(x=225, y=70)
            btn_cadastrar = Button(janela2, text='Cadastrar', command=exportar_dados)
            btn_cadastrar.place(x=20, y=130, width=70, height=30)
            btn_deletar = Button(janela2, text='Deletar', command=excluir_dados)
            btn_deletar.place(x=305, y=130, width=70, height=30)

janela = Tk()
janela.title(string='Inicio')
janela.geometry('400x500')
imagem = PhotoImage(file= 'C:/Users/hugot/OneDrive/Imagens/Saved Pictures/pizza.png')
lbl_imagem = Label(janela, image=imagem)
lbl_imagem.place(x=0, y=0)
lbl_user = Label(janela, text='Insira um user admin', background='#ffffff', font='arial 10')
lbl_user.place(x=123, y=70 )
lbl_senha = Label(janela, text='Insira sua senha', background='#ffffff', font='arial 10')
lbl_senha.place(x=123, y=120)


entry_user = Entry(janela)
entry_user.place(x=125, y=90, width=150)
entry_senha = Entry(janela)
entry_senha.place(x=125, y=140, width=150)

btn_entrar = Button(janela, background='#a72300', command=janela2)
btn_entrar.place(x=150, y=200, width=100)

janela.mainloop()