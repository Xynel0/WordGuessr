
#============================================== imports e definições iniciais ==============================================

import random # usado para escolher a palavra aleatóriamente
import func   # arquivo .py contendo as funções necessárias. Deve estar no mesmo diretório que o presente arquivo

default_path = 'words.txt'  # permite recriar o arquivo de palavras com o nome correto e resetar o caminho, caso necessário
current_path = default_path # guarda o caminho atualmente em uso. inicialmente, é o caminho padrão

#========================================================== main ==========================================================

while True:
    main_menu_return = func.main_menu() # chama o menu inicial e armazena a opção escolhida
    
    #-------------------------------------------------------- jogar --------------------------------------------------------
    if main_menu_return == 1:
        lista = func.gera_lista(current_path) # gera uma lista a partir do caminho atual ou 0 se a lista for inválida
        
        # se a lista puder ser usada...
        if lista != 0:
            while True:
                palavra = random.choice(lista)       # escolhe aleatóriamente uma palavra da lista
                chances = func.dificuldade(palavra)  # define a quantidade de chances a partir da palavra e da dificuldade
                
                if chances == 0: # se a dificuldade retornar 0, quebra o While True da rodada, voltando ao menu inicial
                    break
                #else implícito, já que se a condição para o break for atingida, o While True para imediatamente

                if chances == -1: #
                    zen = True    # se o modo selecionado for o zen, define zen como true
                else:             #
                    zen = False   #
                
                chutes_certos = []   # cria as listas de chutes certos e errados para a rodada
                chutes_errados = []  #
                
                if chances > 25:  # o jogo só conta como erro uma LETRA VÁLIDA porém incorreta(ou uma palavra inteira diferente da correta). assim, com mais que 25 chances, chutar o alfabeto inteiro não resultaria em derrota
                    chances = 25  #
                
                #-------------------------------------------------------------------- rodada --------------------------------------------------------------------
                while chances > 0 or zen: 
                    
                    if zen:                              #
                        chances_restantes = 'infinitas'  # define o que será exibido após cada chute na quantidade de chutes restantes
                    else:                                #
                        chances_restantes = chances      #
                    
                    
                    if len(chutes_errados) >= 1:                           # se já houver algum chute errado na rodada...
                        print()                                            # imprime uma linha vazia para separar o conteúdo seguinte do conteúdo anterior (linha de espaço antes de "Chutes errados:")
                        print('Chutes errados:')                           
                        i_chutes_errados = 1                               #
                        for chute in chutes_errados:                       #
                            if i_chutes_errados != len(chutes_errados):    #
                                print(chute, end = ' | ')                  # percorre a lista de chutes errados, imprimindo cada chute separado por " | ".
                            else:                                          #
                                print(chute)                               #
                                print()                                    #
                            i_chutes_errados += 1                          # (i_chutes_errados serve para controlar o momento de parar de imprimir " | ")

                    for letra in palavra:                  #
                        if letra in chutes_certos:         #
                            print(letra, end=' ')          # percorre a palavra certa letra por letra procurando a referida letra na lista de chutes certos.
                        else:                              # se já estiver lá, a letra é imprimida. se não, um "_" é imprimido.
                            print("_", end=' ')            #
                    print()                                #

                    vitoria = True                           #
                    if palavra not in chutes_certos:         #
                        for letra in palavra:                # confere se, após as atualizações da rodada anterior (abaixo), o jogo foi ganho
                            if letra not in chutes_certos:   #
                                vitoria = False              #

                    if vitoria == True:                                                                                          # se a rodada foi ganha...
                        if tentativas > 1:                                                                                       #
                            print(f"A palavra era {palavra}! Você ganhou!\nSó teve que tentar {tentativas} vezes! Parabéns!!")   # imprime a mensagem de vitoria adequada para a quantidade de tentativas feitas
                        elif tentativas == 1:                                                                                    #
                            print(f"A palavra era {palavra}! Você ganhou!\nSó teve que tentar uma vez! Parabéns!!")              #
                        break                                                                                                    # quebra o laço de repetição da rodada, retornando ao menu 'jogar'
                    #else implícito, pois if vitoria == True: break, então nada nesta identação seria lido.
                    

                    # se ainda há chances (while chances > 0 or zen) e não houve vitória...
                    palpite = func.v_input(chances_restantes, chutes_certos, chutes_errados, len(palavra)) # chama a função responsável por validar chutes
                    
                    if palpite in palavra or palpite == palavra: # se palpite for uma letra correta ou a palavra correta, adiciona aos chutes corretos
                        chutes_certos.append(palpite)
                    
                    else: # se palpite for uma letra errada ou uma palavra errada, adiciona aos chutes errados e tira uma chance
                        chutes_errados.append(palpite)
                        chances -= 1

                    tentativas = len(chutes_certos) + len(chutes_errados) # computa quantas tentativas foram feitas ao todo
                
                # se as chances são menores que 1 E o modo zen NÃO está ativado, ou o programa breakou o while com chances restantes (caso de vitória)...
                if vitoria == False: # se não houve vitória, acabaram as chances e o jogador foi derrotado
                    print(f"Você perdeu!\nA palavra era {palavra}.")
                #_________________________________________________________             fim da rodada                _____________________________________________________
                #                                                         retorna ao menu jogar usando a mesma lista

        
        #se a lista não puder ser usada nas rodadas, não aciona o While True das rodadas e retorna ao menu inicial
        else:
            continue

    #-------------------------------------------------------- configurações --------------------------------------------------------
    elif main_menu_return == 2:
        config_return = func.config() # chama a função que imprime o menu, recebe e valida o input

        if config_return == 0: # voltar ao menu inicial
            continue

        elif config_return == 1: # remover palavras da lista atual
            func.rem_word(current_path) # chama a função responsável por remover palavras (esta função usa a função de adicionar palavras)

        elif config_return == 2: # adicionar palavras à lista atual
            func.add_word(current_path, '') # chama a função responsável por adicionar palavras, passando "sys_word" vazio

        elif config_return == 3: # carregar arquivo de palavras próprio
            msg = "Insira o caminho do arquivo:\n"
            current_path = func.valid_path(msg) # chama a função responsável por determinar se um caminho é válido ou não
            if current_path == 0:
                current_path = default_path # se o caminho não for válido, reseta o caminho para o padrão

        elif config_return == 4: # resetar arquivo de palavras para o padrão
            with open("words.txt", "w", encoding="utf-8"): # sobrescreve o arquivo, limpando-o
                pass
            with open("words.txt", "a", encoding="utf-8") as arq: # preenche o arquivo com as palavras padrão
                for i in ['abacate', 'abacaxi', 'abelha', 'acerola', 'agulha', 'alface', 'alho', 'amizade', 'ancora', 'anel', 'aranha', 'baleia', 'balao', 'banco', 'barco', 'barraca', 'batata', 'beijo', 'berco', 'biscoito', 'boneca', 'botao', 'brinco', 'bruxa', 'cabana', 'cabide', 'caixote', 'calca', 'caneca', 'canoa', 'canudo', 'capivara', 'castelo', 'cebola', 'cenoura', 'cereja', 'chafariz', 'chaveiro', 'chinelo', 'chocalho', 'chuchu', 'cegonha', 'coelho', 'cogumelo', 'colcha', 'colmeia', 'coqueiro', 'coruja', 'cortina', 'gaveta', 'girafa', 'girassol', 'goiaba', 'golfinho', 'gorila', 'grade', 'gravata', 'grelha', 'grilo', 'gruta', 'guaxinim', 'harpa', 'hiena', 'hipopotamo', 'horta', 'helice', 'igreja', 'iogurte', 'jacare', 'jali', 'jarra', 'jasmim', 'javali', 'joaninha', 'jornal', 'judo', 'jumento', 'juriti', 'lagarta', 'lagosta', 'lanche', 'lanterna', 'leao', 'leopardo', 'lesma', 'lagartixa', 'limao', 'lince', 'lixeira', 'lousa', 'lobo', 'lontra', 'lula', 'macaco', 'madeira', 'mastro', 'medalha', 'mochila', 'moinho', 'morcego']:
                    arq.write(i+'\n')
            current_path = default_path #reseta o caminho para o padrão
            print("Sucesso!")

    #-------------------------------------------------------- opção inválida --------------------------------------------------------
    else:
        print("Opção inválida. Insira um dos números abaixo.")
    #(sair é processado em func.main_menu)
