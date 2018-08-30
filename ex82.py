resposta = 's'
lista = list()
pares = list()
impares = list()
while resposta == 's':
    n = int(input('digite: '))
    lista.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
    resposta = str(input('quer continuar? [s/n]  '))

print(lista)
print(pares)
print(impares)