import random


class nodo:
    def __init__(self,dato,hn,np):
        self.dato = dato
        self.hijos=[]
        self.hn = hn
        self.np = np

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

#Generando el posicionamiento aleatorio
def posiPiezas(pieza):  
    numeroF = random.randint(0, 6)
    numeroC = random.randint(0, 7)
    while(juego[numeroF][numeroC] == 1 or juego[numeroF][numeroC]==2):
        numeroF = random.randint(0, 6)
        numeroC = random.randint(0, 7)
    juego[numeroF][numeroC] = pieza
    return numeroF,numeroC
    
    

#Bucar fantasma

#Función euclidiana
""" def distanciaEclidiana(): """
    

#Estado inicial de juego 

juego = [
    ["X", "X", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", "X", ".", "."],    
    ["X", ".", ".", ".", ".", "X", ".", "."],
    [".", ".", ".", "X", "X", "X", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["X", "X", "X", ".", ".", ".", ".", "."]
]


posiPiezas("P")
posiPiezas("F")
    
print("JUEGO INICIAL:")
for fila in juego:
    print(" ".join(fila))



#Algoritmo Hill Climbing



#Algoritmo A*