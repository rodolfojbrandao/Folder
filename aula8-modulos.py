#import emoji
import math
#from math import sqrt

# ao usar from modulo import nao sera mais necessario escrever modulo.xxx, yyy e sim apenas a funcao xxxx
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
#raiz = sqrt(num)
print('a raiz de {} eh igual a {:.2f}'.format(num, raiz))
# {:.2f} mostra apenas 2 casas decimais
#print(emoji.emojize("ola :sunglasses:", use_aliases=True))
