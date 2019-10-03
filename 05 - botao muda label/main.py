from functools import partial
from tkinter import *

def bt_click(botao):
    print(ed.get())
    lb['text'] = ed.get()

janela = Tk()

janela.title("Janela Principal")
janela["bg"] = "purple"

lb = Label(janela, text="Texto")
lb.place(x=80, y=100)



ed = Entry(janela)
ed.place(x=80, y=150)

bt1 = Button(janela, width=20, text='Botão 1')
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=80, y=190)


janela.geometry("300x300+550+0")
janela.mainloop
