import sys
import json
import sys
import ast 
import random
from grafica import grafica
import codificar
from lectura_entrada import lectura_archivo as lector
from lectura_entrada import crearGrafica

def guardarCertificado(certificado,archivo):
    """
    Guarda una lista de números enteros en un archivo, separándolos por espacios.
    
    :param certificado: Lista de números enteros que representan un certificado de vértices.
    :param archivo: Nombre del archivo donde se guardará la información.
    """
    cadena = ""
    for i in certificado:
        cadena += str(i)
        cadena += " "
    
    with open(archivo,'w',encoding = 'utf-8') as file:
        file.write(cadena)

def main():
    """
    Función principal que genera un certificado aleatorio de vértices de una gráfica y lo guarda en un archivo.
    
    Uso:
    python script.py <archivo_grafica> <archivo_salida>
    
    Donde:
    - archivo_grafica contiene la descripción del grafo.
    - archivo_salida es el nombre del archivo donde se guardará el certificado.
    """
    data = lector(sys.argv[1])
    print(data)
    g = crearGrafica(data)
    
    certificado = random.sample(list(g.vertices),g.numero)
    print(certificado)
    guardarCertificado(certificado,sys.argv[2])
    

main()
