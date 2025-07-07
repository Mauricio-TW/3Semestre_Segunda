def busca_linear(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i  # retorna índice onde encontrou
    return -1  # valor não encontrado

# Testando
numeros = [10, 20, 30, 40, 50]
resultado = busca_linear(numeros, 30)
print("Índice encontrado:", resultado)  # Saída: Índice encontrado: 2

resultado = busca_linear(numeros, 100)
print("Índice encontrado:", resultado)  # Saída: Índice encontrado: -1
