# Soma dos múltiplos de 3 ou 5
# Somar todos os números múltiplos de 3 ou 5 que estejam entre 0 até o número digitado pelo usuário

n = int(input('Digite um número: '))
soma = 0
for c in range(0, n+1):
    if c % 3 == 0 or c % 5 == 0:
        soma += c
print(f'A soma dos múltiplos de 3 e 5 entre 0 e {n} é {soma}')
