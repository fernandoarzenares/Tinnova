# Número Fatorial
# Calcular o fatorial de um número digitado pelo usuário

n = int(input('Digite um número: '))
contador = n
fatorial = 1
print(f'{n}! = ', end='')
while contador > 0:
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
