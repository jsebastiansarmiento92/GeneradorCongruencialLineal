import math
import matplotlib.pyplot as plt

class GeneradorCongruencialLineal:
    def __init__(self, semilla, a, c, m):
        """
        Inicializa el generador congruencial lineal con sus parámetros.
        :param semilla: Semilla inicial.
        :param a: Multiplicador.
        :param c: Incremento.
        :param m: Módulo.
        """
        self.semilla = semilla
        self.a = a
        self.c = c
        self.m = m
        self.estado = semilla  # Estado actual del generador

    def generar_uniforme(self):
        """
        Genera un número pseudoaleatorio uniforme en el rango [0, 1).
        :return: Número pseudoaleatorio.
        """
        self.estado = (self.a * self.estado + self.c) % self.m
        return self.estado / self.m  # Normalizar para obtener un número entre 0 y 1


class DistribucionExponencial:
    def __init__(self, lambda_param, generador_uniforme):
        """
        Inicializa la clase con el parámetro lambda y el generador de números uniformes.
        :param lambda_param: Tasa de la distribución (1/media).
        :param generador_uniforme: Instancia del generador congruencial lineal.
        """
        self.lambda_param = lambda_param
        self.generador_uniforme = generador_uniforme

    def generar(self, n):
        """
        Genera una lista de n números aleatorios con distribución exponencial.
        :param n: Cantidad de números a generar.
        :return: Lista de números generados.
        """
        numeros_aleatorios = []
        for _ in range(n):
            u = self.generador_uniforme.generar_uniforme()  # Genera un número aleatorio uniforme entre 0 y 1
            x = -math.log(1 - u) / self.lambda_param  # Aplicación de la fórmula de la inversa
            numeros_aleatorios.append(x)
        return numeros_aleatorios

# Ejemplo de uso
if __name__ == "__main__":
    # Parámetros del generador congruencial lineal (LCG)
    semilla = 13458
    a = 1664525
    c = 1013904223
    m = 2**32
    n = 1000  # Cantidad de números a generar

    # Parámetro lambda de la distribución exponencial
    lambda_param = 1.5

    # Crear instancia del generador congruencial lineal
    generador_uniforme = GeneradorCongruencialLineal(semilla, a, c, m)

    # Crear instancia del generador exponencial
    generador_exponencial = DistribucionExponencial(lambda_param, generador_uniforme)

    # Generar números exponenciales
    numeros_exponenciales = generador_exponencial.generar(n)

    # Imprimir los primeros 10 números generados como ejemplo
    print("Primeros 10 números generados con distribución exponencial:")
    for numero in numeros_exponenciales[:10]:
        print(numero)

    # Graficar los resultados
    plt.plot(numeros_exponenciales, marker='o', linestyle='-', color='b')
    plt.title('Números Generados con Distribución Exponencial')
    plt.xlabel('Índice')
    plt.ylabel('Valor Exponencial')
    plt.grid(True)
    plt.show()

    # Graficar un histograma de los números generados
    plt.hist(numeros_exponenciales, bins=30, color='g', alpha=0.7)
    plt.title('Histograma de la Distribución Exponencial')
    plt.xlabel('Valor Exponencial')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()
