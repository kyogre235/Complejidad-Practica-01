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
    cadena = ""
    for i in certificado:
        cadena += str(i)
        cadena += " "
    
    with open(archivo,'w',encoding = 'utf-8') as file:
        file.write(cadena)

def main():
    data = lector(sys.argv[1])
    print(data)
    g = crearGrafica(data)
    
    certificado = random.sample(list(g.vertices),g.numero)
    print(certificado)
    guardarCertificado(certificado,sys.argv[2])
    

main()
