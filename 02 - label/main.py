from tkinter import *

janela = Tk()

janela.title("Janela Principal")
janela["bg"] = "purple"

lb = Label(janela, text="Texto Label")
lb.place(x=100, y=100)

janela.geometry("300x300+200+200")

janela.mainloop
