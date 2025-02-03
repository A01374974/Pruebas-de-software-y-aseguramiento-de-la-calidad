import sys
import time

def leer_archivo(filename):
    with open(filename, "r") as file:
        data = []
        for line in file:
            line = line.strip()
            if line.replace(".", "", 1).isdigit():
                data.append(float(line))
            else:
                print(f"'{line}' no es un número válido y por lo tanto no será incluido en el procesamiento.")

    return data


def conversion_binario(i):

    if i== 0:
        return "0"
    bin=""
    while i>=1:
        res=i%2
        bin=str(res)+bin
        i=i//2
    return bin

def conversion_hexadecimal(i):
    if i== 0:
        return "0"
    hexDigitos = "0123456789ABCDEF"
    hexadecimal = ""

    while i> 0:
        residuo = i % 16
        hexadecimal = hexDigitos[int(residuo)] + hexadecimal
        i = i // 16

    return hexadecimal

def realizar_conversiones(lista_numeros):
    resultados=[]
    for i in lista_numeros:
        resultados.append(f"La conversión en binario y hexadecimal del número '{i}' respectivamente es {conversion_binario(i)} y {conversion_hexadecimal(i)}")
    print(resultados)
    return resultados


def escribir_archivo(resultados):
    with open("ConvertionResults.txt", "w") as archivo:
        for i in resultados:
            archivo.write(f"{i}\n")

def imprimir_resultados(resultados):
    for i in resultados:
        print(i)

def convert_numbers(filename):
    tiempo_inicial = time.time()
    lista_numeros=leer_archivo(filename)
    resultados=realizar_conversiones(lista_numeros)
    imprimir_resultados(resultados)
    escribir_archivo(resultados)
    tiempo_final = time.time()
    print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicial:.8f} segundos")


def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
    else:
        convert_numbers(sys.argv[1])

if __name__ == "__main__":
    main()