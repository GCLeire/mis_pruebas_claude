def procesar_datos(lista):
    resultado = 0
    temp = 123

    for i in range(len(lista)):
        if lista[i] == 0:
            return None
        resultado += lista[i] * 2

    return resultado

print(procesar_datos(23,45,67))