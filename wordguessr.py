import random
import func

lista = func.gera_lista()
while True:
    palavra = random.choice(lista)
    chances = func.modo(palavra)
    if chances == -1:
        c = True
    else:
        c = False
    chutes_certos = []
    chutes_errados = []
    while chances > 0 or c:
        if c:
            print_chances = 'infinitas'
        else:
            print_chances = chances
        for i in palavra:
            if i in chutes_certos:
                print(i, end=' ')
            else:
                print("_", end=' ')
        print('')
        b = True
        for i in palavra:
            if i not in chutes_certos:
                b = False
        if b == True:
            print(f"a palavra era {palavra}! você ganhou!\nsó teve que tentar {tentativas} vezes! parabens!!")
            break
        letra = func.v_input(f"insira uma letra(você tem {print_chances} chance(s)):\n", chutes_certos, chutes_errados)
        if letra in palavra:
            chutes_certos.append(letra)
        else:
            chutes_errados.append(letra)
            chances -= 1
        tentativas = len(chutes_certos) + len(chutes_errados)
    if b == False:
        print("você perdeu!")
