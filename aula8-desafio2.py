#lista de alunos
import random
n1 = input('aluno 01: ')
n2 = input('aluno 02: ')
n3 = input('aluno 03: ')
n4 = input('aluno 04: ')

#lista fica entre couchetes

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('ESCOLHIDO foi {}'.format(escolhido))

random.shuffle(lista)
print('ORDEM foi {}'.format(lista))