def lectura_archivo(documento: str) :
    datos = []
    with open(documento, encoding="utf-8") as archivo:
        for linea in archivo:
            datos.append(linea.rstrip())
    return datos

def main():
    datos  = lectura_archivo("prueba.txt")
    print(datos)

main()