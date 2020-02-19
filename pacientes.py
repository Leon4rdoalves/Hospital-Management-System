import tkinter


def PAT():
    rootpaciente = tkinter.Tk()
    rootpaciente.title("CADASTRAR PACIÊNTES")

    cadform = tkinter.Label(rootpaciente, text="FORMULÁRIO CADASTRO DE PACIÊNTES", font='Ubuntu 14')

    ID = tkinter.Label(rootpaciente, text="ID PACIENTE", font='Ubuntu 12', fg='blue')
    pat_ID = tkinter.Entry(rootpaciente, width=12)

    nome = tkinter.Label(rootpaciente, text="NOME COMPLETO DO PACIENTE: ", font='Ubuntu 12', fg='blue')
    pat_NOME = tkinter.Entry(rootpaciente, width=50)

    sexo = tkinter.Label(rootpaciente, text="SEXO: ", font='Ubuntu 12', fg='blue')
    pat_SEXO = tkinter.Entry(rootpaciente, width=5)

    nasc = tkinter.Label(rootpaciente, text="DATA DE NASCIMENTO (DD-MM-AAAA): ", font='Ubuntu 12', fg='blue')
    pat_NASC = tkinter.Entry(rootpaciente, width=26)

    gpsangue = tkinter.Label(rootpaciente, text="GRUPO SANGUÍNEO: ", font='Ubuntu 12', fg='blue')
    pat_GPSANGUE = tkinter.Entry(rootpaciente, width=5)

    tel1 = tkinter.Label(rootpaciente, text="TELEFONE: ", font='Ubuntu 12', fg='blue')
    pat_TEL1 = tkinter.Entry(rootpaciente, width=26)

    cel1 = tkinter.Label(rootpaciente, text="CELULAR: ", font='Ubuntu 12', fg='blue')
    pat_CEL1 = tkinter.Entry(rootpaciente, width=26)

    email = tkinter.Label(rootpaciente, text="EMAIL: ", font='Ubuntu 12', fg='blue')
    pat_EMAIL = tkinter.Entry(rootpaciente, width=50)

    equip = tkinter.Label(rootpaciente, text="EQUIPE RESPONSÁVEL: ", font='Ubuntu 12', fg='blue')
    pat_EQUIP = tkinter.Entry(rootpaciente, width=30)

    end = tkinter.Label(rootpaciente, text="ENDEREÇO COMPLETO: ", font='Ubuntu 12', fg='blue')
    pat_END = tkinter.Entry(rootpaciente, width=50)

    cadform.pack()
    ID.pack()
    pat_ID.pack()
    nome.pack()
    pat_NOME.pack()
    sexo.pack()
    pat_SEXO.pack()
    nasc.pack()
    pat_NASC.pack()
    gpsangue.pack()
    pat_GPSANGUE.pack()
    tel1.pack()
    pat_TEL1.pack()
    cel1.pack()
    pat_CEL1.pack()
    email.pack()
    pat_EMAIL.pack()
    equip.pack()
    pat_EQUIP.pack()
    end.pack()
    pat_END.pack()

    rootpaciente.mainloop()

