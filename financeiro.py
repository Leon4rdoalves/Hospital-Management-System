import tkinter
import sqlite3


def Financeiro():
    rootfinanceiro = tkinter.Tk()
    rootfinanceiro.geometry('650x450')
    rootfinanceiro.title('DADOS FINANCEIROS')
    cab = tkinter.Label(rootfinanceiro, text='DADOS FINANCEIROS DO PACIENTE', font='Ubuntu 14', fg='gray')
    cab.place(x=100, y=10)

    id = tkinter.Label(rootfinanceiro, text='ID DO PACIENTE')
    id.place(x=20, y=60)
    p_id = tkinter.Entry(rootfinanceiro)
    p_id.place(x=100, y=60)

    dt = tkinter.Label(rootfinanceiro, text='DATA: ')
    dt.place(x=20, y=60)
    p_dt = tkinter.Entry(rootfinanceiro)
    p_dt.place(x=135, y=100)

    ddp = tkinter.Button(rootfinanceiro, text='ATUALIZAR DATA')
    ddp.place(x=270, y=100)
    tratamento = tkinter.Label(rootfinanceiro, text='TIPO DE TRATAMENTO: ')
    tratamento.place(x=20, y=140)

    # Listbox aqui

    custo = tkinter.Label(rootfinanceiro, text='CUSTO: ')
    custo.place(x=315, y=140)
    custo_t = tkinter.Entry(rootfinanceiro, width=5)
    custo_t.place(x=350, y=140)

    remedio = tkinter.Label(rootfinanceiro, text='SELECIONAR  MEDICAMENTO: ')
    remedio.place(x=20, y=180)
    remedio_qtd = tkinter.Label(rootfinanceiro, text='QUANTIDADE: ')
    remedio_qtd.place(x=240, y=180)
    remedio_valor = tkinter.Label(rootfinanceiro, text='PREÇO: ')
    remedio_valor.place(x=315, y=180)
    remedio_valor1 = tkinter.Entry(rootfinanceiro, width=5)
    remedio_valor1.place(x=360, y=180)

    rootfinanceiro.mainloop()


Financeiro()
