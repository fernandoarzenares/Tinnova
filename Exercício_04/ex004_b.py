# Soma dos múltiplos de 3 ou 5
# Somar todos os números múltiplos de 3 ou 5 que estejam entre 0 até o número digitado

def somarMult(n):
    soma = 0
    for c in range(0, n+1):
        if c % 3 == 0 or c % 5 == 0:
            soma += c
    return soma


print(f'{somarMult(10)}')
