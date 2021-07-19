#Programa permite que o usúario jogue par ou impar com o computador, o jogo sera interrompido quando o jogador perder mostrando assim a contidade de vitorias consecutivas;

from random import randint

print('=-' * 20,'VAMOS JOGAR PAR OU ÍMPAR','=-' * 20)

vitoria = 0
#valor dos jogadores
while True:
    while True:
        jogador = int(input('\nDigite um valor: '))
        if jogador not in range (0,11) :
            print('Número invalido')
        else:
            break
    computador = randint(0, 10)
    total = jogador + computador
    
    escolha = ' '
    
    #escolha par ou impar
    while escolha not in 'PI':
        escolha = str(input('Você escolhe Par ou Ímpar: [P,I]')).strip()[0].upper()    
    
    print ('Você jogou',jogador,'e o Computador jogou',computador,'. Resultado',total, end=' ')
    print ('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    
    #criterio de vitoria e marcação de ponto
    if escolha == 'P':
        if total % 2 == 0:
            print('você venceu!!')
            vitoria += 1
        else: 
            print('Você perdeu!!')
            break
    
    elif escolha == 'I':
        if total % 2 == 1:
            print('você venceu!!')
            vitoria += 1
        else:
            print('Você perdeu!!')
            break
        
    print('Vamos jogar novamente...')
print('\033[031mGame Over!\033[m \nVocê venceu', vitoria, 'x')