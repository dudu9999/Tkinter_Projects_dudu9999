from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, text="Right", bg="blue")
lb2 = Label(janela, text="BOTTOM", bg="blue")
lb3 = Label(janela, text="LEFT", bg="green")
lb4 = Label(janela, text="TOP", bg="purple")

lb1.pack(side=RIGHT)
lb2.pack(side=BOTTOM)
lb3.pack(side=LEFT)
lb4.pack(side=TOP)

janela.geometry("300x300+550+0")
janela.mainloop
