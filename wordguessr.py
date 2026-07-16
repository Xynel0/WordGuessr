import random
import func

default_path = 'words.txt'
current_path = default_path
while True:
    main_menu_return = func.main_menu()
    if main_menu_return == 1:
        lista = func.gera_lista(current_path)
        if lista != 0:
            while True:
                palavra = random.choice(lista)
                chances = func.modo(palavra)
                if chances == -1:
                    c = True
                else:
                    c = False
                chutes_certos = []
                chutes_errados = []
                if chances == 0:
                    break
                elif chances > 25:
                    chances = 25
                while chances > 0 or c:
                    if c:
                        print_chances = 'infinitas'
                    else:
                        print_chances = chances
                    if len(chutes_errados) >= 1:
                        print()
                        print('Chutes errados:')
                        for chute in chutes_errados:
                            print(chute, end = ' ')
                        print()
                    for i in palavra:
                        if i in chutes_certos:
                            print(i, end=' ')
                        else:
                            print("_", end=' ')
                    print('')
                    b = True
                    for i in palavra:
                        if i not in chutes_certos and palavra not in chutes_certos:
                            b = False
                    if b == True:
                        if tentativas > 1:
                            print(f"A palavra era {palavra}! Você ganhou!\nSó teve que tentar {tentativas} vezes! Parabéns!!")
                        elif tentativas == 1:
                            print(f"A palavra era {palavra}! Você ganhou!\nSó teve que tentar uma vez! Parabéns!!")
                        break
                    letra = func.v_input(f"Insira uma letra(você tem {print_chances} chances):\n", chutes_certos, chutes_errados, len(palavra))
                    if letra in palavra or letra == palavra:
                        chutes_certos.append(letra)
                    else:
                        if letra == palavra:
                            b = True
                        else:
                            chutes_errados.append(letra)
                            chances -= 1
                    tentativas = len(chutes_certos) + len(chutes_errados)
                if b == False:
                    print(f"você perdeu!\na palavra era {palavra}.")
        else:
            continue
    elif main_menu_return == 2:
        config_return = func.config()
        if config_return == 0:
            continue
        elif config_return == 1:
            func.rem_word(current_path)
        elif config_return == 2:
            func.add_word(current_path, '')
        elif config_return == 3:
            msg = "insira o caminho do arquivo:\n"
            current_path = func.valid_path(msg)
            if current_path == 0:
                current_path = default_path
        elif config_return == 4:
            with open("words.txt", "w", encoding="utf-8") as arq:
                pass
            with open("words.txt", "a", encoding="utf-8") as arq:
                for i in ['abacate', 'abacaxi', 'abelha', 'acerola', 'agulha', 'alface', 'alho', 'amizade', 'ancora', 'anel', 'aranha', 'baleia', 'balao', 'banco', 'barco', 'barraca', 'batata', 'beijo', 'berco', 'biscoito', 'boneca', 'botao', 'brinco', 'bruxa', 'cabana', 'cabide', 'caixote', 'calca', 'caneca', 'canoa', 'canudo', 'capivara', 'castelo', 'cebola', 'cenoura', 'cereja', 'chafariz', 'chaveiro', 'chinelo', 'chocalho', 'chuchu', 'cegonha', 'coelho', 'cogumelo', 'colcha', 'colmeia', 'coqueiro', 'coruja', 'cortina', 'gaveta', 'girafa', 'girassol', 'goiaba', 'golfinho', 'gorila', 'grade', 'gravata', 'grelha', 'grilo', 'gruta', 'guaxinim', 'harpa', 'hiena', 'hipopotamo', 'horta', 'helice', 'igreja', 'iogurte', 'jacare', 'jali', 'jarra', 'jasmim', 'javali', 'joaninha', 'jornal', 'judo', 'jumento', 'juriti', 'lagarta', 'lagosta', 'lanche', 'lanterna', 'leao', 'leopardo', 'lesma', 'lagartixa', 'limao', 'lince', 'lixeira', 'lousa', 'lobo', 'lontra', 'lula', 'macaco', 'madeira', 'mastro', 'medalha', 'mochila', 'moinho', 'morcego']:
                    arq.write(i+'\n')
            current_path = default_path
            print("sucesso!")
    else:
        print("opção inválida. insira um dos números abaixo.")
