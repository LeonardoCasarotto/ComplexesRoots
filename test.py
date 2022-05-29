import sympy as sp
from math import sqrt

#funzione bisezione
def bisezione(obj, cs):
    if (obj == "sin"):
        return sp.sqrt((1 - cs) / 2)
    elif (obj == "cos"):
        return sp.sqrt((1 + cs) / 2)

#dati
Esponente= 2
n = pow(2,Esponente)
m = int(n/2)
complex = -16

#calcolo dati iniziali
module = (sp.Abs(complex))
P=module
for x in range (Esponente):
    P=sp.sqrt(P)

costeta = sp.re(complex) / module
sinteta = sp.im(complex) / module

# somma sini e cos
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

        # SIN
        sinteta = bisezione("sin", costeta)
        for l in range(m):
            sini.append(sinteta)
            sini.append(-sinteta)
            # COS
        costeta = bisezione("cos", costeta)
        for l in range(m):
            coseni.append(costeta)
            coseni.append(-costeta)

if n <= 2:
    nsoluzioni = 0
    fine = n
else:

    nsoluzioni = int(len(coseni) / 2)
    fine = n * 2

print(sini)
print(coseni)
for x in range(nsoluzioni, fine):
    print(P * (coseni[x] + sini[x] * sp.I))
