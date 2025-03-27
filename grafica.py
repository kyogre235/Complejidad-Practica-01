
class grafica:
    """
    Clase que representa una estructura de datos de gráfica no dirigida.
    
    Atributos:
    - numero: Un identificador o número asociado a la gráfica.
    - vertices: Conjunto de vértices de la gráfica.
    - aristas: Conjunto de aristas representadas como tuplas (v1, v2).
    - matriz: Atributo no utilizado en la implementación actual.
    """
    numero = 0
    vertices = set()
    aristas = set()
    matriz = 0 
    
    def __init__(self):
        """
        Constructor de la clase grafica. Inicializa los conjuntos de vértices y aristas.
        """
        vertices = set()
        aristas = set()

    def agregarNumero(self,num):
        """
        Asigna un número identificador a la gráfica.
        :param num: Número entero a asignar.
        """
        self.numero = num 

    def agregarVertice(self,vertice):
        """
        Agrega un vértice a la gráfica si es un número entero.
        
        :param vertice: Número entero que representa el vértice.
        :raises ValueError: Si el vértice no es un número entero.
        """
        if isinstance(vertice,int):
            self.vertices.add(vertice)
        else:
            raise ValueError("el vertice debe ser nombrado con un numero")

    def agregarArista(self, v1, v2):
        """
        Agrega una arista no dirigida entre dos vértices existentes en la gráfica.
        
        :param v1: Primer vértice.
        :param v2: Segundo vértice.
        :raises ValueError: Si alguno de los vértices no pertenece a la gráfica.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.aristas.add((v1,v2))
            self.aristas.add((v2,v1))
        else:
            raise ValueError("algun vertice no es parte de la grafica")

    def numAristas(self):
        """
        Devuelve el número de aristas en la gráfica.
        :return: Número de aristas sin contar duplicados (direcciones).
        """
        return len(self.aristas)//2

    def numVertices(self):
        """
        Devuelve el número de vértices en la gráfica.
        :return: Número de vértices.
        """
        return len(self.vertices)

    def esVecino(self,a,b):
        """
        Verifica si dos vértices son vecinos (están conectados por una arista).
        
        :param a: Primer vértice.
        :param b: Segundo vértice.
        :return: True si (a, b) es una arista en la gráfica, False en caso contrario.
        """
        return (a,b) in self.aristas 



