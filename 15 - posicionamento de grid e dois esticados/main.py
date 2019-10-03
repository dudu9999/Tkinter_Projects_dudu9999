from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, bg="red",      width='15', height=6)
lb2 = Label(janela, bg="blue",    width='15', height=6)
lb3 = Label(janela, bg="black",  width='15', height=6)
lb4 = Label(janela, bg="yellow", width='15', height=6)

lb5 = Label(janela, text="horizontal", bg="green", height=3)
lb6 = Label(janela, text="vertical", bg="pink", width='7')

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
lb3.grid(row=0, column=1)
lb4.grid(row=1, column=1)
lb5.grid(row=2, column=0, columnspan=2, sticky=W+E)
lb6.grid(row=0, column=2, rowspan=3, sticky=N+S)

janela.geometry("300x300+550+0")
janela.mainloop
