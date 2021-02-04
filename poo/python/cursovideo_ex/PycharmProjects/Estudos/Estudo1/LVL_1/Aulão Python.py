
print('Curso em video anotações')
print('Aula 4')
print('Conteudo;')
print('link: https://www.youtube.com/watch?v=31llNGKWDdo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=5' )

con_saudacao = 'Hello, world!'
print(con_saudacao)
print(6+3)
print('6'+'3')

DICA_1 = 'TODA MENSAGEM PRECISA ESTAR ENTRE ASPAS, SIMPLES OU DUPLAS.'
#No caso de aspas """  """ tripla serve para colar um texto completo no print
print(DICA_1)

DICA_2 = 'NEM TODA CONCATENAÇÃO FICA BOA UTILIZANDO O SIMBOLO "+" AS VEZES É MELHOR USAR ",".'
print(DICA_2)

DICA_3 = 'VARIAVEIS = OBJETOS (LEMBRAR DISSO).'
print(DICA_3)

nome = 'HAILTON'
idade = 25
peso = 81.99

print(nome,idade,peso)

DICA_4 = 'O CONCATENARDOR "+" FUNCIONA MELHOR COM STRING DE TIPO TEXTO'
print(DICA_4)

DICA_5 = 'COMO CRIAR UMA INTERATIVIDADE ENTRE VARIAVEIS E USUARIO?'
print(DICA_5)
DICA_F5 = 'Função "print = ESCREVA" e "input = LEIA"'
print(DICA_F5)

nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
peso = input('Qual seu peso? ')

print(nome,idade,peso)
print(" ")
print('Desafio 01')

print(nome,", Obrigado por aprender. Revise sempre que puder!"
)
print(" ")
print('Desafio 02')
dia = input('Qual dia do seu nascimento? ')
mes = input('Ok, de qual mês? ')
ano = input('Por fim, de qual ano? ')

print('Ok.', nome,'Nascido em ',dia,' de',mes,' do ano de',ano,'.')

print('Dica do video de correção https://www.youtube.com/watch?v=FNqdV5Zb_5Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=0s')
print('Dica de bloco de formatação "{}" sequido no final da string por'.format("{ B====D }"))

print('Obrigado por aprender {}!!!'.format(nome))

print(' ')

print('Alula 6')
print('link https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=9')
print(' ')

DICA_6 =\
    'TIPOS PRIMITIVOS' \
    'int; Inteiros ex: -3,-2,-1,0,1,2,3...' \
    'float; Numeros flutuantes(real) -0.123,0.123...' \
    'bool; True, False (Sempre colocar com a primeira letra maiuscula' \
    'str; Texto sempre entre aspas simples ou " "'  \
    'COMANDO "type(x)" retorna o tipo da variavel X'
print(DICA_6)

n_1 = int(input('Digite um numero '))
n_2 = float(input('Digite outro numero '))
SOMA = n_1 + n_2
print('A soma entre {} e {} equivale a {}!'.format(n_1, n_2, SOMA))
print(type(SOMA))

DICA_F6 = 'A FORMULA TESTE DE STRING "n.isnumeric(X) retorna o valor booleano se x é numerico ou não. Já a formula ".  '
print(DICA_F6)


print(' ')
print('Fim da aula 6')
print('Desafio 3 ')
print(' ')

print('{} , bem vindo a uma calculadora '.format(nome))
n_1 = float(input('Digite um numero '))
n_2 = float(input('Digite outro valor '))
SOMA = n_1 + n_2

# <---<< linha ignorada
# Fazer a soma de dois valores
print('Resultado do desafio 003')
print('{}, a resposta da soma entre {} e {} é igual a {}.'.format(nome, n_1, n_2, SOMA))
print('')

# Retornar todos os dados possiveis sobre os valores imputado
print('Resultado do desafio 004')
print('')
coisa = input('Digite uma coisa ')
print('O tipo do valor digitado {}.'.format(type(coisa)))
print('Algo foi digitado {}.'.format(bool(coisa)))
print('O valor digitado é um numero {}.'.format(coisa.isnumeric()))
print('O valor digitado é uma letra {}.'.format(coisa.isalpha()))
print('A variavel registrada é espaço {}.'.format((coisa.isspace())))
print('é alfanumerico?',coisa.isalnum())
print('Esta com uma letra maiuscula (capitalizado) ? ', coisa.istitle())
print('')

