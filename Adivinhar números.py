numero_fixo = 7

tentativas = 0

while tentativas < 3:

    escolha_do_jogador = int(input('Adivinhe o número que estou pensando: '))

    tentativas += 1

    if tentativas == 3 and escolha_do_jogador != 7:
        print('Infelizmente você errou, tentativas acabadas')
        break

    elif escolha_do_jogador != 7:
        print('Número errado, tente novamente\n')

    else:
        print('Parabéns! Você acertou o número.')
        break

        
