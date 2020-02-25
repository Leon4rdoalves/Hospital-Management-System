import tkinter
import sqlite3
import tkinter.messagebox
from paciente import PAT


def Menu():
    global root1, botão1, botão2, botão3, botão4, botão5, botão6

    root1 = tkinter.Tk()
    root1.resizable(width=False, height=False)
    root1.geometry('600x305+0+0')
    root1.title("Ebony Sys || Menu")
    m = tkinter.Label(root1, text=".. MENU PRINCIPAL ", font='Ubuntu 13 italic', fg='green')
    m.place(x=25, y=15)

    botão1 = tkinter.Button(root1, text="PACIENTE", bg='light blue', fg='black', font='Ubuntu 8 bold',
                            bd=2, relief='raised', highlightcolor='orange', activebackground='orange',
                            width=16, height=1)
    botão2 = tkinter.Button(root1, text="Nº DO QUARTO", bg='light green', fg='black', font='Ubuntu 8 bold',
                            bd=2, relief='raised', highlightcolor='orange', activebackground='orange',
                            width=16, height=1)
    botão3 = tkinter.Button(root1, text="COLABORADORES", bg='light blue', fg='black', font='Ubuntu 8 bold',
                            bd=2, relief='raised', highlightcolor='orange', activebackground='orange',
                            width=16, height=1)
    botão4 = tkinter.Button(root1, text="RESERVAS", bg='light green', fg='black', font='Ubuntu 8 bold',
                            bd=2, relief='raised', highlightcolor='orange', activebackground='orange',
                            width=16, height=1)
    botão5 = tkinter.Button(root1, text="FINANCEIRO", bg='light blue', fg='black', font='Ubuntu 8 bold',
                            bd=2, relief='raised', highlightcolor='orange', activebackground='orange',
                            width=16, height=1)
    botão6 = tkinter.Button(root1, text="SAIR", bg='yellow', fg='black', font='Ubuntu 8 bold',
                            bd=2, relief='raised', highlightcolor='orange', activebackground='orange',
                            width=16, height=1)

    botão1.pack(side=tkinter.TOP)
    botão1.place(x=25, y=50)
    m1 = tkinter.Label(root1, text='Cadastrar/ Alterar dados dos Pacientes.', font='Ubuntu 12 italic', fg='gray')
    m1.place(x=152, y=53)

    botão2.pack(side=tkinter.TOP)
    botão2.place(x=25, y=90)
    m2 = tkinter.Label(root1, text='Atribuir/ Desatribuir Pacientes à Quartos.', font='Ubuntu 12 italic', fg='gray')
    m2.place(x=152, y=93)

    botão3.pack(side=tkinter.TOP)
    botão3.place(x=25, y=130)
    m3 = tkinter.Label(root1, text='Cadastrar/ Alterar dados dos Colaboradores.', font='Ubuntu 12 italic', fg='gray')
    m3.place(x=152, y=133)

    botão4.pack(side=tkinter.TOP)
    botão4.place(x=25, y=170)
    m4 = tkinter.Label(root1, text='Cadastrar/ Alterar Reservas.', font='Ubuntu 12 italic', fg='gray')
    m4.place(x=152, y=173)

    botão5.pack(side=tkinter.TOP)
    botão5.place(x=25, y=210)
    m5 = tkinter.Label(root1, text='Verificar/ Alterar dados Financeiros.', font='Ubuntu 12 italic', fg='gray')
    m5.place(x=152, y=213)

    botão6.pack(side=tkinter.TOP)
    botão6.place(x=25, y=250)
    m6 = tkinter.Label(root1, text='Finalizar o Sistema.', font='Ubuntu 12 italic', fg='gray')
    m6.place(x=152, y=253)

    root1.mainloop()


Menu()