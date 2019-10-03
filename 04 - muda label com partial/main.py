from tkinter import *

def bt_click1():
    print("Botao 1 clicado")
    lb['text'] = 'Funcionou 1'

def bt_click2():
    print("Botao 2 clicado")
    lb['text'] = 'Funcionou 2'

janela = Tk()

janela.title("Janela Principal")
janela["bg"] = "purple"

lb = Label(janela, text="Texto Label")
lb.place(x=120, y=100)

bt = Button(janela, width=20, text='Botão 1',
            command=bt_click1 )
bt.place(x=80, y=150)

bt = Button(janela, width=20, text='Botão 2',
            command=bt_click2 )
bt.place(x=80, y=190)

janela.geometry("300x300+200+200")
janela.mainloop
