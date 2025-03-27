import sys
from grafica import grafica
from lectura_entrada import lectura_archivo as lector 
from lectura_entrada import crearGrafica as mkGraph

def leerCertificado(archivo):
    """
    Lee un archivo que contiene una línea de números enteros separados por espacios
    y los convierte en una lista de enteros.
    
    :param archivo: Ruta del archivo que contiene el certificado
    :return: Lista de enteros extraídos del archivo
    """
    numeros = ""
    with open(archivo,'r') as f:
        linea = f.readline().strip()
        numeros = list(map(int, linea.split()))
    return numeros

def main():
    """
    Función principal que verifica si una secuencia de vértices forma una ruta inducida
    en una gráfica dada.
    
    Uso:
    python verificador.py <archivo_certificado> <archivo_grafica>
    
    Donde:
    - archivo_certificado contiene la secuencia de vértices.
    - archivo_grafica contiene la descripción del grafo.
    """
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
