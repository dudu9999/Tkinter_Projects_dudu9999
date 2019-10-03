from tkinter import *

def bt_click():
    print("Botao clicado")
    lb['text'] = 'Funcionou'

janela = Tk()

janela.title("Janela Principal")
janela["bg"] = "purple"

lb = Label(janela, text="Texto Label")
lb.place(x=120, y=100)

bt = Button(janela, width=20, text='OK', command=bt_click )
bt.place(x=80, y=150)

janela.geometry("300x300+200+200")
janela.mainloop
