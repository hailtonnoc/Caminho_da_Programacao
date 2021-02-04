print ('_'*18)
print ('Desafio 028')
# Programa que gera um numero entre 0 e 5 peça para o usuario tentar adinivar. Escreva se ganhou ou perdeu.
# from random import randint
#escolha = randint (0,5) escolher entre 0 e 5
lista = [0,1,2,3,4,5]
from random import choice
choicer = int(choice(lista))
splayer = int(input('Escolha um numero de 0 a 5 '))
if splayer == choicer:
    print('Ganhou')
else:
    print('Perdeu')
print('Fim de jogo, o numero era {}'.format(choicer))

print ('_'*18)
print()


print('_'*18)
print('Desafio 029')
# Leia a velocidade de um carro ao passar no pedagio. Se ele ultrapassar 80km/h monstre que ele foi multado. e cobre R$ 7,00 por cada km acima do limite.
km_radar = int(input('Em qual velocidade (kmph) voce passou no radar? '))
from time import sleep
if km_radar >= 81:
    print('voce foi multado! ')
    print('Calculando multa...')
    sleep(3)
    multa = ((km_radar-80)*7)
    print('O valor da multa foi R${} '.format(multa))
else:
    print('Voce não foi multado, continue dirigindo com segurança. Obrigado!')
print(' Rodovia NOC ')


print()


print('_'*18)
print('Desafio 030')
# Leia um numero inteiro e mostre se ele é PAR ou IMPAR.
N = int(input('Digite um numero '))
if (N % 2) > 0:
    print('impar')
else:
    print('Par')


print()


print('_'*18)
print('Desafio 031')
# Pergunte a distancia em km, calcule o preço da passagem R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
# Operador ternario '''preço = dkm * 0.50 if dkm <=200 else dkm * 0.50
dkm = int(input('Quantos Km gostaria de viajar em nossa companhia? '))
if  dkm >= 201:
    print('O valor da passagem ficara R${:.2f} .'.format(dkm * 0.45))
else:
    print('O valor da passagem ficou R${:.2f} .'.format(dkm * 0.50))
print('OBRIGADO POR ESCOLHER A AVIACÃO NOC ☺')

print()


print('_'*18)
print('Desafio 032')
# Leia um ano e mostre se é BISSEXTO.
from datetime import date
ano = int(input('Qual ano gostaria de saber se é bissexto? se deseja saber do presente digite "0"'))
if ano == 0:
    ano =  date.today().year
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('o ano não é um bissexto')


print()


print('_' * 18)
print('Desafio 033')
# Leia três numeros e mostre qual dele é o maior e qual o menor
n1 = int(input('Qual o primeiro numero? '))
n2 = int(input('Qual o segundo numero? '))
n3 = int(input('Qual o terceiro numero? '))
if n1 > n2:
    mai = n1
    min = n2
else:
    mai = n2
    min = n1
#
if min > n3:
    med = min
    min = n3
else:
    med = n3
#
if med > mai:
    maiF = med
    med = mai
else:
    maiF = mai

print()

print('o maior numero é {}'.format(maiF))
print('o numero medio {}'.format(med))
print('o numero minimo é {}'.format(min))

print()


print('_'*18)
print('Desafio 034')
# Leia um salario de funcionario e calcule o aumento. Para salarios superiores a R$ 1.250,00 calcule um aumento de 10% e o aumento de 15% para inferiores.
sal = float(input('Qual salario do funcionario R$? '))
if  sal >= 1250:
    print('O salario atualizado do funcionario sera de R${:.2f} '.format(sal*1.10))
else:
    print('O salario atualizado do funcionario sera de R${:.2f} '.format(sal*1.15))


print()


print('_'*18)
print('Desefio 035')
# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.

t1 = float(input('Qual a primeira medida? '))
t2 = float(input('Qual a segunda medida? '))
t3 = float(input('Qual a terceira medida? '))
#maior e menor
if t1 > t2:
    tmai = t1
    tmin = t2
else:
    tmai = t2
    tmin = t1

#medio
if tmin > t3:
    tmed = tmin
    tmin = t3
else:
    tmed = t3

#prova do maior
if tmed > tmai :
    tmaiF = tmed
    tmed = tmai
else:
    tmaiF = tmai


print()

if tmaiF >= (tmed+tmin):
    print('Triangulo impossivel')
else:
    print('Triangulo possivel')

print(tmaiF)
print(tmed)
print(tmin)
