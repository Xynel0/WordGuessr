def val_word(word):
    b = True
    for l in word:
        if l not in 'abcdefghijklmnopqrstuvwxyz':
            print(f'{l} encontrado em {word}.')
            b = False
    return b
        

def gera_lista(words):
    lista = []
    with open(words, "r", encoding="utf-8") as arq:
        for i in arq.readlines():
            lista.append(i.strip("\n"))
        if lista != []:
            for i in lista:
                b = val_word(i)
            if b == False:
                print('formatação do arquivo inválida. Modifique-o e tente novamente ou continue com o arquivo padrão.')
                return 0
            if b == True:
                return lista
        else:
            print("lista vazia!")
            return 0

def main_menu():
    print ("==============Bem Vindo ao WordGuessr==============")
    while True:
        print("1 - jogar\n2 - configurações\n0 - sair do jogo")
        opcao = input().strip()
        try:
            opcao = int(opcao)
            if opcao == 0:
                exit()
            elif opcao == 1:
                return 1
            elif opcao == 2:
                return 2
            else:
                print("opção selecionada indisponível")
        except ValueError:
            print("insira o número correspondente a uma das opções!")


def config():
    print("================== Configurações ==================")
    while True:
        escolha = input("insira o número relativo à respectiva configuração\n1 - remover palavras do arquivo atual\n2 - adicionar palavras ao arquivo atual\n3 - carregar seu próprio arquivo de palavras\n4 - resetar arquivo de palavras usado\n0 - voltar ao menu inicial\n").strip()
        try:
            escolha = int(escolha)
            if escolha >= 0 and escolha <= 4:
                return escolha
            else:
                print("opção inválida!")
        except ValueError:
            print("opção inválida! deve ser um número. tente novamente.")

def modo(palavra):
    x = len(palavra)
    while True:
        escolha = input("========= Escolha seu modo de jogo =========\n1 - zen\n2 - fácil\n3 - médio\n4 - difícil\n5 - impossível\n0 - voltar ao menu inicial\n").strip()
        try:
            escolha = int(escolha)
            if escolha == 0:
                return 0
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

def v_input(x, certos, errados, tamanho):
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
                if chute == '':
                    print("tente chutar uma letra!")
                elif len(chute) != tamanho and len(chute) > 1:
                    print("insira somente uma letra por vez ou chute uma palavra com o mesmo tamanho da correta!")
                elif len(chute) == 1 and chute not in "abcdefghijklmnopqrstuvwxyz":
                    print("as palavras aqui não levam acentos ou caracteres especiais, apenas letras do alfabeto!\ntente novamente")
                else:
                    return chute
 
def valid_path(msg):
    while True:
        x = input(msg)
        if x == '':
            print("o caminho não pode ser vazio!")
        elif x.endswith(".txt") == False:
            print("o arquivo deve estar no formato .txt")
        else:
            try:
                lista = gera_lista(x)
                if lista == 0:
                    return 0
                else:
                    return x
            except FileNotFoundError:
                print("arquivo não encontrado. insira outro caminho.")

def add_word(arq_path, sys_word):
    with open (arq_path, "a", encoding="utf-8") as arq:
        while True:
            if sys_word == '':
                word = input("insira a palavra desejada:\n").strip().lower()
            else:
                word = sys_word
            if word == '':
                print("a palavra não pode ser vazia.")
            else:
                b = val_word(word)
                if b == True and sys_word == '':
                    lista = gera_lista(arq_path)
                    if lista != 0:
                        if word in lista:
                            print("a palavra inserida já existe na lista.\ndeseja inserir outra?(s/n)")
                            b = False
                            while True:
                                ans = input().strip().lower()
                                if ans == 's':
                                    break
                                elif ans == 'n':
                                    return
                                else:
                                    print("por favor insira 's' ou 'n'")
                    else:
                        print("adicionando nova palavra...")
                if b == True:
                    arq.write(word+'\n')
                    if sys_word == '':
                        print('sucesso!')
                    break
def rem_word(arq_path):
    lista = gera_lista(arq_path)
    if lista == 0:
        return 0
    for i in range (len(lista)):
        print(i+1, lista[i])
    while True:
        try:
            n = int(input("insira o número correspondente à palavra a ser deletada:\n(ou insira '0' para limpar o arquivo)\n").strip())
            if n < 0 or n > len(lista):
                print("não há palavra com esse número na lista")
            else:
                with open (arq_path, "w", encoding="utf-8") as arq:
                    pass
                if n != 0:
                    for i in range(len(lista)):
                        if i != n-1:
                            add_word(arq_path, lista[i])
                print('sucesso!')
                break
        except ValueError:
            print('insira um inteiro.')
