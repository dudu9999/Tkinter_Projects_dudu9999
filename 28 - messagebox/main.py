import tkinter
#import tkMessageBox
import tkinter.messagebox

tkMessageBox = tkinter.messagebox

top = tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Atenção", "Se deseja instalar\no virus clique em \"OK\" ")

B1 = tkinter.Button(top, text = "Clica em mim!", command=hello)
B1.pack()

top.mainloop()
