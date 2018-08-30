# tuplas sao imutaveis
# tuplas sao entre parenteses ()
#listas sao entre colchetes []
#dicionairios sao entre chaves {}
# lista(1:4) ira mostrar do item 1 ao 3 pois o ultimo eh excludente    (inicio:fim:delta)

lanche = ('hamburguer', 'pizza', 'suco', 'bosta')
for comida in lanche:
    print(f'{comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])

print(len(lanche))
print(type(lanche))
print(sorted(lanche))
print(lanche.count('hamburguer'))
print(lanche.index('suco'))

#printar em linhas separadas
print('a' '\n' 'b' '\n' 'c')
