from math import sqrt

class vector: #crea un objeto de clase vector con sus operaciones y default dim = 3
    def __init__(self, dim=3):
        if dim < 1:
            print("Tontuelo, estás calculando para un punto... o peor o.O")
        self.elementos = [] #Se inicializa el arreglo para el vector
        self.dimension = dim #Se asigna la dimensión como variable local de la clase
        for i in range(self.dimension):
            try:
                self.elementos.append(float(input("valor para el índice " + str(i+1) + " = ")))
            except:
                print("Eso no era un número ergo ejecuto la auto-morisión x_x")
                raise BaseException #termina el programa de inmediato
    
    def ppunto(self, b): #producto punto (escalar) entre dos vectores self y b
        p = 0
        for i in range(self.dimension):
            p += self.elementos[i]*b[i]
        return p
    
    def pcruz(self, b): #producto cruz (exterior) entre dos vectores self y b
        if self.dimension == 3: #sólo si la dimensión es igual a 3
            a = self.elementos #nueva variable a para simplicidad
            c = [a[1]*b[2] - a[2]*b[1],
                 a[2]*b[0] - a[0]*b[2],
                 a[0]*b[1] - a[1]*b[0]]
            return c
        else:
            print("Sólo se calcular producto cruz en 3 dimensiones, no en " + str(self.dimension))
            return 0
        
    def modulo(self): #expresado como la raíz cuadrada del producto punto con si mismo
        return sqrt(self.ppunto(self.elementos))
    
    def invertir(self): #refleja todos sus elementos
        for i in range(self.dimension):
            self.elementos[i] = -self.elementos[i]
    
    
    
while True:
    try:
        d = int(input("Dimensión del vector a crear = "))
        break
    except:
        print("Dato inválido, intenta de nuevo")
try:        
    print("Para el primer vector: ")
    test = vector(d)
    print("Para el segundo vector: ")
    test2 = vector(d)
    print()
    print("Vector = ", test.elementos)
    print("Módulo = ", round(test.modulo(),3))
    print()
    test.invertir()
    print("Vector invertido = ", test.elementos)
    print("Módulo invertido = ", round(test.modulo(),3))
    print()
    print("Producto cruz = ", test.pcruz(test2.elementos))
    print()
    print("FIN (éxito)")
except:
    print("FIN (error)")