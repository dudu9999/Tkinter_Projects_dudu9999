from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, text="Login: ", bg="white")
lb2 = Label(janela, text="Senha: ", bg="white")

ed1 = Entry(janela,  bg="white")
ed2 = Entry(janela,  bg="white")

bt1 = Button(janela, text="Confirmar")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)

ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)

bt1.grid(row=2, column=1)

janela.geometry("200x100+550+0")
janela.mainloop
