import sympy as sp
from math import sqrt

def bisezione(obj, cs):
    if (obj == "sin"):
        return sp.sqrt((1 - cs) / 2)
    elif (obj == "cos"):
        return sp.sqrt((1 + cs) / 2)


n = 4
m = int(n/2)
complex = -16*sp.I
module = (sp.Abs(complex))
P = 2 ##TODO variabilize p
costeta = sp.re(complex) / module
sinteta = sp.im(complex) / module

for x in range (n):
    if (x%2==0):
        cosm =1
        sinm = 0
    else:
        cosm=-1
        sinm = 0

    costeta= (costeta*cosm)-(sinteta*sinm)
    sinteta= (costeta*sinm)+(sinteta*cosm)
    cosj = costeta
    sinj = sinteta
    coseni =[]
    sni =[]
    for y in range(m):

        sinj = bisezione("sin", cosj)

        for l in range(m):
            sni.append(-sinj)
            sni.append(sinj)

        cosj= bisezione("cos", cosj)

        for l in range(m):
            coseni.append(cosj)
            coseni.append(-cosj)

if n<=2:
    nsoluzioni =0
else:

    nsoluzioni = int(len(coseni)/2)

for x in range (nsoluzioni,n*2):

    print(P*(coseni[x] + sni[x]*sp.I))


