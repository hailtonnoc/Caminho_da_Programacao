print('_\|/_'*9)
print('CONDICIONAIS')
print('_'*9)

# 'if' equivale ao SE do Excel

kg = int(input('Quantos kilos a garota tem ? '))
if kg <= 60:
#SE sim +
    print('Eca, vai fazer uns agachamentos filha!!!')
else:
#se não -
    print('E ai safada, vamo fechar? ')
print('--- FIM---')

print()
print('CONDIÇÃO SIMPLIFICADA')
#Uma especie de operador "ternario" ou "if" simplicado

tall = int(input('Qual a altura da guria em cm? '))
print('Mama em pé'if tall<=155 else 'mama de joelhos ')