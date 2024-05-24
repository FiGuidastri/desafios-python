from random import randint

N = 0
pontos_pc = 0
pontos_usuario = 0
usuario = input('Digite seu nome de jogador: ').capitalize()

while N < 5:
    numero_escolhido_pc = randint(1, 10)
    numero_escolhido_usuario = int(input('Escolha um número de 1 a 10: '))

    print(f'Número escolhido pelo PC: {numero_escolhido_pc}')
    print(f'Número escolhido pelo jogador: {numero_escolhido_usuario}')

    if numero_escolhido_pc == numero_escolhido_usuario:
        print("Empate!")
    elif numero_escolhido_pc > numero_escolhido_usuario:
        print("Ponto para o PC!")
        pontos_pc += 1
    else:
        print(f"Ponto para {usuario}!")
        pontos_usuario += 1
    
    print(f'Placar: PC - {pontos_pc} x {usuario} - {pontos_usuario}')
    N += 1

ganhador = ''
if pontos_pc > pontos_usuario:
    ganhador = 'VITÓRIA DO PC!!!'
elif pontos_pc < pontos_usuario:
    ganhador = f'VITÓRIA DO {usuario.upper()}!!!'
else:
    ganhador = 'EMPATE!'

print(f'Placar final: {pontos_pc} X {pontos_usuario}.')
print(ganhador)
