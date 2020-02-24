import tkinter
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import INSERT


def PAT():
    rootpaciente = tkinter.Tk()
    rootpaciente.resizable(width=False, height=False)
    rootpaciente.geometry('600x570+0+0')
    rootpaciente.title("Ebony Sys || Cadastro de Pacientes")

    cadform = tkinter.Label(rootpaciente, text=".. ATENÇÃO AO PREENCHER ESTE FORMULÁRIO! ",
                            font='Ubuntu 13 italic', fg='green')
    cadform.place(x=25, y=15)

    ID = tkinter.Label(rootpaciente, text="ID Paciente:", font='Ubuntu 12', fg='gray')
    pat_ID = tkinter.Entry(rootpaciente, width=12)
    ID.place(x=25, y=55)
    pat_ID.place(x=125, y=55)

    nome = tkinter.Label(rootpaciente, text="Nome completo:", font='Ubuntu 12', fg='gray')
    pat_NOME = tkinter.Entry(rootpaciente, width=49)
    nome.place(x=25, y=95)
    pat_NOME.place(x=160, y=95)

    nasc = tkinter.Label(rootpaciente, text="Data de Nascimento: ", font='Ubuntu 12', fg='gray')
    pat_NASC = tkinter.Entry(rootpaciente, width=15)
    nasc.place(x=25, y=135)
    pat_NASC.place(x=190, y=135)

    sexo = tkinter.Label(rootpaciente, text="Sexo: ", font='Ubuntu 12', fg='gray')
    pat_SEXO = tkinter.Entry(rootpaciente, width=5)
    sexo.place(x=345, y=135)
    pat_SEXO.place(x=395, y=135)

    gpsangue = tkinter.Label(rootpaciente, text="T.S.: ", font='Ubuntu 12', fg='gray')
    pat_GPSANGUE = tkinter.Entry(rootpaciente, width=5)
    gpsangue.place(x=470, y=135)
    pat_GPSANGUE.place(x=509, y=135)

    tel = tkinter.Label(rootpaciente, text="Telefone: ", font='Ubuntu 12', fg='gray')
    pat_TEL = tkinter.Entry(rootpaciente, width=15)
    tel.place(x=25, y=175)
    pat_TEL.place(x=105, y=175)

    tel2 = tkinter.Label(rootpaciente, text='Telefone (Recado): ', font='Ubuntu 12', fg='gray')
    pat_TEL2 = tkinter.Entry(rootpaciente, width=15)
    tel2.place(x=279, y=175)
    pat_TEL2.place(x=429, y=175)

    cel = tkinter.Label(rootpaciente, text="Celular: ", font='Ubuntu 12', fg='gray')
    pat_CEL = tkinter.Entry(rootpaciente, width=15)
    cel.place(x=25, y=215)
    pat_CEL.place(x=92, y=215)

    email = tkinter.Label(rootpaciente, text="E-mail: ", font='Ubuntu 12', fg='gray')
    pat_EMAIL = tkinter.Entry(rootpaciente, width=33)
    email.place(x=230, y=215)
    pat_EMAIL.place(x=287, y=215)

    cep = tkinter.Label(rootpaciente, text='CEP: ', font='Ubuntu 12', fg='gray')
    pat_CEP = tkinter.Entry(rootpaciente, width='10')
    cep.place(x=25, y=255)
    pat_CEP.place(x=65, y=255)

    cidade = tkinter.Label(rootpaciente, text='Cidade: ', font='Ubuntu 12', fg='gray')
    pat_CIDADE = tkinter.Entry(rootpaciente, width='23')
    cidade.place(x=175, y=255)
    pat_CIDADE.place(x=240, y=255)

    estado = tkinter.Label(rootpaciente, text='Estado: ', font='Ubuntu 12', fg='gray')
    pat_ESTADO = tkinter.Entry(rootpaciente, width='3')
    estado.place(x=457, y=255)
    pat_ESTADO.place(x=525, y=255)

    rua = tkinter.Label(rootpaciente, text="Rua: ", font='Ubuntu 12', fg='gray')
    pat_RUA = tkinter.Entry(rootpaciente, width=42)
    rua.place(x=25, y=295)
    pat_RUA.place(x=65, y=295)

    num = tkinter.Label(rootpaciente, text='Nº: ', font='Ubuntu 12', fg='gray')
    pat_NUM = tkinter.Entry(rootpaciente, width=10)
    num.place(x=435, y=295)
    pat_NUM.place(x=469, y=295)

    comp = tkinter.Label(rootpaciente, text='Complemento: ', font='Ubuntu 12', fg='gray')
    pat_COMP = tkinter.Entry(rootpaciente, width=15)
    comp.place(x=25, y=335)
    pat_COMP.place(x=145, y=335)

    equip = tkinter.Label(rootpaciente, text="Equipe Responsável: ", font='Ubuntu 12', fg='gray')
    pat_EQUIP = tkinter.Entry(rootpaciente, width=45)
    equip.place(x=25, y=375)
    pat_EQUIP.place(x=187, y=375)

    obs = tkinter.Label(rootpaciente, text='Observação: ', font='Ubuntu 12', fg='gray')
    obs.place(x=25, y=415)
    pat_OBS = scrolledtext.ScrolledText(rootpaciente, width=51, height=6, fg='red')
    pat_OBS.insert(INSERT, ' Inclua informações seguindo o padrão!')
    pat_OBS.place(x=125, y=415)

    rootpaciente.mainloop()


PAT()
