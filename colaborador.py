import tkinter


def Func_Tela():
    rootfunc = tkinter.Tk()
    rootfunc.geometry('600x475+0+0')
    rootfunc.resizable(width=False, height=False)

    rootfunc.title('Ebony Sys || Colaboradores')

    var = tkinter.StringVar(master=rootfunc)

    cadfunc = tkinter.Label(rootfunc, text='.. CADASTRO DE COLABORADORES', fg='green', font='Ubuntu 13 italic')
    cadfunc.place(x=25, y=15)

    func1 = tkinter.Label(rootfunc, text='ID colaborador: ', fg='gray', font='Ubuntu 12')
    tx1 = tkinter.Entry(rootfunc, width=12)
    func1.place(x=25, y=55)
    tx1.place(x=152, y=55)

    func2 = tkinter.Label(rootfunc, text='Nome completo: ', fg='gray', font='Ubuntu 12')
    tx2 = tkinter.Entry(rootfunc, width=49)
    func2.place(x=25, y=95)
    tx2.place(x=160, y=95)

    func3 = tkinter.Label(rootfunc, text='Sexo: ', fg='gray', font='Ubuntu 12')
    rdm3 = tkinter.Radiobutton(rootfunc, variable='func_sexo_masc', text='Masculino', value='M', fg='gray', font='Ubuntu 12')
    rdf3 = tkinter.Radiobutton(rootfunc, variable='func_sexo_femi', text='Feminino', value='F', fg='gray', font='Ubuntu 12')
    func3.place(x=25, y=135)
    rdm3.place(x=70, y=135)
    rdf3.place(x=180, y=135)

    func4 = tkinter.Label(rootfunc, text='CPF: ', fg='gray', font='Ubuntu 12')
    tx4 = tkinter.Entry(rootfunc, width=14)
    func4.place(x=25, y=175)
    tx4.place(x=65, y=175)

    func10 = tkinter.Label(rootfunc, text='RG: ', fg='gray', font='Ubuntu 12')
    tx10 = tkinter.Entry(rootfunc, width=12)
    func10.place(x=205, y=175)
    tx10.place(x=240, y=175)

    func20 = tkinter.Label(rootfunc, text='Data Nasc.: ', fg='gray', font='Ubuntu 12')
    tx20 = tkinter.Entry(rootfunc, width='10')
    func20.place(x=375, y=175)
    tx20.place(x=470, y=175)

    func5 = tkinter.Label(rootfunc, text='Telefone: ', fg='gray', font='Ubuntu 12')
    tx5 = tkinter.Entry(rootfunc, width=15)
    func5.place(x=25, y=215)
    tx5.place(x=105, y=215)

    func6 = tkinter.Label(rootfunc, text='celular: ', fg='gray', font='Ubuntu 12')
    tx6 = tkinter.Entry(rootfunc, width=15)
    func6.place(x=365, y=215)
    tx6.place(x=430, y=215)

    func7 = tkinter.Label(rootfunc, text='E-mail: ', fg='gray', font='Ubuntu 12')
    tx7 = tkinter.Entry(rootfunc, width=58)
    func7.place(x=25, y=255)
    tx7.place(x=85, y=255)

    func8 = tkinter.Label(rootfunc, text='Função: ', fg='gray', font='Ubuntu 12')
    medi8 = tkinter.Radiobutton(rootfunc, variable='função', text='Médica(o)', value='M', fg='gray', font='Ubuntu 12')
    enfe8 = tkinter.Radiobutton(rootfunc, variable='função', text='Enfermeira(o)', value='F', fg='gray', font='Ubuntu 12')
    rece8 = tkinter.Radiobutton(rootfunc, variable='função', text='Recepçionista', value='R', fg='gray', font='Ubuntu 12')
    dprh8 = tkinter.Radiobutton(rootfunc, variable='função', text='Dptº RH', value='RH', fg='gray', font='Ubuntu 12')
    dpti8 = tkinter.Radiobutton(rootfunc, variable='função', text='Dptº TI', value='TI', fg='gray', font='Ubuntu 12')
    limp8 = tkinter.Radiobutton(rootfunc, variable='função', text='Limpeza', value='L', fg='gray', font='Ubuntu 12')
    func8.place(x=25, y=295)
    medi8.place(x=70, y=325)
    enfe8.place(x=220, y=325)
    rece8.place(x=400, y=325)
    dprh8.place(x=70, y=355)
    dpti8.place(x=220, y=355)
    limp8.place(x=400, y=355)

    func9 = tkinter.Label(rootfunc, text='Plantão: ', fg='gray', font='Ubuntu 12')
    um = tkinter.Radiobutton(rootfunc, variable='plantão', text='1', value='Um', fg='gray', font='Ubuntu 12')
    dois = tkinter.Radiobutton(rootfunc, variable='plantão', text='2', value='Dois', fg='gray', font='Ubuntu 12')
    tres = tkinter.Radiobutton(rootfunc, variable='plantão', text='3', value='Três', fg='gray', font='Ubuntu 12')
    quatro = tkinter.Radiobutton(rootfunc, variable='plantão', text='4', value='Quatro', fg='gray', font='Ubuntu 12')
    cinco = tkinter.Radiobutton(rootfunc, variable='plantão', text='5', value='Cinco', fg='gray', font='Ubuntu 12')
    seis = tkinter.Radiobutton(rootfunc, variable='plantão', text='6', value='Seis', fg='gray', font='Ubuntu 12')
    ns = tkinter.Radiobutton(rootfunc, variable='plantão', text='N/S', value='NS', fg='gray', font='Ubuntu 12')
    func9.place(x=25, y=395)
    um.place(x=70, y=425)
    dois.place(x=140, y=425)
    tres.place(x=210, y=425)
    quatro.place(x=280, y=425)
    cinco.place(x=350, y=425)
    seis.place(x=420, y=425)
    ns.place(x=490, y=425)
    rootfunc.mainloop()


Func_Tela()
