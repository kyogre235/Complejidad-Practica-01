import sys
import codificar
import json 

def camino(matriz):
    vertices_impares = 0
    numV = len(matriz)
    
    for i in range(numV):
        vecinos = 0
        for j in range(numV):
            if matriz[j][i] == 1:
                vecinos += 1
                
        if vecinos % 2 != 0:
            vertices_impares += 1
        if vertices_impares > 2:
            
            return False
    if vertices_impares  >= 1:
        
        return False
    
    return True

def leer(documento):
    datos = []
    with open(documento,  encoding="utf-8") as archivo:
        for linea in archivo:
            datos.append(linea.rstrip())
    return datos

def pasoEu(matriz,inicio):
    lista = []
    
    numV = len(matriz)

    for i in range(numV):
        for j in range(numV):
            if matriz[i][j] == 1:
                matriz[i][j] = 0
                matriz[j][i] = 0
                lista.append(i+1)
                if j == numV-1:
                    i=j-2
                else:
                    i=j
                j=0
    
    return lista

def main ():
    file = sys.argv[1]
    cadena = leer(file)
    matriz = codificar.decodificar(cadena[0])
    euleriano = camino(matriz)
    print(euleriano)
    print(pasoEu(matriz,1))

main()




