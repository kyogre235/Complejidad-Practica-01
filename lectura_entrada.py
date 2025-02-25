import json
import sys
import ast
from grafica import grafica
import codificar
import math
def lectura_archivo(documento: str) :
    """
    Lee un archivo y devuelve una lista de líneas sin saltos de línea.
    
    Args:
        documento (str): Nombre del archivo a leer.
    
    Returns:
        list: Lista de líneas del archivo.
    """
    datos = []
    with open(documento, encoding="utf-8") as archivo:
        for linea in archivo:
            datos.append(linea.rstrip())
    return datos

def crearGrafica (datos):
    """
    Crea un objeto de tipo grafica a partir de los datos proporcionados.
    
    Args:
        datos (list): Lista que contiene el número de vértices, los vértices y las aristas.
    
    Returns:
        grafica: Objeto de la clase grafica con los datos procesados.
    """
    num = int(datos[0])
    vertices = json.loads(str(datos[1]))
    aristas = evaluar_lista_de_tuplas(str(datos[2]))
    graf = grafica()
    graf.agregarNumero(num)
    for vertice in vertices:
        graf.agregarVertice(vertice)
    for arista in aristas:
        graf.agregarArista(arista[0],arista[1])
    return graf


def evaluar_lista_de_tuplas(s):
    """
    Evalúa una cadena para convertirla en una lista de tuplas de enteros.
    
    Args:
        s (str): Cadena con la representación de una lista de tuplas.
    
    Returns:
        list of tuple: Lista de tuplas de enteros.
    
    Raises:
        ValueError: Si el formato de entrada no es válido.
    """
    try:
        resultado = ast.literal_eval(s)
        if isinstance(resultado, list) and all(isinstance(t, tuple) and all(isinstance(n, int) for n in t) for t in resultado):
            return resultado
        else:
            raise ValueError("El formato no es válido.")
    except (SyntaxError, ValueError):
        raise ValueError("Entrada inválida.")    

def main():
    """
    Función principal que lee un archivo de entrada, crea una gráfica y genera su codificación.
    """
    datos  = lectura_archivo(sys.argv[1])
    g = crearGrafica(datos)
    
    tam = len(g.vertices)
    
    matriz = [[0 for _ in range(tam)] for _ in range(tam)]
        
    for (a,b) in g.aristas:
        matriz[a-1][b-1] = 1
    
    g.matriz = matriz

    codificacion2 = ""
    # Convertir la matriz de adyacencia a una cadena binaria
    for fila in matriz:
        for n in fila:
            codificacion2 += str(n)
    codificacion2 += format(g.numero,'b')
    # Guardar la codificación en un archivo
    guardar(sys.argv[2],codificacion2)

    print("la cantidad de vertices es: ",len(g.vertices))
    print("la cantidad de aristas es: ",math.floor(len(g.aristas)/2))

    
def guardar(file,codificacion):
    """
    Guarda la codificación de la gráfica en un archivo.
    
    Args:
        file (str): Nombre del archivo donde se guardará la codificación.
        codificacion (str): Cadena codificada de la gráfica.
    """
    with open(file,'w',encoding = 'utf-8') as archivo:
        archivo.write(codificacion)

main()
