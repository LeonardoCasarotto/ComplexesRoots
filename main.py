import tkinter.messagebox
from tkinter import *
import sympy as sp

import numpy as np
from sympy import sqrt
root = Tk()
root.title("Radici di numeri complessi")
root.geometry("500x400")

def bisezione(obj, cs):
    if (obj == "sin"):
        return sp.sqrt((1 - cs) / 2)
    elif (obj == "cos"):
        return sp.sqrt((1 + cs) / 2)


# Elaboration
def Elabora(Esponente, Parte_reale, Parte_immaginaria):

    n = pow(2, Esponente)
    m = int(n / 2)
    complex = Parte_reale + Parte_immaginaria * sp.I

    # calcolo dati iniziali
    module = (sp.Abs(complex))
    P = module
    for x in range(Esponente):
        P = sp.sqrt(P)

    costeta = sp.re(complex) / module
    sinteta = sp.im(complex) / module

    coseni = []
    sini = []

    for x in range(m):
        sinm = 0
        if x % 2 == 0:
            cosm = 1
        elif x % 2 == 1:
            cosm = -1

        costeta = sp.simplify((costeta * cosm) - (sinteta * sinm))
        sinteta = sp.simplify((sinteta * cosm) + (costeta * sinm))

        for y in range(m):
            sinteta = bisezione("sin", costeta)
            costeta = bisezione("cos", costeta)

        for l in range(m):
            sini.append(sinteta)
            sini.append(-sinteta)
            coseni.append(costeta)
            coseni.append(-costeta)

    message=""
    for x in range(n):
        message+="• \t"+(str(P * (coseni[x] + sini[x] * sp.I)))+"\n"

    tkinter.messagebox.showinfo("Soluzioni", message)


def errore():
    tkinter.messagebox.showwarning("Errore", "Inserire correttamente i dati")




def guarda(Esponente, Parte_reale, Parte_immaginaria):
    if Esponente=="" or Parte_reale=="" or Parte_immaginaria=="":
        errore()
    else:
        try:



            Parte_immaginaria= eval(Parte_immaginaria)
            Parte_reale= eval(Parte_reale)
            Parte_immaginaria =int(Parte_immaginaria)
            Parte_reale = int(Parte_reale)
            Esponente=int(Esponente)

        except ValueError:
            errore()
        except NameError:
            errore()


    if(Esponente==0):
        tkinter.messagebox.showwarning("Risultato", "Il risultato uguale a 1 ")

    else:
        Elabora(Esponente, Parte_reale, Parte_immaginaria)


# UI
Label_reale = Label(root, text="Parte reale:")
Label_reale.grid(row=0, column=0)

Parte_reale = Entry(root, width=10, text="", )
Parte_reale.grid(row=0, column=1)

label_immaginaria = Label(root, text="Parte immaginaria:")
label_immaginaria.grid(row=1, column=0)

Parte_immaginaria = Entry(root, width=10, text="Parte Immaginaria", )
Parte_immaginaria.grid(row=1, column=1)

Label_Esponente = Label(root, text="Esponente di 2 → (2^n):")
Label_Esponente.grid(row=2, column=0)
Esponente = Entry(root, width=10, text="Esponente di 2", )
Esponente.grid(row=2, column=1)

Confirm = Button(root, text="Calcola",
                 command=lambda: guarda(Esponente.get(), Parte_reale.get(), Parte_immaginaria.get()))

Confirm.grid(row=3, column=1)
root.mainloop()
