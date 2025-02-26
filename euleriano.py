import sys
import codificar
import json 

def es_conexa(graph):
    """Verifica si la gráfica es conexa, ignorando vértices aislados."""
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
    datos = []
    with open(documento,  encoding="utf-8") as archivo:
        for linea in archivo:
            datos.append(linea.rstrip())
    return datos

def tiene_camino_euleriano(graph):
    """Verifica si la gráfica tiene un camino euleriano."""
    if not es_conexa(graph):
        return False, None

    impares = [i for i in range(len(graph)) if sum(graph[i]) % 2 == 1]
    if len(impares) in [0, 2]:
        return True, impares[0] if impares else 0
    return False, None

def es_puente(graph, u, v):
    """Verifica si la arista (u, v) es un puente."""
    graph[u][v] -= 1
    graph[v][u] -= 1
    conexa_despues = es_conexa(graph)
    graph[u][v] += 1
    graph[v][u] += 1
    return not conexa_despues

def encontrar_camino_euleriano(graph):
    """Encuentra un camino euleriano si existe."""
    tiene_camino, inicio = tiene_camino_euleriano(graph)
    if not tiene_camino:
        return None

    camino = []
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

def main ():
    file = sys.argv[1]
    cadena = leer(file)
    matriz = codificar.decodificar(cadena[0])
    euleriano = encontrar_camino_euleriano(matriz) 
    
    if euleriano:
        euleriano = [x + 1 for x in euleriano]
        print("El camino euleriano es: ", euleriano)
    else:
        print("No existe un camino euleriano. ")

main()




