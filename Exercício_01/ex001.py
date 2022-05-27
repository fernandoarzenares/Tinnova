# Votos Eleitorais
# Calcular o percentual de votos válidos, brancos e nulos

class Eleitores(object):
    def __init__(votos):
        votos.total = 1000
        votos.válidos = 800
        votos.brancos = 150
        votos.nulos = 50

    # Retorna percentual dos votos válidos
    def calcula_válidos(votos):
        return votos.válidos * 100 / votos.total

   # Retorna o percentual dos votos brancos
    def calcula_brancos(votos):
        return votos.brancos * 100 / votos.total

    # Retorna o percentual dos votos nulos
    def calcula_nulos(votos):
        return votos.nulos * 100 / votos.total


eleitores = Eleitores()

# Imprimindo os valores na tela
print(f'O percentual de votos válidos é de {eleitores.calcula_válidos()}%')
print(f'O percentual de votos brancos é de {eleitores.calcula_brancos()}%')
print(f'O percentual de votos nulos é de {eleitores.calcula_nulos()}%')
