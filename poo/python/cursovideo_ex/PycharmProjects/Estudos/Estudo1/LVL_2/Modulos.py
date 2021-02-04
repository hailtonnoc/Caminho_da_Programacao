print('_'*18)
print('Bem vindo a aula de modulos')
print('O video dos desafios a seguir é o https://www.youtube.com/watch?v=oOUyhGNib2Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=24')
print('='*18)
#import math             <-- importação do modulo
#from math import trunc  <-- importação somente da função

print('')
print('D 016')
#Crie um programa que leia um numero real e mostre sua porção interia.
import math
valor = float(input('Qual o numero vc deseja converter para real? '))
print('O valor real é {:.0f}'.format(math.trunc(valor)))
#Função Trunc = cortar o numero inteiro

print('')
print('D 017')
#Calcule e hipotenusa
cat_oposto = float(input('Qual a medida do cateto oposto? '))
cat_adjacente = float(input('Qual a medida do cateto adjacente? '))
hipo = math.hypot(cat_oposto,cat_adjacente)
print('_'*18)
print('O comprimento da hipotenusa é {:.3f}'.format(hipo))
#o quadrado da hipotenusa é igual a soma do quadrado dos catetos

print('')
print('D 018')
#Calcule ^seno, >cosseno, e tangente.
angulo = float(input('Qual o angulo desejaria saber o seno, cosseno e tangente? '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(' Seno {:.3f}\n Cosseno {:.3f}\n Tanjente {:.3f}\n'.format(seno, cosseno, tangente))

print('')
print('D 019')
#Sortiar o nome de 4 individuos
from random import choice
a1 = input('Qual o nome do primeiro aluno? ')
a2 = input('Qual o nome do segundo Aluno? ')
a3 = input('e o tercerio ? ')
a4 = input('Quarto? ')
lista = [a1, a2,a3 ,a4 ]
choicer = choice(lista)
print('O aluno escolhido é {}!'.format(choicer))

print('')
print('D 020')
#Sortiar e Ordenar os individuos
import random
random.shuffle(lista)
print(' a segunda lista é ')
print(lista)

print('')
print('D 021')
#Abrir e reproduzir um arquivo mp3
from pygame import mixer
mixer.init()
mixer.music.load('LBOY.mp3')
mixer.music.play()
input('Ta pegando fogo bicho!')

from time import sleep
print('acabou o programa!')
sleep(3)
print( 'TCHAHUHAUHAUHAUHAUH')