#par ou impar
import random as rd
pc = n = res = 0
escolha = 'par'
while res !=1:
    pc = rd.randrange(10)
    escolha = str(input(' par ou impar:'))
    n = int(input('digite o numero: '))
    c = pc+n
    print(pc)
    if c%2 == 0:
        resposta = 'par'
    else:
        resposta =  'impar'
    if escolha in resposta:
        res = 0
        print('vc ganhou va novamente')
    else:
        res = 1
        print('vc perdeu')

