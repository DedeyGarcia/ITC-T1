print('Simulador Universal de Autômatos Finitos')
newFileName = input("Entre com o nome ou endereço do arquivo de entrada: ")     #Explicar no manual como tratar o enderaço corretamente

#Início do tratamento dos dados de entrada

#Divisão do arquivo em linhas e destrincha-lás em variáveis

newFile = open(newFileName, 'r')
newFileLines = newFile.readlines()

numberOfStates = newFileLines[0]
print('Número de Estados Q: ' + numberOfStates)

quantityOfTerminalSymbols = newFileLines[1][0]
print('Quantidade de Simbolos terminais (Σ): ' + quantityOfTerminalSymbols)
terminalSymbolsList = []
for i in newFileLines[1][1:]:
    if i != ' '  and i != '\n':
        terminalSymbolsList.append(i)
print('Lista de símbolos terminais (Σ): ')
print(terminalSymbolsList)

quantityOfAcceptanceStates = newFileLines[2][0]
print('Quantidade de Estados de aceitação (F): ' + quantityOfAcceptanceStates)
acceptanceStatesList = []
for i in newFileLines[2][1:]:
    if i != ' '  and i != '\n':
        acceptanceStatesList.append(i)
print('Lista de Estados de aceitação (F): ')
print(acceptanceStatesList)

numberOfTransitions = newFileLines[3]
print('o número de transições (δ) da máquina: ', numberOfTransitions)

transitionsList = []
for i in range(4, 4 + int(numberOfTransitions)):
    transitionsList.append(newFileLines[i].replace('\n', ''))
print('Lista de transições (δ): ')
print(transitionsList)

numberOfChainsLine = 4 + int(numberOfTransitions)
numberOfChains = newFileLines[numberOfChainsLine]
print('Número de Cadeias: ' + numberOfChains)

chainsList = []
for i in range(numberOfChainsLine + 1, numberOfChainsLine + 1 + int(numberOfChains)):
    chainsList.append(newFileLines[i].replace('\n', ''))
print('Lista de cadeias: ')
print(chainsList)

#Fim do tratamento dos dados de entrada

#Execução do autômato a partir dos dados obtidos da entrada

newFile.close()