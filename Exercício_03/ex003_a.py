# Número Fatorial
# Calcular o fatorial de um número digitado pelo usuário através do método factorial da biblioteca math

from math import factorial
n = int(input('Digite um número: '))
fatorial = factorial(n)
print(f'{n}! = {fatorial}')
