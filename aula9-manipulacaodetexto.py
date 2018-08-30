frase = 'curso em video python'
#python comeca a numerar os dados a partir de 0
print(frase[2])
# o contador final sempre vai ate uma indexacao anterior ex: 9:14    pegara os dados do 9 ate a celula 13
print(frase[9:14])
#contador inicial final e delta contador
print(frase[0:21:2])
#se omitir contador inicial o codigo interpretara inicio como 0
print(frase[:10])
#se omitir contador final o codigo ira ate o ultimo caractere
print(frase[9:])
#mostrar num de caracteres
print(len(frase))
#conta quantas vezes o 'o' aperece em frase
print(frase.count('o'))
#momento que inicia 'deo' em frase
print(frase.find('deo'))
#verifica se existe 'curso'
print('curso' in frase)
#substituir caracteres
print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip()) #remove espacos em branco antes e apos o incio e fim de 'frase'
print(frase.split()) #serapa 'frase' em diversas 'frases' dependendo do espacamento

# desafio
nome = input('digite nome: ')
sobrenome = input('digite sobrenome: ')
print('seu nome completo eh {} {}'.format(nome, sobrenome))

#=================DESAFIO===========================================

frase2 = str(input('digite uma frase: ')).strip()
print('a aparece {} vezes na frase'.format(frase2.count('a')))
print('primeira ocorrencia {}'.format(frase2.find('a')))
print('ultima ocorrencia {}'.format(frase2.rfind('a')))