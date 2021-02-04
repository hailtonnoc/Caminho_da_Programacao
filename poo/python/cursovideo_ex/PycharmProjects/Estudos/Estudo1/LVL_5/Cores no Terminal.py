#Codigo "ANSI"
#STYLE
# 0 NONE (NADA)
# 1 BOLD (NEGRITO)
# 4 UNDERLINE (SUBLINHADO)
# 7 NEGATIVE (TOMAR NO CU)

#TEXT               BACK
#30   BRANCO         40
#31   VERMELHO       41
#32   VERDE          42
#33   AMARELO        43
#34   AZUL           44
#35   ROXO           45
#36   CIANO          46
#37   CINZA          47



#inicio  style  text  back   fim
#  \ 033 [   0  ; 33 ; 44     m

print('\033[32mE ai Brother _\|/_\033[m')

print('\033[7;31mOLA BROTHER\033[m')

print('\033[30mOla \033[7mMundo!\033[m')

#crie uma biblioteca de cores
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}

nome = 'Hailton Oliveira'

print('Ola {}{}{}!'.format(cores['pretobranco'], nome , cores['limpa']))