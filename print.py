print('         *Banco Visa Mais* \n')
print('Bem Vindo ao melhor Banco do Mundo \n')
saldo=1000
while True:
    print('O que podemos fazer por você hoje?')
    print('         #MENU#')
    print('1 - Ver saldo na conta')
    print('2 - Sacar dinheiro ')
    print('3 - Depositar dinheiro')
    opcoes=int(input('Digite a opção desejada \n'))
    while opcoes != 1 and opcoes != 2 and opcoes != 3 and opcoes != 4:
         print('Opção inexistente!')
         opcoes=int(input('Digite novamente\n'))
    if opcoes == 1:
         print('{} Reais'. format (saldo))
    if opcoes == 2:
         sacar=float(input('Quanto você quer sacar? \n'))
         while sacar > saldo:
             print('ERRO, SALDO INSUFICIENTE')
             sacar=float(input('Digite um valor de saque válido\n'))
         if sacar <= saldo:
             saldo=saldo-sacar
             print('Seu valor bancario agora é de {} Reais'. format(saldo))
    if opcoes == 3:
         depositar=float(input('Quanto você quer depositar?\n'))
         saldo= saldo + depositar
         print('Agora você tem um saldo de {} Reais'. format(saldo))
    voltar=int(input('Se deseja voltar ao menu, digite 9, se desejar sair digite qualquer outro número\n'))
    if voltar == 9:
         print('Voltando ao menu ...')
    else:
         break











