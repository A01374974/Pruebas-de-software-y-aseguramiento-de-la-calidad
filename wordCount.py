import sys
import time
import re


def leer_archivo (filename):
    with open(filename, "r", encoding="utf-8") as file:
        contenido = file.read().lower()
    palabras = re.split(r'\W+', contenido)
    lista_palabras = []
    for palabra in palabras:
        if palabra:
            lista_palabras.append(palabra)
    return palabras


def contar_palabras(lista):
    contador_palabras = {}
    for palabra in lista:
        if palabra in contador_palabras:
            contador_palabras[palabra] = contador_palabras[palabra] + 1
        else:
            contador_palabras[palabra] = 1
    del contador_palabras[""]
    return contador_palabras


def escribir_archivo(resultados):
    with open("WordCountResults.txt", "w") as archivo:
        for palabra, conteo in resultados.items():
            archivo.write(f"{palabra}: {conteo}\n")


def imprimir_resultados(resultados):
    for palabra, conteo in resultados.items():
        print(f"{palabra}: {conteo}")


def word_count(filename):
    tiempo_inicial = time.time()
    lista_palabras = leer_archivo(filename)
    conteo_palabras = contar_palabras(lista_palabras)
    escribir_archivo(conteo_palabras)
    imprimir_resultados(conteo_palabras)
    tiempo_final = time.time()
    print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicial:.8f} segundos")


def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
    else:
        word_count(sys.argv[1])


if __name__ == "__main__":
    main()
