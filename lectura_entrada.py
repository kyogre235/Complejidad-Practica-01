import json
import sys
import ast
from grafica import grafica
import codificar

def lectura_archivo(documento: str) :
    datos = []
    with open(documento, encoding="utf-8") as archivo:
        for linea in archivo:
            datos.append(linea.rstrip())
    return datos

def crearGrafica (datos):
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
    try:
        resultado = ast.literal_eval(s)
        if isinstance(resultado, list) and all(isinstance(t, tuple) and all(isinstance(n, int) for n in t) for t in resultado):
            return resultado
        else:
            raise ValueError("El formato no es válido.")
    except (SyntaxError, ValueError):
        raise ValueError("Entrada inválida.")    

def main():
    datos  = lectura_archivo(sys.argv[1])
    g = crearGrafica(datos)
    
    tam = len(g.vertices)


    matriz = [[0 for _ in range(tam)] for _ in range(tam)]
        
    for (a,b) in g.aristas:
        matriz[a-1][b-1] = 1
    
    g.matriz = matriz
    codificacion2 = ""
    
    for fila in matriz:
        for n in fila:
            codificacion2 += str(n)
    codificacion2 += format(g.numero,'b')
    
    guardar(sys.argv[2],codificacion2)

    print("la cantidad de vertices es: ",len(g.vertices))
    print("la cantidad de aristas es: ",len(g.aristas))

def guardar(file,codificacion):
    with open(file,'w',encoding = 'utf-8') as archivo:
        archivo.write(codificacion)

main()
