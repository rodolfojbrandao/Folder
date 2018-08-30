#ex: carro.siga()
#carro eho objeto e siga o método... método sempre deve ser utilizado com parenteses no final
#condicional if termina com dois pontosex if carro.esquerda(): xxxxxx else:

#tempo = int(input('digite tempo de uso do carro: '))
#if tempo<3:
   # print('carro novo')
#else:
    #print('carro velho')
#print('exemplo 01 condicional')

#print('carro novo'if tempo<2 else 'carro velho')

#=========DESAFIO==========

#n = float(input('digite a velocidade do carro em km/h: '))
#if n>=80:
  #  print('voce ultrapassou o limite de velocidade')
  #  multa = (n-80)*7
  #  print('o valor de sua multa foi de {} reais'.format(multa))

#n1 = int(input('digite um numero: '))
#if n1%2==0:
  #  print('numero eh par')
#else:
   # print('numero eh impar')

m1 = float(input('digite o primeiro numero: '))
m2 = float(input('digite o segundo numero: '))
m3 = float(input('digite o terceiro numero: '))

m1m2 = m1-m2
m1m3 = m1-m3
m2m3 = m2-m3

if m1m2>0:
    maior = m1
    if m1m3 > 0:
        maior = m1
    else:
        maior = m3
else:
    maior = m2
    if m2m3 > 0:
        maior = m2
    else:
        maior = m3

if m1m2<0:
    menor = m1
    if m1m3 < 0:
        menor = m1
    else:
        menor = m3
else:
    menor = m2
    if m2m3 < 0:
        menor = m2
    else:
        menor = m3

print('maior eh {}'.format(maior))
print('menor eh {}'.format(menor))

