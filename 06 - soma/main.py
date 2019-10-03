from tkinter import *

def bt_click():
    print('Botão Clicado!')
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):        
        num1 = int(ed1.get())
        num2 = int(ed2.get())

        soma = num1+num2

        lb['text'] = 'Resultado da soma de\n'+ed1.get()+' + '+ed2.get()+' = '+str(soma)

        print('Resultado da soma de\n'+ed1.get()+' + '+ed2.get()+' = '+str(soma))
    else:
        lb['text'] = 'Valores informado Inválido'
        print('Valores informado Inválido')

janela = Tk()

janela.title("Python TKinter Tutoriais")
janela["bg"] = "purple"

lb = Label(janela, text="Soma")
lb.place(x=80, y=50)

ed1 = Entry(janela)
ed1.place(x=80, y=100)

ed2 = Entry(janela)
ed2.place(x=80, y=150)

bt1 = Button(janela, width=20, text='Botão 1',
             command=bt_click)
bt1.place(x=70, y=200)


janela.geometry("300x300+550+0")
janela.mainloop
