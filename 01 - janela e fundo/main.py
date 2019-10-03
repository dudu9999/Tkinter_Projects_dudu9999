##import tkinter as tk
##
##janela = tk.Tk()
##
##janela.mainloop

# OU

import tkinter

janela = tkinter.Tk()
janela.title("Janela Principal")
janela["bg"]                  = "green" # coloca a cor de fundo
janela["background"] = "green" # ou assim.

# largura x Altura + Distancia da esquerda da tela + Distancia do topo da tela
# LxA+E+T
# 500x600+400+200 (medida em pixel)
janela.geometry("500x200+10+30") # tamano e local onde a janela vai ficar
# janela.geometry("+10+30")  # ou aasim que só escole o local onde a janela ai ficar


janela.mainloop
