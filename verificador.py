import sys
from grafica import grafica
from lectura_entrada import lectura_archivo as lector 
from lectura_entrada import crearGrafica as mkGraph

def leerCertificado(archivo):
    numeros = ""
    with open(archivo,'r') as f:
        linea = f.readline().strip()
        numeros = list(map(int, linea.split()))
    return numeros

def main():
    archivo = sys.argv[1]
    certificado = leerCertificado(archivo)
    data = lector(sys.argv[2])
    g = mkGraph(data)
    n = len(certificado)

    print("Numero de Vertices: ",g.numVertices())
    print("Numero de aristas:",g.numAristas())
    print("Primer vertice de la ruta inducida:",certificado[0])
    print("Ultimo vertice de la ruta inducida:",certificado[n-1])

    for i in range(0,len(certificado)-1):
        if not (g.esVecino(certificado[i],certificado[i+1])):
            print("no es ruta inducida")
            sys.exit()
    print("es ruta inducida")

main()
