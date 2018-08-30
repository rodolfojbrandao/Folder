# caso int n seja usado o numero sera interpretado como string

n1 = int(input('digite um numero '))
n2 = float(input('digite um numero '))

print(type(n1))

s = n1+n2


print('a soma emtre {} e {} vale {}'.format(n1, n2, s))