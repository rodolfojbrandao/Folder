expressao = str(input('digite uam expressao: '))
n = 0
for i in range(0, len(expressao)):
    if expressao[i]=='(':
        n =n + 1
    elif expressao[i]==')':
         n = n - 1
if n == 0:
    print('colchetes corretos')
elif n>0:
    print('falta fechar colchetes')
else:
    print('falta abrir colchetes')