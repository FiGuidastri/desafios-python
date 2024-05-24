from random import randint

N = 0
PONTOS_AI1 = 0
PONTOS_AI2 = 0

while N < 5:
    numero_escolhido_1 = randint(1, 10)
    numero_escolhido_2 = randint(1, 10)

    print(f'Número escolhido pela IA 1: {numero_escolhido_1}')
    print(f'Número escolhido pela IA 2: {numero_escolhido_2}')

    if numero_escolhido_1 == numero_escolhido_2:
        print("Empate!")
    elif numero_escolhido_1 > numero_escolhido_2:
        print("Ponto para IA 1!")
        PONTOS_AI1 += 1
    else:
        print("Ponto para IA 2!")
        PONTOS_AI2 += 1
    
    print(f'Placar: AI 1 - {PONTOS_AI1} x AI 2 - {PONTOS_AI2}')
    N += 1

ganhador = ''
if PONTOS_AI1 > PONTOS_AI2:
    ganhador = 'VITÓRIA DA AI 1!!!'
elif PONTOS_AI1 < PONTOS_AI2:
    ganhador = 'VITÓRIA DA AI 2!!!'
else:
    ganhador = 'EMPATE!'

print(f'Placar final: {PONTOS_AI1} X {PONTOS_AI2}.')
print(ganhador)
