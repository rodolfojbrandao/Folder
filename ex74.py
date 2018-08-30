import random as rd
menor = 1000
maior = 0
for i in range(0,5):
    if i == 1:
        a = rd.random()
        if a<menor:
            menor = a
        if a>maior:
            maior = a
    elif i == 2:
        b = rd.random()
        if b<menor:
            menor = b
        if b>maior:
            maior = b
    elif i == 3:
        c = rd.random()
        if c<menor:
            menor = c
        if c>maior:
            maior = c
    elif i == 4:
        d = rd.random()
        if d<menor:
            menor = d
        if d>maior:
            maior = d
    else:
        e = rd.random()
        if e<menor:
            menor = e
        if e>maior:
            maior = e

tupla = (a, b, c, d, e)
lista = [a, b, c, d, e]
dicionario = {a, b, c, d, e}
print(type(tupla)) #tuple
print(type(lista)) #lista
print(type(dicionario)) #dicionario
print(tupla)
print(maior)
print(menor)
