print('Aula 09')
print('Manipulando Texto https://www.youtube.com/watch?v=a7DH88vk2Sk')

#Fatiamento
#inicia no "0"
#No python toda variavel é um objeto, logo toda frase é uma lista de letras
frase = str(input('Qual frase deseja analizar? '))

print()
print()

print(frase[3])
#é um corte unico
print(frase[0:6])
#é o equivalente a print(frase[:5]
print(frase[:3:1])
#Quando temo uma area sem numero = 0 no terceiro caractere temos um marcador onde sera pulado a quantidade informada
print(frase[:6:3])
#No caso iniciando do terceiro caracter vai até o final pulando a quantidade informada no ultimo caracter

print(' ')
print('---'*6)
print(' ')
#função len mostra a quantidade de caracteres em uma premissa

#conta a quantidade de caracteres em uma frase
print('A quantidade de caracteres digitadas foi {}'.format(len(frase)))

#função count
#conta o apareceimento de uma premisa
print('A quantidade de "o" digitados é {}'.format(frase.count('o')))
#para contar "count" com o fatiamento é possivel, basta adicionar medida dos cortes x.count('o',0,9)
print('A quantidade de "o" do primeiro ao nono caractere é igual a {} !'.format(frase.count('o',0,9)))
#para localizar algum item no texto digitado basta usar o .find('isso')
print()
busca = str(input('O que gostaria de procurar? '))
print(frase.find(busca))

#verificar se existe no campo função "in"
print(busca in frase)

print()
print()
print('_'*18)

print('TRANSFORMAÇÃO')
print('_'*18)
print()
#Função "replace" substitui uma terminada parte de string por outra
print(frase.replace('ovo','cu'))
print()
#Função "upper" deixa o que não esta em maiusculo maiusculo
print(frase.upper())
#Função "lower" deixa o que estava maiusculo em minusculo
print(frase.lower())
#Função "capitalize" deixa tudo em minusculo exceto a primeira letra da sentença
print(frase.capitalize())
#Função "title" transforma a primeira letra de todas palavras em maiusculo
print(frase.title())
#Função "strip" remove os espaços do inicio e do final das sentenças
#Porem mantem as do meio \\ caso coloque o "r" (Right) antes de strip elinima somente os espaços a Direita

print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print()
print('-'*18)
print('DIVISÃO')
print('_'*18)
print()

#Função "split" divide toda a string em varias listas, atraves do espaço (por principio)
frase.split()
#Função "join" junta os elementos o '-' é somente o espaçador
print('-'.join(frase))
print()
print()

print('-=-'*18)
a = int(input('Qual o primeiro valor? '))
b = int(input('Qual o primeiro valor? '))
c = int(input('Qual o primeiro valor? '))
#VERIFICADOR DE MAIOR
if a>b and a>c:
    maior = a
if  b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
#VERIFICADOR DE MENOR
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

