s = c = n = 0
while n !=999:
    n = float(input('digite um numero: '))
    if n == 999:
        break
    s +=n
    c +=1
print(f'foram digitados {c} valors e a soma  deles eh {s}') #nova forma de printar sem usar o .format