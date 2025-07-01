numeros = [2, 4, 6, 8, 10, 12, 14]

def dividirNumeros(d):
    return d / 2

dividivos = map(dividirNumeros, numeros)
print(list(dividivos))

def multiplicarNumeros(m):
    return m * 5

multiplicados = map(multiplicarNumeros, numeros)
print(list(multiplicados))

def subtrairNumeros(s):
    return s - 5

subtraidos = map(subtrairNumeros, numeros)
print(list(subtraidos))

def somarNumeros(so):
    return so + 10

somados = map(somarNumeros, numeros)
print(list(somados))

def final(alteracoes):
    aumento = 0
    for x in alteracoes:
        aumento += x
    return aumento

aumentos = map(final, ((numeros), [1, 2, 3, 4, 5, 6, 7]))
print(list(aumentos))