sexo = str(input('digite seu sexo [M/F]: ')).upper()
while sexo not in 'MF':
    print('errou burro')
    sexo = str(input('digite seu sexo [M/F]: ')).upper()
print('sexo eh {}'.format(sexo))