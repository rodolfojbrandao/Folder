import time

for c in range(10,-1,-1): #de um ate 10 de 2 em 2
    print(c)
    #time.sleep(1)
print('===============FELIZ ANO NOVO===============')
#lembrar que o python ignora uma unidade no fim do contador
#s = s +n ou s += n

#numeros pares de 1 ate 50
for c in range(0,51,2):
     print(c)

#soma dos multiplos de 3
s=0
for c in range(1,500):
    if c%3==0:
        s+=c
print(s)