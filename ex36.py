casa = float(input('digite o valor da casa: '))
salario = float(input('digite seu salario: '))
vezes = float(input('digite quantidade de vezes em anos: '))

v1 = casa/(vezes*12)
v2 = salario*0.3
if v1>=v2:
    print('financiamento recusado, seu salario deveria ser de {:.2f}'.format(v1/0.3))
else:
    print('financiamento aceito, o valor da parcela eh de {:.2f}'.format(v1))