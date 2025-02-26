import sys
import codificar
import json 

def es_conexa(graph):
    """
    Verifica si la gráfica es conexa, ignorando los vértices aislados.

    Parámetros:
    -----------
    graph : list[list[int]]
        Matriz de adyacencia que representa la gráfica.

    Retorna:
    --------
    bool
        True si la gráfica es conexa, False en caso contrario.
    """

    n = len(graph)
    visitados = [False] * n

    # Encuentra el primer nodo con al menos una arista
    def dfs(v):
        visitados[v] = True
        for u in range(n):
            if graph[v][u] > 0 and not visitados[u]:
                dfs(u)

    inicio = next((i for i in range(n) if sum(graph[i]) > 0), -1)
    if inicio == -1:
        return True  # Si no hay aristas, la gráfica es trivialmente conexa

    dfs(inicio)
    return all(visitados[i] or sum(graph[i]) == 0 for i in range(n))

def leer(documento):
    """
    Lee un archivo y devuelve una lista con sus líneas.

    Parámetros:
    -----------
    documento : str
        Ruta del archivo a leer.

    Retorna:
    --------
    list[str]
        Lista con cada línea del archivo como un elemento.
    """
    datos = []
    with open(documento,  encoding="utf-8") as archivo:
        for linea in archivo:
            datos.append(linea.rstrip())
    return datos

def tiene_camino_euleriano(graph):
    """
    Verifica si la gráfica tiene un camino euleriano.

    Parámetros:
    -----------
    graph : list[list[int]]
        Matriz de adyacencia de la gráfica.

    Retorna:
    --------
    tuple (bool, int or None)
        - True y el vértice inicial si existe un camino euleriano.
        - False y None si no existe.
    """
    if not es_conexa(graph):
        return False, None

    impares = [i for i in range(len(graph)) if sum(graph[i]) % 2 == 1]
    if len(impares) in [0, 2]:
        return True, impares[0] if impares else 0
    return False, None

def es_puente(graph, u, v):
    """
    Determina si la arista (u, v) es un puente.

    Parámetros:
    -----------
    graph : list[list[int]]
        Matriz de adyacencia de la gráfica.
    u, v : int
        Vértices de la arista a evaluar.

    Retorna:
    --------
    bool
        True si la arista (u, v) es un puente, False en caso contrario.
    """
    graph[u][v] -= 1
    graph[v][u] -= 1
    conexa_despues = es_conexa(graph)
    graph[u][v] += 1
    graph[v][u] += 1
    return not conexa_despues

def encontrar_camino_euleriano(graph):
    """
    Encuentra un camino euleriano en la gráfica si existe.

    Parámetros:
    -----------
    graph : list[list[int]]
        Matriz de adyacencia de la gráfica.

    Retorna:
    --------
    list[int] or None
        - Lista con el camino euleriano si existe.
        - None si no existe.
    """
    tiene_camino, inicio = tiene_camino_euleriano(graph)
    if not tiene_camino:
        return None

    camino = []
    # Algoritmo de Fleury para encontrar el camino euleriano
    
    def fleury(v):
        for u in range(len(graph)):
            if graph[v][u] > 0:
                if graph[v][u] > 1 or not es_puente(graph, v, u):
                    graph[v][u] -= 1
                    graph[u][v] -= 1
                    fleury(u)
        camino.append(v)

    fleury(inicio)
    return camino[::-1]

def max_grado_vertice(matriz):
    """
    Encuentra el vértice con el mayor grado en la gráfica.

    Parámetros:
    -----------
    matriz : list[list[int]]
        Matriz de adyacencia de la gráfica.

    Retorna:
    --------
    tuple (int, int)
        - Vértice con el mayor grado (sumando aristas incidentes).
        - Valor del grado del vértice.
    """
    numV = len(matriz)
    grados = []
    for fila in range(numV):
        aux=0
        for columna in range(numV):
            if matriz[fila][columna] == 1:
                aux += 1
        grados.append(aux)
    
    grado = max(grados)
    vertice = grados.index(grado)   
    return vertice+1,grado
    

def main ():
    """
    Función principal:
    - Lee una matriz de adyacencia desde un archivo.
    - Determina el vértice con mayor grado.
    - Verifica si existe un camino euleriano e imprime el resultado.
    """
    file = sys.argv[1]
    cadena = leer(file)
    matriz = codificar.decodificar(cadena[0])
    vertice ,numV = max_grado_vertice(matriz)
    euleriano = encontrar_camino_euleriano(matriz)
    
    print("Vertice con mayor grado:",vertice)
    print("Grado del vertice:", numV)
    
    if euleriano:
        euleriano = [x + 1 for x in euleriano]
        print("Si tiene un camino euleriano, el camino euleriano es: ", euleriano)
    else:
        print("No existe un camino euleriano. ")

main()