import sys
import time

def leer_archivo(filename):
        with open(filename, "r") as file:
            data=[]
            for line in file:
                line = line.strip()
                if line.replace(".", "", 1).isdigit():
                    data.append(float(line))
                else:
                    print(f"'{line}' no es un número válido y por lo tanto no será incluido en los cálculos.")
        return data


def calcular_promedio(lista):
    sumaNumeros=0
    for numero in lista:
        sumaNumeros += numero
    promedio=sumaNumeros/len(lista)
    return "El promedio es: "+str(promedio)

def calcular_mediana(lista):
    lista.sort()
    if len(lista)%2==1:
        mediana=lista[len(lista)//2]
    else:
        mediana = lista[len(lista) // 2]+lista[len(lista) // 2-1]
    return "La mediana es: " + str(mediana)

def calcular_moda(lista):
    contador_numeros={}
    for numero in lista:
        if numero in contador_numeros:
            contador_numeros[numero] = contador_numeros[numero] + 1
        else:
            contador_numeros[numero] = 1
    moda = []
    maximo_ocurrencia = 0
    for num in contador_numeros:
        if contador_numeros[num] > maximo_ocurrencia:
            maximo_ocurrencia = contador_numeros[num]
            moda = [num]
        elif contador_numeros[num] == maximo_ocurrencia:
            moda.append(num)
    if len(moda)==len(lista):
        return "No hay moda"
    elif len(moda)>1:
        modaStr="La moda son: "+str(moda)
        return modaStr
    else:
        modaStr="La moda es: "+str(moda)
        return modaStr

def calcular_desviacion_estandar(lista):
    suma_numeros = 0
    for numero in lista:
        suma_numeros += numero
    promedio = suma_numeros / len(lista)
    for numero in lista:
        desviacion=(numero-promedio)**2
    desviacion=desviacion/len(lista)
    desviacion=desviacion**0.5
    return "La desviación estándar es: " + str(desviacion)

def calcular_varianza(lista):
    suma_numeros = 0
    for numero in lista:
        suma_numeros += numero
    promedio = suma_numeros / len(lista)
    for numero in lista:
        desviacion = (numero - promedio) ** 2
    desviacion = desviacion / len(lista)
    return "La varianza es: " + str(desviacion)

def escribir_archivo(resultados):
    with open("StatisticsResults.txt", "w") as archivo:
        for i in resultados:
            archivo.write(f"{i}\n")

def imprimir_resultados(resultados):
    for i in resultados:
        print(i)

def computeStatistics(filename):
    tiempoInicial = time.time()
    lista_numeros=leer_archivo(filename)
    resultados=[]
    resultados.append(calcular_promedio(lista_numeros))
    resultados.append(calcular_mediana(lista_numeros))
    resultados.append(calcular_moda(lista_numeros))
    resultados.append(calcular_desviacion_estandar(lista_numeros))
    resultados.append(calcular_varianza(lista_numeros))
    escribir_archivo(resultados)
    imprimir_resultados(resultados)
    tiempoFinal = time.time()
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicial:.8f} segundos")


def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
    else:
        computeStatistics(sys.argv[1])

if __name__ == "__main__":
    main()