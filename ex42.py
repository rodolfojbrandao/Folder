import random as rd

l1 = float(rd.uniform(1, 9.0))
l2 = float(rd.uniform(1, 9.0))
l3 = float(rd.uniform(1, 9.0))

if l1>l2+l3:
    print('isso n forma triangulo')
elif l2>l1+l3:
    print('isso n forma triangulo')
elif l3>l2+l1:
    print('isso n forma triangulo')
elif l1!=l2 and l1!=l3 and l2!=l3:
    tri = 'escaleno'
    print('o trigulo eh {} com lados {:.2f}, {:.2f} e {:.2f}'.format(tri, l1, l2, l3))
elif l1==l2 and l2==l3:
    tri = 'equilatero'
    print('o trigulo eh {} com lados {:.2f}, {:.2f} e {:.2f}'.format(tri, l1, l2, l3))
else:
    tri = 'isosceles'
    print('o trigulo eh {} com lados {:.2f}, {:.2f} e {:.2f}'.format(tri, l1, l2, l3))