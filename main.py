import tkinter.messagebox
from tkinter import *
import sympy as sp

import numpy as np
from sympy import sqrt
root = Tk()
root.title("Radici di numeri complessi")
root.geometry("500x400")


# Elaboration
def Elabora(Esponente, Parte_reale, Parte_immaginaria):
    n = pow(2, Esponente)

    complex = Parte_reale + Parte_immaginaria * sp.I

    angle = sp.arg(complex)
    module = sp.Abs(complex)

    angle = angle + sp.pi * 2

    theta = angle / n
    '''
    thetaval=str(theta)
    thetaval=thetaval.replace("pi","np.pi")
    thetaval=eval(thetaval)
    '''
    ##valore ="I risultati sono: \n\n"
    message="I risultati sono i seguenti:\n\n"
    P = sp.sqrt(module)

    message+="•\t"+str(sp.simplify(P * (sp.cos(theta) + sp.sin(theta) * sp.I)))+"\n"
    ##valore+=str(P*(np.cos(thetaval)+ np.sin(thetaval)*1j))

    for x in range(1, n):
        theta = theta + (2 * sp.pi / n)
        #thetaval= np.degrees(thetaval) + (360/n)
        message += "•\t"+str(sp.simplify(P * (sp.cos(theta) + sp.sin(theta) * sp.I)))+"\n"
        ##valore += str(P * (np.cos(thetaval) + np.sin(thetaval) * 1j))+"\n"

    tkinter.messagebox.showinfo("Radici", message)
    ##tkinter.messagebox.showinfo("Valori", valore)

    print(theta)
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
        tkinter.messagebox.showwarning("Risultato", "Il risultato uguale a "+Parte_reale+" + "+Parte_immaginaria+"i")

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
