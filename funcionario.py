import tkinter


def Func_Tela():
    rootfunc = tkinter.Tk()
    rootfunc.geometry('400x400')
    rootfunc.title('FUNCIONÁRIOS')

    var = tkinter.StringVar(master=rootfunc)

    H = tkinter.Label(rootfunc, text='CADASTRO DE FUNCINÁRIOS', fg='gray', font='Ubuntu 14')
    H.place(x=50, y=20)

    func1 = tkinter.Label(rootfunc, text='ID FUNCIONÁRIO: ', fg='black', font='Ubuntu 12')
    func1.place(x=50, y=50)
    tx1 = tkinter.Entry(rootfunc)
    tx1.place(x=170, y=50)

    func2 = tkinter.Label(rootfunc, text='NOME: ', fg='black', font='Ubuntu 12')
    func2.place(x=50, y=80)
    tx2 = tkinter.Entry(rootfunc)
    tx2.place(x=170, y=80)

    func3 = tkinter.Label(rootfunc, text='SEXO: ', fg='black', font='Ubuntu 12')
    func3.place(x=50, y=110)
    rdm3 = tkinter.Radiobutton(rootfunc, text='MASCULINO', value='M')
    rdm3.place(x=80, y=110)
    rdf3 = tkinter.Radiobutton(rootfunc, text='FEMININO', value='F')
    rdf3.place(x=150, y=110)

    func4 = tkinter.Label(rootfunc, text='IDADE: ', fg='black', font='Ubuntu 12')
    func4.place(x=50, y=140)
    tx4 = tkinter.Entry(rootfunc)
    tx4.place(x=80, y=140)

    func5 = tkinter.Label(rootfunc, text='FUNÇÃO: ', fg='black', font='Ubuntu 12')
    func5.place(x=50, y=170)
    scrollbar = tkinter.Scrollbar(rootfunc, width=2)
    scrollbar.place(x=260, y=140)

    '''lista = tkinter.Listbox(rootfunc, selectmode='SINGLE', exportselection=0, heigth=1, width=15)
    lista.insert(tkinter.END, 'DOUTOR')
    lista.insert(tkinter.END, 'ENFERMEIRO')
    lista.insert(tkinter.END, 'RECEPCIONISTA')
    lista.place(x=150, y=170)
    lista.config(yscroollcommand=scrollbar.set)
    scrollbar.configure(command=lista.yview())'''

    func6 = tkinter.Label(rootfunc, text='SALÁRIO: ', fg='black', font='Ubuntu 12')
    func6.place(x=50, y=200)
    tx6 = tkinter.Entry(rootfunc)
    tx6.place(x=110, y=200)

    func7 = tkinter.Label(rootfunc, text='TELEFONE: ', fg='black', font='Ubuntu 12')
    func7.place(x=50, y=230)
    tx7 = tkinter.Entry(rootfunc)
    tx7.place(x=140, y=230)

    func8 = tkinter.Label(rootfunc, text='EMAIL: ', fg='black', font='Ubuntu 12')
    func8.place(x=50, y=260)
    tx8 = tkinter.Entry(rootfunc)
    tx8.place(x=140, y=260)

    rootfunc.mainloop()


