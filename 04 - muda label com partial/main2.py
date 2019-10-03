from functools import partial
from tkinter import *

def bt_click(botao):
    print(botao["text"])
    lb['text'] = 'Botao clicado foi o '+botao["text"]

janela = Tk()

janela.title("Janela Principal")
janela["bg"] = "purple"

lb = Label(janela)
lb.place(x=80, y=100)

bt1 = Button(janela, width=20, text='Botão 1')
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=80, y=150)

bt2 = Button(janela, width=20, text='Botão 2')
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=80, y=190)

janela.geometry("300x300+200+200")
janela.mainloop
