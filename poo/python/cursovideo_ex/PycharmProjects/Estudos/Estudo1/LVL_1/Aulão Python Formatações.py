# Aula de formatação

# enquadramento = todo texto de constar dentro dos simbolos '
# concatenar = pode ser usado com , ou +
# Multiplicacao = pode ser usado o simbolo *
print('Bem v{}ndo!'.format('i'*9))
print('_\|/_ '*12)

print('OI '+ 'GRACINHA')

nome = input('Qual seu nome? ')
print('Bem vindo a aula de formatações {:_^18}!'.format(nome))
#para colar os print usa-se "end=' '"
#para quebrar a linha usa-se "\n"
'\n'
print('E assim funciona uma \n quebra de linha {:.>18}'.format(nome))
'\n'
n1 = int(input('Digite um valor '))
n2 = int(input('Digite outr valor '))
divisao = n1 / n2
print('a resposta da divisão dos dois numeros esta limitado {:.2f} '.format(divisao), end=' ☺')
#{:} item
#{: . } o que vem depois do .format
#{:. ^} em qual alinhamento
#{:.^ x} em quantos caracteres

#{:.x f} quantos numeros flutuantes ou depois do ponto

print(' ')
print(' ')
