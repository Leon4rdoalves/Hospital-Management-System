import tkinter
from menu import Menu
from funcionario import Func_Tela


def GET():
    global c_usuario, c_senha, erro
    user1 = c_usuario.get()
    pass1 = c_senha.get()

    if user1 == 'ebony' and pass1 == '123':
        Menu()

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

    cab = tkinter.Label(t_frame, text="\n\nGestão Hospitalar",
                        fg='green', font='Ubuntu 12')

    usuario = tkinter.Label(t_frame, text="Usuário: ")
    c_usuario = tkinter.Entry(t_frame)

    senha = tkinter.Label(b_frame, text="Senha: ")
    c_senha = tkinter.Entry(b_frame)

    login = tkinter.Button(b_frame, text="LOGIN", font='Ubuntu 8', command=GET)

    '''root.wm_iconbitmap(r"/home/ebony/git/Hospital-Management-System/icones/ebony_32.png")
    root.wm_iconbitmap(bitmap=None, default=None)
    img = tkinter.PhotoImage(file="/home/ebony/git/Hospital-Management-System/icones/hospital_128.ico")
    img = img.subsample(1, 1)
    labelimg = tkinter.Label(image=img, height="400", width="500")
    labelimg.pack()'''

    cab.pack()
    usuario.pack()
    c_usuario.pack()
    senha.pack()
    c_senha.pack()
    login.pack()
    root.title("Ebony Sys || Login")
    root.mainloop()


Entrada()