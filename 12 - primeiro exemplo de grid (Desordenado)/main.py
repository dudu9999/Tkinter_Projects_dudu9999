from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, text="Label 1", bg="blue")
lb2 = Label(janela, text="Label 2", bg="red")
lb3 = Label(janela, text="Label 3", bg="green")
lb4 = Label(janela, text="Label 4", bg="purple")

lb1.grid(row=10, column=19)
lb2.grid(row=8, column=12)
lb3.grid(row=56, column=13)
lb4.grid(row=99, column=17)

janela.geometry("300x300+550+0")
janela.mainloop
