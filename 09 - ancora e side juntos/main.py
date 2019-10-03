from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, text="SIDE 1", bg="blue")
lb2 = Label(janela, text="SIDE 2", bg="red")
lb3 = Label(janela, text="ANCHOR 1", bg="green")
lb4 = Label(janela, text="ANCHOR 2", bg="purple")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)
lb4.pack(side=BOTTOM, anchor=SW)

janela.geometry("300x300+550+0")
janela.mainloop
