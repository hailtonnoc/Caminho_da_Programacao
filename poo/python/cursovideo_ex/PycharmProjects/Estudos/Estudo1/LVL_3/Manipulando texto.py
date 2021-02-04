print('_'*18)
print('Desafios')
print('-'*18)

print()
print('Desafio 22')
#Ler um nome completo, mostrar maiusculas, minusculas, quantas letras(ou seja sem os espaços), quantas letras tem no primeiro nome
nome = input('Qual seu nome? ').strip()
nome_s = nome.split()
print(nome.upper())
print(nome.lower())
print('A quantidade de letras são ', (int(len(nome)))-int(nome.count(' ')))
print('-'*27)
nome_1 = (nome_s[0])
print(nome_1)
print('Quantidade de letras do primeiro nome é {}'.format(len(nome_1)))

print()
print('Desafio 23')
#Leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados, por casas numericas unidade, dezena, centena, e milhar
numeros = int(input('Qual numero gostaria de analizar? '))
#base = int((len(numeros))-1)

uni = numeros // 1 % 10
print('A unidade é', uni)
dez = numeros // 10 % 10
print('A dezena é {}0'.format(dez))
cen = numeros // 100 % 10
print('A centena é {}00'.format(cen))
mil = numeros // 1000 % 10
print('O milhar é {}.000'.format(mil))
print('-'*27)

print()
print('Desafio 24')
#Verifique se começa com "Santo"
cidade = input('Qual cidade voce nasceu? ').strip()
#print(cidade.find('Santo '))
print('SANTO ' in cidade.upper())

print()
print('Desafio 25')
#Verifique se tem "Silva" no nome
print('SILVA' in nome.upper())

print()
print('Desafio 26')
#Verifique quantas vezes aparece a letra "A", onde aparece pela primeira vez, onde aparece por ultimo
print('A Quantidade de letras "A" são {}! '.format((nome.upper()).count('A')))
print('A primeira letra "A" aparece na posição {} '.format(nome.upper().find('A')))
print('A ultima letra "A" aparecena posição {} '.format(nome.upper().rfind('A')))


print()
print('Desafio 27')
#Leia um nome completo, mostre o primeiro nome e o ultimo
print(nome_s[1],nome_s[int(len(nome_s)-2)])
