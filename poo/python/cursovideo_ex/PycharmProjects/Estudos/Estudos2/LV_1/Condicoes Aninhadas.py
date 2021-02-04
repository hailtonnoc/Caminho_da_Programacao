#ESTRUTURA CONDICIONAL

nome = str(input('Qual seu nome? '))
if  nome.upper() == 'HAILTON':       #!se!
    print( 'E ai monstro \033[31;1m{}!\033[m'.format(nome))
else:   #!se FALSO!
    print('Seu nome é um nome qualquer {}'.format(nome))
print ('Tenha uma boa tarde {}!'.format(nome))


#ESTRUTURA CONDICIONAL ANINHADA

nome = str(input('Qual seu nome? '))
if  nome.upper() == 'HAILTON':       #!se!
    print( 'E ai monstro \033[31;1m{}!\033[m'.format(nome))
elif nome.upper() == 'ALYNNE' or nome == 'Karen' or nome == 'Gisele': #!ou!se! entrada de novas condições
    print('Ola bibitchen {}'.format(nome))
elif nome.upper() in 'CASA ANTONIO BIEL JAPA':
    print('G-A-Y!')
else:
    print('nome de bosta em')
print ('Tenha uma boa tarde {}!'.format(nome))