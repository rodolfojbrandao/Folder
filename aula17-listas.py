lista = ['b','c','d']
print(lista)

lista.append('e')
print(lista)

lista.insert(0,'a') # inserir 'a' na posicao 0
print(lista)

del lista[3]
print(lista)

lista.pop(2)
print(lista)

lista.remove('b')
print(lista)

valor = list(range(0,10))
print(valor)

valor2 = [8,4,6,2,1]
print(valor2)

valor2.sort()
print(valor2)

valor2.sort(reverse=True)
print(valor2)

print(len(valor2))

remocao = int(input('digite o valor a ser removido: '))
if remocao in valor2:
    valor2.remove(remocao)
    print(valor2)
else:
    print(f'valor {remocao} nao encontrado')