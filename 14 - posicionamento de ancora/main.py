from tkinter import *

janela = Tk()

janela.title("Python TKinter Tutoriais")


lb1 = Label(janela, text="ESPAÇO", bg="blue", width='15', height=3)
lbHORIZONTAL = Label(janela, text="horizontal", bg="yellow")
lbVERTICAL = Label(janela, text="vertical", bg="red")

lb1.grid(row=0, column=0)
lbHORIZONTAL.grid(row=1, column=0, sticky=E)
lbVERTICAL.grid(row=0, column=1, sticky=N)

janela.geometry("200x100+550+0")
janela.mainloop
