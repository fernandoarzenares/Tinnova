# Algoritmo de Ordenação Bubble Sort
# Ordenar o vetor [5, 3, 2, 4, 7, 1, 0, 6] utilizando o algoritmo de ordenação Bubble Sort até que os elementos fiquem totalmente em ordem crescente

def bubbleSort(vetor):

    for final in range(len(vetor), 0, -1):
        for posição in range(0, final - 1):
            if vetor[posição] > vetor[posição + 1]:
                vetor[posição], vetor[posição + 1] = vetor[posição + 1], vetor[posição]


vetor = [5, 3, 2, 4, 7, 1, 0, 6]
bubbleSort(vetor)
print(vetor)
