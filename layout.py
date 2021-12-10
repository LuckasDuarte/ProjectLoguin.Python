#importar as bibliotecas
from os import name
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
import DataBase

#criar a janela
jan = Tk()

#titulo
jan.title('Loguin')
#tamanho
jan.geometry('600x300')
#cor da janela
jan.configure(background='white')
#tamanho fixo
jan.resizable(width=False, height=False)
#transparência a janela
jan.attributes('-alpha', 0.9)
#adicionando icone
jan.iconbitmap(default='icons/LogoIcon.ico')

#======== Carregando Imagens ==========

logo = PhotoImage(file='icons/logo.png')


#separar a janela em dois
LeftFrame = Frame(jan, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)

#======== Adicionando Imagens ===========#

LogoLabel = Label(LeftFrame, image= logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50, y=100)

#texto usuário
UserLabel = Label(RightFrame, text='Usuário:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
UserLabel.place(x=5, y=100)

#caixa de texto
UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=120, y=110)

#texto Senha
PasswordLabel = Label(RightFrame, text='Senha: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
PasswordLabel.place(x=5,y=150)

#caixa texto senha
PasswordEntry = ttk.Entry(RightFrame, width=30, show='•')
PasswordEntry.place(x=120, y=160)

def Loguin():
    User = UserEntry.get()
    Senha = PasswordEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (Usuário = ? AND Senha = ?)
    """, (User, Senha))
    print('Selecionou')
    VerificarLoguin = DataBase.cursor.fetchone()
    try:
        if (User in VerificarLoguin and Senha in VerificarLoguin):
            messagebox.showinfo(title='Loguin', message='Acesso Confirmado. Bem Vindo')
    except:
        messagebox.showinfo(title='Loguin', message='Acesso Negado. Verifique os Dados')


#Criando os Botões LOGUIN
LoguiButton = ttk.Button(RightFrame, text='Login', width=30, command= Loguin)
LoguiButton.place(x=72, y=210)

#definindo uma função

def Register():
    #removendo os botões
    LoguiButton.place(x=5000)
    RegistrarButton.place(x=5000)
    #Nome letra
    NomeLabel = Label(RightFrame, text='Nome:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
    NomeLabel.place(x=5, y=5)
    #nome Entrada
    NomeEntry = ttk.Entry(RightFrame, width=33)
    NomeEntry.place(x=100, y=20)
    #emai lLetra
    EmailLabel = Label(RightFrame,text='Email:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
    EmailLabel.place(x=5, y=50)
    #email entrada
    EmailEntry = ttk.Entry(RightFrame, width=33)
    EmailEntry.place(x=100, y=60)

    #registrando no banco de dados
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        Usuário = UserEntry.get()
        Senha = PasswordEntry.get()

        if (Name == "" or Email == "" or Usuário == "" or Senha == ""):
            messagebox.showerror(title='Erro de Registro', message='Preencha Todos os Campos')
        else:
            DataBase.cursor.execute("""
            INSERT INTO Users(Name, Email, Usuário, Senha) VALUES(?, ?, ?, ?)
            """, (Name, Email, Usuário, Senha))
            DataBase.conn.commit()
            messagebox.showinfo(title='Registrar', message='Usuário Criado com sucesso')

    #Botão Registrar 
    Register = ttk.Button(RightFrame, text='Registrar', width=20, command=RegisterToDataBase)
    Register.place(x=100, y=250)

    def BackToLoguin ():
        #removendo os componentes
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #trazendo de volta os Botões
        LoguiButton.place(x=72, y=210)
        RegistrarButton.place(x=100, y=250)

    #Botão voltar
    Back = ttk.Button(RightFrame,text='Voltar', width=20, command= BackToLoguin)
    Back.place(x=100, y=210)    

#REGISTRAR
RegistrarButton = ttk.Button(RightFrame, text='Registrar', width=20, command=Register)
RegistrarButton.place(x=100, y=250)


#encerra as atribuições a janela
jan.mainloop()

