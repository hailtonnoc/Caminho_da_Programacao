
print()
confiança = input('Qual sua espectativa?\n'
'x - Movimentação Extrema\n'
'a - Movimentação Exelente\n'
'b - Movimentação normal\n').upper()

print(''
      'OK...\n'
      '')



print('\033[34m      $       $')
print('     $       $$ ')
print('    $$       $  ')
print(' $   $$$  $     ')
print(' $$ $$$$$ $$  $ ')
print('$$$  $$$$$$$$ $$')
print('$$$$$$$$$$$$$$$$')
print('  $$$$$$$$$$$')
print('    $$$$$$$$ ')
print('                ')
print('   Calculador\033[m')
print()
operador = float(input('Qual o valor da Ação? R$ '))
quantidadeop = int(input('Quantos comprados? X '))
opert= float(operador*quantidadeop)
print()
print('\033[7mOk, vai brincar com     R${:.2f}\033[m'.format(opert))
print()
print('-'*18)
#Indicadores--------------------------------------
critical_D3 = float(.15)
forte_D2    = float(.09)
normal_D1   = float(.06)
miss_D2     = float(0.97)
hit_D3      = float(0.94)


if confiança == 'X':
    print('\033[32mUma espectativa de lucro R${:.2f} Em até 3 Dias '.format((opert * (critical_D3))))
    print('Venda R${:.2f}\033[m'.format(operador * (1+critical_D3)))
    print('\033[31mTire em R${:.2f}'.format((opert * forte_D2)))
    print('Vender em R${:.2f}\033[m'.format(operador * (1 + normal_D1)))
elif confiança == 'A':
    print('\033[32mA espectativa de lucro é R${:.2f}\033[m'.format((opert * forte_D2)))
    print('\033[32mVenda em R${:.2f}'.format((operador * (1+forte_D2))))
    print('\033[31mTire em R${:.2f}'.format((opert * normal_D1)))
    print('Vender em R${:.2f}\033[m'.format(operador * (1 + normal_D1)))
elif confiança == 'NENHUMA':
    print('JÁ PAROU PARA PENSAR QUE LOUCO ESSA VIDA? FUMA UM AE!\n'
          'Não Gela guerreiro o chamado é esse ai\n'
          'Então mostra pra esses cu com é que se faz\n'
          'SEJA IRREFREAVEL COMO UMA ONDA E FORTE COMO UMA PARTICULA\n'
          'E nunca, destrutivel como uma uma particula, ignorando toda a essencia e delicadeza da onda, sua foma existe e é alem do fisico. E sim no intangivel da informação bem apurada. Todas as camadas de abistração. Todos o niveis da existencia,\n'
          'permitase não limitar a realidade, explore e não se prenda ao ruim, não caçe o bom, pois ele é um passaro que so existe livre\n'
          'e livre é voce para aprender com todo os momentos\n'
          'O JOGO SEMPRE ACABA ZERADO\n'
          'Então voce já é o telespectador de sua vida\n'
          'E ainda pode dar palpite do que fazer\n'
          'voce devolvera atomo por atomo\n'
          'exitação do ETHER\n'
          'Volte a se comportar de maneira INTELIGENTE    ☺\n'
          'E se ficar com tedio que tal ir ao extremo com alguma promeça, chegar em alguma coisa ainda é chegar em alguma coisa')
elif confiança == 'B':
    print('\033[32mA espectativa de lucro é R${:.2f}\033[m'.format((opert * normal_D1)))
    print('\033[32mVenda em R${:.2f}'.format((operador * (1 + normal_D1))))
    print('\033[31mTire em R${:.2f}'.format((opert * miss_D2)))
    print('Vender em R${:.2f}\033[m'.format(operador * miss_D2))