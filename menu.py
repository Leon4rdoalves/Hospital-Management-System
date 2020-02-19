import tkinter
import sqlite3
import tkinter.messagebox


def Menu():
    global root1, botão1, botão2, botão3, botão4, botão5, botão6

    root1 = tkinter.Tk()
    root1.geometry('280x350')
    root1.title("Ebony Sys || Menu")
    m = tkinter.Label(root1, text="MENU", font='Ubuntu 12', fg='gray')

    botão1 = tkinter.Button(root1, text="PACIENTE", bg='light blue', fg='black', font='Ubuntu 8')
    botão2 = tkinter.Button(root1, text="Nº DO QUARTO", bg='light green', fg='black', font='Ubuntu 8')
    botão3 = tkinter.Button(root1, text="FUNCIONÁRIOS", bg='light blue', fg='black', font='Ubuntu 8')
    botão4 = tkinter.Button(root1, text="RESERVAS", bg='light green', fg='black', font='Ubuntu 8')
    botão5 = tkinter.Button(root1, text="FINANCEIRO", bg='red', fg='black', font='Ubuntu 8')
    botão6 = tkinter.Button(root1, text="SAIR", bg='yellow', fg='black', font='Ubuntu 8')

    m.place(x=75, y=5)

    botão1.pack(side=tkinter.TOP)
    botão1.place(x=80, y=50)

    botão2.pack(side=tkinter.TOP)
    botão2.place(x=80, y=100)

    botão3.pack(side=tkinter.TOP)
    botão3.place(x=80, y=150)

    botão4.pack(side=tkinter.TOP)
    botão4.place(x=80, y=200)

    botão5.pack(side=tkinter.TOP)
    botão5.place(x=80, y=250)

    botão6.pack(side=tkinter.TOP)
    botão6.place(x=80, y=300)

    root1.mainloop()




