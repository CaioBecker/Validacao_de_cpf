fim = 'https://www.google.com/search?q=answer+to+life+the+universe+and+everything&oq=answer+&aqs=chrome.5.69i57j0i433i512j0i512j0i131i433i512l2j0i512j0i131i433i512j0i512l3.8595j0j4&sourceid=chrome&ie=UTF-8'

import webbrowser

while fim != 'fim':
    # Variaveis
    parametros = ".-qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_=+{}[]|'';:/?>,<`~"
    indice = 0
    conta = 10
    cpf_separado = []
    num_valida = []
    num = 0
    conta = 10
    resultado = 0
    pergunta_fim = 0
    certo = 'not ok'

    #Funcoes
    def conta(cpf):
        global cpf_separado
        valor = 1 + len(cpf)
        resultado = 0
        for z in cpf:
            resultado += int(z) * valor
            valor -= 1
        if len(cpf) == 8:
            num1 = 11 - (resultado % 11)
            cpf_separado.insert(9, num1)
        else:
            num2 = 11 - (resultado % 11)
            cpf_separado.insert(10, num2)

    #Validar se o usuario vai digitar certo
    while certo != 'ok':

        #Receber o cpf
        cpf = input("digite o seu cpf: ")

        #Remover os pontos e o traco do cpf
        for x in range(len(parametros)):
            cpf = cpf.replace(parametros[x],"")


        if len(cpf) == 11:
            certo = 'ok'
        else:
            pass
    #Separar os numeros
    for valor in cpf:
        if indice < 9:
            cpf_separado.insert(indice, cpf[indice])
            indice += 1
        else:
            num_valida.insert(num, cpf[indice])
            indice += 1
            num += 1
    #Contas
    conta(cpf_separado)
    conta(cpf_separado)

    #Validacao
    if int(num_valida[0]) == cpf_separado[9]:
        if int(num_valida[1]) == cpf_separado[10]:
            print('Tudo certo, este cpf esta certo')
        else:
            print('Cpf invalido')
    else:
        print('Cpf invalido')

    #Perguntar se o usuario vai querer fazer outra validacao
    while pergunta_fim == 0:
        outra_vez = input('Voce quer validar outro cpf? ')
        if outra_vez[0] == 'S' or outra_vez[0] == 's':
            pergunta_fim = 1
        elif outra_vez[0] == 'N' or outra_vez[0] == 'n':
            pergunta_fim = 1
            fim = 'fim'
        elif outra_vez == 'video':
            new = 2
            url = "youtube.com/watch?v=dQw4w9WgXcQ"
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)

        elif outra_vez == 'jogo da velha':
            #Um easter egg
            def menu():
                continuar = 1
                while continuar:
                    continuar = int(input("0. Sair \n" +
                                          "1. Jogar novamente\n"))
                    if continuar:
                        game()
                    else:
                        print("Saindo...")

            def game():
                jogada = 0

                while ganhou() == 0:
                    print("\nJogador ", jogada % 2 + 1)
                    exibe()
                    linha = int(input("\nLinha :"))
                    coluna = int(input("Coluna:"))

                    if board[linha - 1][coluna - 1] == 0:
                        if (jogada % 2 + 1) == 1:
                            board[linha - 1][coluna - 1] = 1
                        else:
                            board[linha - 1][coluna - 1] = -1
                    else:
                        print("Nao esta vazio")
                        jogada -= 1

                    if ganhou():
                        print("Jogador ", jogada % 2 + 1, " ganhou apos ", jogada + 1, " rodadas")

                    jogada += 1

            def ganhou():
                # checando linhas
                for i in range(3):
                    soma = board[i][0] + board[i][1] + board[i][2]
                    if soma == 3 or soma == -3:
                        return 1

                # checando colunas
                for i in range(3):
                    soma = board[0][i] + board[1][i] + board[2][i]
                    if soma == 3 or soma == -3:
                        return 1

                # checando diagonais
                diagonal1 = board[0][0] + board[1][1] + board[2][2]
                diagonal2 = board[0][2] + board[1][1] + board[2][0]
                if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
                    return 1

                return 0


            def exibe():
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            print(" _ ", end=' ')
                        elif board[i][j] == 1:
                            print(" X ", end=' ')
                        elif board[i][j] == -1:
                            print(" O ", end=' ')

                    print()


            board = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

            menu()
        else:
            pass

print('Obrigado por usar o nosso programa')
