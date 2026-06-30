def gera_lista():
    lista = []
    with open("words.txt", "r", encoding="utf-8") as arq:
        for i in arq.readlines():
            lista.append(i[0:len(i)-1])
    return lista


def modo(palavra):
    x = len(palavra)
    while True:
        escolha = input("Escolha seu modo de jogo:\n1 - zen\n2 - fácil\n3 - médio\n4 - difícil\n5 - impossível\n0 - sair do jogo\n").strip()
        try:
            escolha = int(escolha)
            if escolha == 0:
                exit()
            elif escolha == 1:
                return -1
            elif escolha == 2:
                return 2*x
            elif escolha == 3:
                return x
            elif escolha == 4:
                return x//3
            elif escolha == 5:
                return 1
            else:
                print("opção inválida!")

        except ValueError:
            print("opção inválida! deve ser um número. tente novamente.")

def v_input(x, certos, errados):
    while True:
        chute = input(x).strip().lower()
        if chute in certos:
            print("letra já descoberta!")
        elif chute in errados:
            print("já vimos que isso não funciona!")
        else:
            try:
                chute = int(chute)
                print("tente chutar uma letra!")
            except ValueError:
                if len(chute) > 1:
                    print("chute uma letra por vez!")
                elif chute == '':
                    print("tente chutar uma letra!")
                elif chute not in "abcdefghijklmnopqrstuvwxyz":
                    print("as palavras aqui não levam acentos ou caracteres especiais, apenas letras do alfabeto!\ntente novamente")
                else:
                    return chute