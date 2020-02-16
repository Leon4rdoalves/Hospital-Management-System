import tkinter


def Get():
    global c_usuario, c_senha, erro
    pass
    erro = tkinter.Label(b_frame, text='Usuário e/ou Senha, incorretos!', fg='red', font='bold')
    erro.pack()


def Entrada():
    global c_usuario, c_senha, login, t_frame, b_frame, imagem
    root = tkinter.Tk()
    root.geometry('280x250')
    t_frame = tkinter.Frame(root)
    t_frame.pack()

    b_frame = tkinter.Frame(root)
    b_frame.pack()

    cab = tkinter.Label(t_frame, text="Gestão Hospitalar",
                        bg='black', fg='green', font='Ubuntu 12')

    usuario = tkinter.Label(t_frame, text="Usuário: ")
    c_usuario = tkinter.Entry(t_frame)

    senha = tkinter.Label(b_frame, text="Senha: ")
    c_senha = tkinter.Entry(b_frame)

    login = tkinter.Button(b_frame, text="LOGIN", font='Ubuntu 8', command=Get)

    cab.pack()
    usuario.pack()
    c_usuario.pack()
    senha.pack()
    c_senha.pack()
    login.pack()
    root.title("Ebony System #Login")
    root.mainloop()


Entrada()
