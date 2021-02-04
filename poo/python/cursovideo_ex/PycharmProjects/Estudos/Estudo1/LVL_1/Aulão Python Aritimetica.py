print('Aula 07')
print('Operações aritimeticas')
print('Link https://www.youtube.com/watch?v=Vw6gLypRKmY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=12 ')
print('')

print('Operadores aritimeticos')
n1 = float(input('Digite um numero para logar os exemplos '))
n2 = float(input('Digite outro valor '))

print('Soma =          +')
print(n1 + n2)
print('')

print('Subtração =     -')
print(n1 - n2)
print('')

print('Multiplicação = *')
print(n1 * n2)
print('')

print('Divisão =       /')
print(n1 / n2)
print('')

print('Div. inteira = //')
print(n1 // n2)
print('')

print('Div. resto =    %')
print(n1 % n2)
print('')

print('Potencia =     **')
print('Ainda pode ser usado como operador "pow(x,y)"')
print(n1 ** n2)
pow(n1,n2)
print('')

#Formato correto é **(1/x) onde o "X" recebe a raiz
print('raizQuadrada =          **(1/2)')
print('raizCubica =            **(1/3)')

print(n1 **(1/2) )
print(n1 **(1/3) )

print('')

print('Ordem de precedencia ')
print('1º ()')
print('2º ** potencias')
print('3°  *  /  //  % ')
print('4 + ou -')
print('')

'\n'
'\n'

print('Desafio 005')
#Um programa que mostre que numero vem antes e qual vem depois
print('o numero que vem antes do primeiro numero digitado é {} \n e o seu sucessor é {}.'.format(int(n1 - 1), int(n1 + 1)))
'\n'
print('Desafio 006')
#Um programa que mostra o dobro o triplo e a raiz quadrada
print('o dobro de é {} o triplo {} e a raiz quadrada é {}.'.format(int(n1 * 2), int(n1 * 3), (n1 **(1/2))))
'\n'
print('Desafio 007')
#calcular a media dos numeros digitado (notas de um aluno)
resultado007 = ((n1 + n2)/2)
print('a media dos valores digitados é {}'.format(resultado007))
'\n'
print('Desafio 008')
#converter metros em centimetro e milimetros
centimetros = (n1 * 100)
milimetros = (n1 * 1000)
print('O Valor em \ncentimetro é {} \nmilimetros {}'.format(centimetros, milimetros))
'\n'
print('Desafio 009')
#criar uma tabuada com o numero digitado
print('A tabuada sera do numero {}'.format(n1))
'\n'
print('{} x  1 = {}'.format(n1, (n1 * 1)))
print('{} x  2 = {}'.format(n1, (n1 * 2)))
print('{} x  3 = {}'.format(n1, (n1 * 3)))
print('{} x  4 = {}'.format(n1, (n1 * 4)))
print('{} x  5 = {}'.format(n1, (n1 * 5)))
print('{} x  6 = {}'.format(n1, (n1 * 6)))
print('{} x  7 = {}'.format(n1, (n1 * 7)))
print('{} x  8 = {}'.format(n1, (n1 * 8)))
print('{} x  9 = {}'.format(n1, (n1 * 9)))
print('{} x 10 = {}'.format(n1, (n1 * 10)))

print('')
print('Desafio 010')
#converter reais em dolar
#cotação sujerida 3,27
cotacao = float(3.27)
print('o seu saldo em dolar pela cotação de 2017 é de US$ {:.2f}'.format(n1 / cotacao))

print('')
print('Desafio 011')
#Calcular a area quadrada de uma largura e altura e retornar a area em seguida a guantidade de latas de tinda que cobriria
#Cala lata de tinta cobre 2m²
area = n1 * n2
ltinta = 2
print('Para pintar uma parede de {}m² precisa de {} litros'.format(area, (area / ltinta) ))

print('')
print('Desafio 012')
#Criar um programa que da desconto de 5%
print('Um produto de R$ {} recebe um desconto de R$ {} e devera pagar R$ {}.'.format(n1, (n1 * 0.05), (n1 - (n1 * 0.05)) ))

print('')
print('Desafio 013')
#Criar um programa que da um aumento de 15%
print('Um produto de R$ {:.2} recebe um aumento de R$ {:.2f} e devera pagar R$ {:.2f}.'.format(n1, (n1 * 0.15), (n1 + (n1 * 0.15)) ))

print('')
print('Desafio 014')
#Converter celsius em fahrenheit
c = float(input('Informe a temperatura °C: '))
fahrenheit = 33.8
print('A temperatura em fahrenheit é {:.3f}°F.'.format((c*(9/5))+32))

print('')
print('Desafio 015')
#Com base no KM rodado e quantidade de dias.
day = 60
km = 0.15

ikm = float(input('Quantos km foi rodado? '))
iday = int(input('Quantos dias ficou com o carro? '))
print('')
print('_'*9)
print('Extrato')
print('_'*9)
print('dia         R${:.2f}'.format(iday*day))
print('km rodado   R${:.2f}'.format(ikm*km))
print('')
print('TOTAL A PAGAR R${:.2f}'.format((iday*day)+(ikm*km)))