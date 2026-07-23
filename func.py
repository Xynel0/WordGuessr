
#menu principal. retorna o número referente à opção escolhida ou encerra o programa
def main_menu():
    print ("============== Bem Vindo ao WordGuessr! ==============")
    while True:
        print("1 - Jogar\n2 - Configurações\n0 - Sair do jogo") #exibe as opções
        opcao = input().strip()
        try:
            opcao = int(opcao) #
            if opcao == 0:     #
                exit()         #
            elif opcao == 1:   # opções aceitas
                return 1       #
            elif opcao == 2:   #
                return 2       #
            else:
                print("Opção selecionada indisponível")               #
        except ValueError:                                            # casos de erro
            print("Insira o número correspondente a uma das opções!") #


#valida palavras para uso no jogo. recebe a palavra e retorna True para palavra válida e False para palavra inválida
def val_word(word):
    b = True
    for l in word:                                  # percorre cada posição na palavra
        if l not in 'abcdefghijklmnopqrstuvwxyz':   # verifica se é uma letra
            print(f'{l} encontrado em {word}.')     # imprime o caractere encontrado em caso de caractere não aceito
            b = False
    return b


# gerador de listas. recebe o caminho atual e retorna uma lista com as palavras do arquivo
def gera_lista(words):
    lista = []      # inicia lista vazia que será retornada
    try:
        with open(words, "r", encoding="utf-8") as arq:   # abre o arquivo no caminho recebido
            for i in arq.readlines():                     # percorre a lista de linhas
                lista.append(i.strip("\n"))               # filtra \n e adiciona na lista a ser retornada

    except FileNotFoundError:    # lida com o caso de arquivo não encontrado
        print("O arquivo não foi encontrado. Veja se o mesmo se localiza no diretório de trabalho atual.")
        return 0
    
    # valida a lista gerada
    if lista != []: # caso de lista não vazia
        for i in lista:         # percorre a lista
            b = val_word(i)     #chama a validação para cada palavra
        if b == False:          # se o arquivo não estiver de acordo com as exigências, retorna 0 e exibe a mensagem abaixo
            print('Formatação do arquivo inválida. Modifique-o e tente novamente ou continue com o arquivo padrão.')
            return 0
        if b == True:
            return lista # se a lista atender aos requisitos, é retornada
    else: #caso de lista vazia
        print("Lista vazia!")
        return 0


# define e retorna a quantidade de chances, -1 no modo zen, ou 0 para retornar ao menu inicial. recebe a palavra escolhida para a rodada
def dificuldade(palavra):
    x = len(palavra) #quantidade de letras da palavra

    #pede o modo de jogo
    while True:
        escolha = input("========= Escolha seu modo de jogo =========\n1 - Zen\n2 - Fácil\n3 - Médio\n4 - Difícil\n5 - Impossível\n0 - Voltar ao menu inicial\n").strip()
        try:
            escolha = int(escolha) #
            if escolha == 0:       #
                return 0           #
            elif escolha == 1:     #
                return -1          #
            elif escolha == 2:     #
                return 2*x         #  calcula a quantidade de chances a depender do modo e da palavra
            elif escolha == 3:     #
                return x           #
            elif escolha == 4:     #
                return x//3        #
            elif escolha == 5:     #
                return 1           #
            else:
                print("Opção inválida!")
        except ValueError:
            print("Opção inválida! Deve ser um número. Tente novamente.")


# valida os palpites
def v_input(chances, certos, errados, tamanho): # recebe chances restantes, a lista com os chutes certos, a lista com os chutes errados, e o tamanho da palavra correta
    while True:
        try:
            if chances > 1:                                                                       #
                chute = input(f"Insira uma letra(você tem {chances} chances):\n").strip().lower() # imprime a mensagem correta a depender da quantidade de chances restantes e recebe
            else:                                                                                 # o imput quantas vezes forem precisas
                chute = input(f"Insira uma letra(você tem {chances} chance):\n").strip().lower()  #
        except TypeError:                                                                         #
            chute = input(f"Insira uma letra(você tem {chances} chances):\n").strip().lower()     #

        if chute in certos:                                 #
            print("Letra já descoberta!")                   # valida se a letra (ou palavra) já foi chutada
        elif chute in errados:                              #
            print("Já vimos que isso não funciona!")        #

        else:

            try:                                 #
                chute = float(chute)             # testa se o input foi um número
                print("Tente chutar uma letra!") #

            # valida os casos de...
            except ValueError:
                if chute == '': # chute vazio
                    print("Tente chutar uma letra!")

                elif len(chute) == 1: # chute de tamanho 1 com...
                    if chute not in "abcdefghijklmnopqrstuvwxyz": # letra fora do alfabeto do jogo
                        print("As palavras aqui não levam acentos ou caracteres especiais, apenas letras do alfabeto!\nTente novamente.")
                    else:
                        return chute
                    
                else: # chute de tamanho maior que 1 com...
                    if len(chute) != tamanho: # tamanho diferente do tamanho correto
                        print("Insira somente uma letra por vez ou chute uma palavra com o mesmo tamanho da correta!")

                    else: # tamanho correto mas com...
                        letras_validas = True
                        for letra in chute:
                            if letra not in "abcdefghijklmnopqrstuvwxyz": # algum caractere fora do alfabeto do jogo
                                letras_validas = False
                                break
                            
                        if letras_validas == False:
                            print("As palavras aqui não levam acentos ou caracteres especiais, apenas letras do alfabeto!\nTente novamente")
                        else:
                            return chute


# imprime o menu, recebe e valida o input
def config():
    print("================== Configurações ==================")
    while True:
        escolha = input("Insira o número relativo à respectiva configuração\n1 - Remover palavras do arquivo atual\n2 - Adicionar palavras ao arquivo atual\n3 - Carregar seu próprio arquivo de palavras\n4 - Resetar arquivo de palavras usado\n0 - Voltar ao menu inicial\n").strip()

        #validação do input
        try:
            escolha = int(escolha)
            if escolha >= 0 and escolha <= 4: #valores de acordo com as opçoẽs. em caso de adição de novas configurações, modificar os valores presentes.
                return escolha
            else:
                print("Opção inválida!")
        except ValueError:
            print("Opção inválida! Deve ser um número. Tente novamente.")


# adiciona palavras à lista. recebe o caminho do arquivo atualmente em uso e uma palavra do sistema em caso de recuperação do arquivo original (se o usuário estiver apenas adicionando uma palavra, sys_word é vazia)
def add_word(arq_path, sys_word): 
    with open (arq_path, "a", encoding="utf-8") as arq:

        # usuário deseja adicionar palavra -> sys_word = ''
        if sys_word == '':
            while True:

                word = input("Insira a palavra desejada:\n").strip().lower() # recebe a palavra
                if word == '':
                    print("A palavra não pode ser vazia.") # palavra inserida não pode ser vazia. (só cai nesse caso se sys_word for vazia E o input for vazio)

                else:
                    b = val_word(word) # valida a palavra de acordo com o alfabeto do jogo
                    if b == True:
                    # se b for False, val_word imprime a mensagem e o while True acima reinicia
                        lista = gera_lista(arq_path) # cria uma lista com o arquivo como está

                        if lista == 0 or word not in lista:      # se a lista for vazia não há motivo para verificar se a palavra já existe na lista. se a lista contém palavras, e a nova não está na lista, ela pode ser adicionada
                            print("Adicionando nova palavra...")
                            arq.write(word+'\n')
                            print("Sucesso!")
                            return
                        
                        else: # verifica se a palavra já está na lista
                            print("A palavra inserida já existe na lista.\nDeseja inserir outra?(s/n)") #
                            while True:                                                                 #
                                ans = input().strip().lower()                                           #
                                if ans == 's':                                                          #
                                    break                                                               # se a palavra já existe, pergunta até obter uma resposta válida se o usuário deseja inserir outra palavra ou não.
                                elif ans == 'n':                                                        #
                                    return                                                              #
                                else:                                                                   #
                                    print("Por favor insira 's' ou 'n'.")                               #
                            
        else:
            arq.write(sys_word+'\n')

# remove palavras
def rem_word(arq_path):            # recebe o caminho do arquivo atualmente em uso
    lista = gera_lista(arq_path)   # gera a lista com as palavras
    if lista == 0:                 # se a lista gerada retornar inválida, o arquivo tem algum erro de formatação ou não existe
        return                     # como a mensagem para isso é gerida pela função gera lista, apenas retornamos

    #se a lista estiver ok...
    for i in range (len(lista)): # imprime cada palavra com seu respectivo número ao lado
        print(i+1, lista[i])     #

    while True:
        try:
            n = int(input("Insira o número correspondente à palavra a ser deletada:\n(ou insira '0' para limpar o arquivo)\n").strip()) # recebe o número da palavra ou 0 para limpar a palavra ou o arquivo todo

            if n < 0 or n > len(lista):                          # valida inputs fora do intervalo aceito
                print("Não há palavra com esse número na lista.") #

            else: # se é uma palavra válida a ser deletada ou 0...
                with open (arq_path, "w", encoding="utf-8"): # sobrescreve o arquivo, limpando-o
                    pass                                     #

                if n != 0: # se o número não for 0...
                    for i in range(len(lista)):          #
                        if i != n-1:                     # reescreve (usando a add_word) o arquivo passando uma palavra da lista gerada por vez por meio do parâmetro sys_word
                            add_word(arq_path, lista[i]) #
                print('Sucesso!')                        #
                break

        except ValueError:               #caso não seja um inteiro, pede por um
            print('Insira um inteiro.')


# valida um caminho
def valid_path(msg):
    while True:
        caminho = input(msg).lower().strip() # pede o caminho
        if caminho == '': # lida com o caso do input vazio
            print("O caminho não pode ser vazio!")

        elif caminho.endswith(".txt") == False: # lida com o caso de o formato de arquivo não ser .txt
            print("O arquivo deve estar no formato .txt")

        else:
            lista = gera_lista(caminho) # tenta gerar uma lista com o caminho do arquivo. em caso de impossibilidade, o motivo é mostrado pela função gera lista, enquanto a função valid_path retorna 0.
            if lista == 0:
                print("O caminho foi redefinido para o padrão 'words.txt'") # não foi ainda, mas será logo após o retorno da função
                return 0
            else:
                return caminho # se a lista puder ser gerada, retorna o caminho
