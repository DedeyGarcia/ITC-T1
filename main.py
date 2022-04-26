'''
    testChainNew(chain):
    Função que define um estado inicial para o simulador e 
    chama a função recursiva de analise de cadeias testSubchain(chain, state).
'''
def testChainNew(chain):
    global acceptanceStatesList, terminalSymbolsList, transitionsList
    initialState = 0

    return testSubchain(chain, initialState)

'''
    testSubchain(chain, state)
    Função recursiva que testa se uma subCadeia 
    dada a partir da cadeia inicial é valida.
    Tem como caso base da recursão chegar a uma cadeia vazia
    seja ela '' ou a string de cadeia vazia definada no input ('-')
'''
def testSubchain(chain, state):
    global acceptanceStatesList, terminalSymbolsList, transitionsList
   
    if(chain == '' or chain == '-'):
        if state in acceptanceStatesList:
            return True
        return False

    currentChainInput = chain[0]

    for transition in transitionsList:
        if int(transition[0]) == int(state) and transition[2] == currentChainInput:
            return testSubchain(chain[1:], transition[4])

    return False


'''
    Função principal do arquivo, realiza a leitura de dados
    a partir de um arquivo e faz a chamada das funções de analise
    das cadeias
'''
if __name__ == "__main__":
    print('Simulador Universal de Autômatos Finitos')
    newFileName = input("Entre com o nome ou endereço do arquivo de entrada: ")     #Explicar no manual como tratar o enderaço corretamente

    # Início do tratamento dos dados de entrada
    
    newFile = open(newFileName, 'r')
    newFileLines = newFile.readlines()

    numberOfStates = newFileLines[0]

    quantityOfTerminalSymbols = newFileLines[1][0]

    terminalSymbolsList = []
    for i in newFileLines[1][1:]:
        if i != ' '  and i != '\n':
            terminalSymbolsList.append(i)


    quantityOfAcceptanceStates = newFileLines[2][0]

    acceptanceStatesList = []
    for i in newFileLines[2][1:]:
        if i != ' '  and i != '\n':
            acceptanceStatesList.append(i)

    numberOfTransitions = newFileLines[3]

    transitionsList = []
    for i in range(4, 4 + int(numberOfTransitions)):
        transitionsList.append(newFileLines[i].replace('\n', ''))

    numberOfChainsLine = 4 + int(numberOfTransitions)
    numberOfChains = newFileLines[numberOfChainsLine]

    chainsList = []
    for i in range(numberOfChainsLine + 1, numberOfChainsLine + 1 + int(numberOfChains)):
        chainsList.append(newFileLines[i].replace('\n', ''))

    # Fim do tratamento dos dados de entrada

    # Execução da simulação autômato 
    # a partir dos dados obtidos da entrada e escrito no arquivo de saída

    outFile = open("ExemploOut.txt", "w")

    for i in chainsList:
        if(testChainNew(i)): 
            outFile.write("Aceita\n")
        else:
            outFile.write("Rejeita\n")

    outFile.close()
    newFile.close()

