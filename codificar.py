from grafica import grafica

def codificarVertice(vertice):
    return '0'*vertice

def codificarVertices(vertices):
    return '1'.join('0'*n for n in vertices)

def codificarAristas(aristas):
    return '1'.join(codifcarTupla(n) for n in aristas)

def codifcarTupla(tupla):
    return '1'.join('0'*n for n in tupla)

def codificar(grafica):
    codificacion = ""
    codificacion += codificarVertice(grafica.numero)
    codificacion += "11"
    codificacion += codificarVertices(grafica.vertices)
    codificacion += "11"
    codificacion += codificarAristas(grafica.aristas)
    return codificacion 


