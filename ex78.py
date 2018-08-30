lista = list()
for i in range(0,5):
    n = int(input("digite: "))
    lista.append(n)
print(lista)
maior = max(lista)
menor = min(lista)
pmax = lista.index(maior)
pmin = lista.index(menor)

print(f'da sua lista o maior numero foi {maior} na posicao {pmax}')
print(f'da sua lista o menor numero foi {menor} na posicao {pmin}')