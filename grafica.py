
class grafica:
    numero = 0
    vertices = set()
    aristas = set()
    matriz = 0 
    
    def __init__(self):
        vertices = set()
        aristas = set()

    def agregarNumero(self,num):
        self.numero = num 

    def agregarVertice(self,vertice):
        
        if isinstance(vertice,int):
            self.vertices.add(vertice)
        else:
            raise ValueError("el vertice debe ser nombrado con un numero")

    def agregarArista(self, v1, v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.aristas.add((min(v1,v2), max(v1,v2)))
        else:
            raise ValueError("algun vertice no es parte de la grafica")

    def numAristas(self):
        return len(self.vertices)

    def numVertices(self):
        return len(self.aristas)

    def esVecino(self,a,b):
        return (a,b) in self.aristas 



