import math
from grafica import grafica

def codificarVertice(vertice):
    """
    Codifica un vértice representándolo con una cadena de ceros de longitud igual al valor del vértice.
    
    Args:
        vertice (int): Número del vértice.
    
    Returns:
        str: Cadena de ceros de longitud `vertice`.
    """
    return '0'*vertice

def codificarVertices(vertices):
    """
    Codifica una lista de vértices representando cada uno con una cadena de ceros
    y separándolos con '1'.
    
    Args:
        vertices (list of int): Lista de vértices.
    
    Returns:
        str: Codificación de los vértices en una sola cadena.
    """
    return '1'.join('0'*n for n in vertices)

def codificarAristas(aristas):
    """
    Codifica una lista de aristas utilizando la función `codificarTupla` y separándolas con '1'.
    
    Args:
        aristas (list of tuple): Lista de aristas representadas como tuplas de vértices.
    
    Returns:
        str: Codificación de las aristas en una sola cadena.
    """
    return '1'.join(codifcarTupla(n) for n in aristas)

def codifcarTupla(tupla):
    """
    Codifica una tupla de números representando cada número con una cadena de ceros,
    separados por '1'.
    
    Args:
        tupla (tuple of int): Tupla de dos vértices que representan una arista.
    
    Returns:
        str: Codificación de la tupla.
    """
    return '1'.join('0'*n for n in tupla)

def codificar(grafica):
    """
    Codifica una gráfica representando su número total de vértices, lista de vértices y lista de aristas.
    
    Args:
        grafica (Grafica): Objeto que contiene la información de la gráfica.
    
    Returns:
        str: Codificación de la gráfica como una cadena.
    """
    codificacion = ""
    codificacion += codificarVertice(grafica.numero)
    codificacion += "11"
    codificacion += codificarVertices(grafica.vertices)
    codificacion += "11"
    codificacion += codificarAristas(grafica.aristas)
    return codificacion

def decodificar(codificacion):
    longitud = len(codificacion)
    numVer = math.floor(math.sqrt(longitud))

    matriz = [[0 for _ in range(numVer)] for _ in range(numVer)]
    caracteres = list(codificacion)
    k=0

    for i in range(numVer):
        for j in range(numVer) :
            matriz[i][j] = int(caracteres[k])
            k += 1

   # for fila in matriz:
   #     for columna in fila:
   #         if caracteres[0] == '1':
   #             fila[columna] = 1
   #         caracteres = caracteres[1:]
    


    return matriz
    
