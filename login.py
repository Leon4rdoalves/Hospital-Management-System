import tkinter
from menu import Menu


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
    root.resizable(width=False, height=False)
    root.geometry('280x290+0+0')
    root.title("Ebony Sys || Login")

    image = tkinter.PhotoImage(file='/home/ebony/git/Hospital-Management-System/icones/128p.png')
    image = image.subsample(4, 4)

    labelimage = tkinter.Label(image=image)
    labelimage.place(x=120, y=127, relwidth=1.0, relheight=1.0)

    t_frame = tkinter.Frame(root)
    t_frame.pack()
    b_frame = tkinter.Frame(root)
    b_frame.pack()

    cab = tkinter.Label(t_frame, text="\nGestão Hospitalar\n", fg='green', font='Ubuntu 18 italic')

    usuario = tkinter.Label(t_frame, text="Usuário: ")
    c_usuario = tkinter.Entry(t_frame, bg='light gray')

    senha = tkinter.Label(b_frame, text="Senha: ")
    c_senha = tkinter.Entry(b_frame, bg='light gray')

    login = tkinter.Button(b_frame, text="LOGIN", bg='light green', font='Ubuntu 8', bd=2, relief='raised'
                           , highlightcolor='orange', activebackground='orange', command=GET)

    cab.pack()
    usuario.pack()
    c_usuario.pack()
    senha.pack()
    c_senha.pack()
    login.pack()
    root.mainloop()


Entrada()
