#link da aula https://www.youtube.com/watch?v=j9bYDjaAYzw

#Aula de Condições Aninhadas

# if == se        elif == se nao se       else= se nao

# and == e        or == ou

print('\033[36m  PROGRAMA DE APRENDIZADO !!!\033[m')
print()
nome = input('Qual seu nome? ')
if nome =='Hailton Oliveira':
    print('\033[7mOlá mestre {}'.format('!'*9))
elif nome.upper()=='ARTHUR' or nome.upper()=='IGOR' or nome.upper() == 'ALYNNE':
    print('Fala tiro liro')
elif nome.upper() in 'ANTONIO, VITOR, PRAPPAS, GABRIEL':
    print('E ai vagabunda!')
else:
    print('Olá {}, voce por favor encerre o programa, ate agora eu não aprendi hahahaha'.format(nome))
from time import sleep
sleep(4)
print()
print('Valeu {} vou ali roubar um urubu '.format(nome))