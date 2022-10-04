import mysql.connector                  #IMPORTA BIBLIOTECA PARA CONECTAR AO MYSQL
from tkinter import *                   #IMPORTA TKINTER
from tkinter import ttk
import tkinter as tk

def janela2():                          #FUNÇÃO PARA SE CONECTAR AO MYSQL E ABRIR A JANELA2
    janela2 = Toplevel()                #CRIA A JANELA2
    janela2.geometry('400x500')
    janela2.withdraw()                  #OCULTA A JANELA2
    mybd = mysql.connector.connect(     #COMANDO PARA SE CONECTAR AO BANCO MYSQL
        host='localhost',
        user='root',
        password='17032005',
        database='pizzaria'
    )
    mc = mybd.cursor()
    mc.execute('SELECT * FROM admins')  #SELECIONA/MOSTRA OS DADOS DA TABELA ADMINS
    #A TABELA NO MYSQL CONSITE EM 3 COLUNAS; ID, LOGIN E SENHA RESPECTIVAMENTE
    #OS DADOS DA TABELA SÃO GUARDADOS EM UMA LISTA []

    lista1 = Listbox(janela2)           #VARIÁVEIS DE LISTBOX
    lista2 = Listbox(janela2)
    lista3 = Listbox(janela2)

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

        lista1.insert(END, xc1)         #INSERI OS VALORES NAS LISTBOX
        lista2.insert(END, xc2)
        lista3.insert(END, xc3)
        #SE XC2 FOR = AO QUE ESTIVER ESCRITO NO ENTRY_USER E O XC3 NO ENTRY_SENHA, A JANELA2 É MOSTRADA
        if xc2 == str(entry_user.get()) and xc3 == int(entry_senha.get()):
            janela2.deiconify()         #MOSTRA A JANELA2 QUE ESTAVA OCULTADA
            janela.withdraw()
            lista1.place(x=20, y=40, width=20, height=50)# POSIÇÃO DOS LISTBOX
            lista2.place(x=45, y=40, width=100, height=50)
            lista3.place(x=150, y=40, width=50, height=50)
            lbl_id = Label(janela2, text='ID')
            lbl_id.place(x=20, y=20)

janela = Tk()
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