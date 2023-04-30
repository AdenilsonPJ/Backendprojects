import random
import os

print('Seja bem vindo ao jogo!')
palavras=['computador','cachorro','rabanete','graviola','chipre','cotonete','tubarão']
palavra=random.choice(palavras)

tentativas=0
chances=4
letras_escolhidas=[]
estado_atual=['_']*len(palavra)
print(estado_atual,f'{os.linesep}Você poderá errar 5 vezes{os.linesep}')

while tentativas<chances:  # and '|'.join(estado_atual) !=palavra:
    letra=input('\n Escolha uma letra:')
    while letra in letras_escolhidas:
        print('Você já escolheu esta letra!')
        print(estado_atual)
        print(tentativas)
        print(chances-tentativas)
        letra = input('\n Escolha uma letra:')
    letras_escolhidas.append(letra)
    for i in range(len(palavra)):
        if letra == palavra[i]:
            estado_atual[i]=letra
    if letra in palavra:
        print('Muito bem!')
        print(estado_atual)
        print(tentativas)
        print(chances-tentativas)
    else:
        print('Que pena! Escolha outra letra:')
        print(estado_atual)
        print(tentativas)
        print(chances-tentativas)

        tentativas=tentativas+1 # o mesmo que: tentativas+=1

# tentativas restantes
    for item in letras_escolhidas:
       print(item, end=' ')

if tentativas==chances:
    print('Que pena! Você foi enforcado.')
    print('A palavra era',palavra)
else:print('Parabéns! Você escapou da forca.')