from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, text="Label 1", bg="blue")
lb2 = Label(janela, text="Label 2", bg="blue")
lb3 = Label(janela, text="Label 3", bg="green")
lb4 = Label(janela, text="Label 4", bg="purple")
lb5 = Label(janela, text="Label 5", bg="purple")
lb6 = Label(janela, text="Label 6", bg="green")
lb7 = Label(janela, text="Label 7", bg="pink")
lb8 = Label(janela, text="Label 8", bg="pink")
lb9 = Label(janela, text="Label 9", bg="green")
lb10 = Label(janela, text="Label 10", bg="green")
lb11 = Label(janela, text="Label 11", bg="green")
lb0 = Label(janela, text="Label 0", bg="red")


lb0.pack(side=TOP)
lb10.pack(side=TOP)
lb1.pack(side=TOP)
lb11.pack(side=TOP)
lb6.pack(side=LEFT)
lb3.pack(side=RIGHT)
lb4.pack(side=BOTTOM)
lb5.pack(side=TOP)
lb2.pack(side=LEFT)
lb7.pack(side=RIGHT)
lb8.pack(side=BOTTOM)
lb9.pack(side=BOTTOM)



janela.geometry("300x300+550+0")
janela.mainloop
