from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, text="HORIZONTAL TOP\nEM CIMA", bg="blue")
lb2 = Label(janela, text="LEFT\nESQUERDA", bg="red")
lb3 = Label(janela, text="RIGHT----------------\nDIREITA--------------", bg="green")
lb4 = Label(janela, text="BOTTOM\nEM BAIXO\n1\n2\n3\n4", bg="purple")

lb1.pack(side=TOP, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)
lb4.pack(side=BOTTOM, fill=X)

janela.geometry("300x300+550+0")
janela.mainloop
