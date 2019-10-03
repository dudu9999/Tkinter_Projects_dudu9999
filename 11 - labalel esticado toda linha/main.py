from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, text="Linha 1", bg="blue")
lb2 = Label(janela, text="Linha 2", bg="red")
lb3 = Label(janela, text="Linha 3", bg="green")
lb4 = Label(janela, text="Linha 4", bg="purple")

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP,fill=BOTH, expand=1)

janela.geometry("300x300+550+0")
janela.mainloop
