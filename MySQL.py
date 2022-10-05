#--------------------IMPORTAÇÃO DE BIBLOTECAS-------------------#
import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter as tk
#--------------------FUNÇÕES-------------------#

#---FUNÇÃO PARA INSERIR OS DADOS DAS ENTRADAS NO BANCO---#
def inserir_dados():
    mydb = mysql.connector.connect(     #CONECTA O PYTHON AO MYSQL
        host='localhost',
        user='root',
        password='17032005',
        database='pizzaria'
    )
    mc = mydb.cursor()
    ins = 'INSERT INTO produtos (nome, preço) VALUES (%s, %s)'  #COMANDO SQL PARA INSERIR DADOS NA TABELA DO BANDO
    val = f'{str(entry_in_nome.get())}', f' {float(entry_in_preco.get())}'   #VALORES A SEREM INSERIDOS
    mc.execute(ins, val)    #EXECUTA O COMANDO JUNTO AOS VALORES
    mydb.commit()   #NECESSARIO PARA FAZER AS ALTERAÇÕES

#---FUNÇÃO PARA DELETAR LINHAS DA TABELA DO BANCO---#
def excluir_dados():
    mydb = mysql.connector.connect(     #CONECTA O PYTHON AO MYSQL
        host='localhost',
        user='root',
        password='17032005',
        database='pizzaria'
    )
    mc = mydb.cursor()
    #---IF PARA SABER QUAL COMANDO EXECUTAR---#
    if entry_ex_nome.get() == '':
        mc.execute(f'DELETE FROM produtos WHERE id_produto = {int(entry_ex_id.get())}')
        mydb.commit()
    elif entry_ex_id.get() == '':
        mc.execute(f'DELETE FROM produtos WHERE nome = "{str(entry_ex_nome.get())}"')
        mydb.commit()
    elif entry_ex_id.get() and entry_ex_nome.get() != '':
        mc.execute(f'DELETE FROM produtos WHERE id_produto = {int(entry_ex_id.get())}')
        mydb.commit()

#---FUNÇÃO PARA ABRIR A JANELA DE CADASTRO---#
def janela_cadasto_abrir():
    mybd = mysql.connector.connect(     #CONECTA O PYTHON AO MYSQL
        host='localhost',
        user='root',
        password='17032005',
        database='pizzaria'
    )
    mc = mybd.cursor()
    mc.execute('SELECT * FROM admins')  #COMANDO SQL PARA SELECIONAR A TABELA DO BANCO

    mr = mc.fetchall()
    for x in mr:
        #---SEPARA SOMENTE OS VALORES DO ID DO BANCO---#
        xa = str(x).split()
        xb1 = xa[0]
        xc1 = [int(xb1[1])]
        #---SEPARA SOMENTE OS VALORES DO NOME DO BANCO---#
        xb2 = xa[1]
        xc2 = str(xb2[1:-2])
        #---SEPARA SOMENTE OS VALORES DA SENHA DO BANCO---#
        xb3 = xa[2]
        xc3 = int(xb3[:-1])
        #---SE OS VALORES DOS ENTRYS DA JANELA INICIAL ESTIVEREM NO BANCO, CRIARÁ A JANELA DE CADASTRO---#
        if xc2 == str(entry_user.get()) and xc3 == int(entry_senha.get()):
            #---VARIÁVEIS GLOBAIS---#
            global entry_in_nome
            global entry_in_preco
            global entry_ex_id
            global entry_ex_nome
            #---CRIAÇÃO EM SI DA JANELA DE CADASTROS---#
            janelaCadatro = Tk()
            janelaCadatro.geometry('400x500')
            janelaCadatro.title(string='Cadastrar produtos')
            janelaInicial.withdraw()
            janelaInicial.destroy()
            #---ENTRADAS JANELA CADASTRO---#
            entry_in_nome = Entry(janelaCadatro)
            entry_in_nome.place(x=20, y=40, width=150)
            entry_in_preco = Entry(janelaCadatro)
            entry_in_preco.place(x=20, y=100, width=150)
            entry_ex_id = Entry(janelaCadatro)
            entry_ex_id.place(x=225, y=40, width=150)
            entry_ex_nome = Entry(janelaCadatro)
            entry_ex_nome.place(x=225, y=100, width=150)
            #---LABELS JANELA CADASTRO---#
            lbl_in_nome = Label(janelaCadatro, text='Qual o nome do produto?')
            lbl_in_nome.place(x=20, y=10)
            lbl_in_preco = Label(janelaCadatro, text='Qual é o preço do produto?')
            lbl_in_preco.place(x=20, y=70)
            lbl_ex_id = Label(janelaCadatro, text='ID do produto')
            lbl_ex_id.place(x=225, y=10)
            lbl_ex_nome = Label(janelaCadatro, text='Nome do produto')
            lbl_ex_nome.place(x=225, y=70)
            #---BOTÕES JANELA CADASTRO---#
            btn_cadastrar = Button(janelaCadatro, text='Cadastrar', command=inserir_dados)
            btn_cadastrar.place(x=20, y=130, width=70, height=30)
            btn_deletar = Button(janelaCadatro, text='Deletar', command=excluir_dados)
            btn_deletar.place(x=305, y=130, width=70, height=30)

#--------------------JANELA INICIAL--------------------#
janelaInicial = Tk()
janelaInicial.title(string='Inicio')
janelaInicial.geometry('400x500')
imagem = PhotoImage(file= 'C:/Users/hugot/OneDrive/Imagens/Saved Pictures/pizza.png')
#---LABELS JANELA INICIAL---#
lbl_imagem = Label(janelaInicial, image=imagem)
lbl_imagem.place(x=0, y=0)
lbl_user = Label(janelaInicial, text='Insira um user admin', background='#ffffff', font='arial 10')
lbl_user.place(x=123, y=70 )
lbl_senha = Label(janelaInicial, text='Insira sua senha', background='#ffffff', font='arial 10')
lbl_senha.place(x=123, y=120)
#---ENTRADAS JANELA INICIAL---#
entry_user = Entry(janelaInicial)
entry_user.place(x=125, y=90, width=150)
entry_senha = Entry(janelaInicial)
entry_senha.place(x=125, y=140, width=150)
#BOTÕES JANELA INICIAL---#
btn_entrar = Button(janelaInicial, background='#a72300', command=janela_cadasto_abrir)
btn_entrar.place(x=150, y=200, width=100)
janelaInicial.mainloop()