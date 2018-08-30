lista = list()
lista2 = list()
for i in range(0,5):
    n = int(input("digite: "))
    lista.append(n)
    print(lista)
while len(lista2) != 5:
    lista2.append(min(lista))
    lista.remove(min(lista))
print(lista2)
