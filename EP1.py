import random
import time
import math
import heapq

class nodo:
    def __init__(self,dato,hn):
        self.dato = dato
        self.hijos=[]
        self.hn = hn

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

class nodoA:
    def __init__(self,dato,hn,gn):
        self.dato = dato
        self.hijos=[]
        self.hn = hn
        self.gn = gn
        self.fn = hn+gn

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        
    def __lt__(self, otro):
        return self.fn < otro.fn

#Generando el posicionamiento aleatorio
def posiPiezas(pieza):  
    numeroF = random.randint(0, 6)
    numeroC = random.randint(0, 7)
    while(juego[numeroF][numeroC] == 1 or juego[numeroF][numeroC]==2):
        numeroF = random.randint(0, 6)
        numeroC = random.randint(0, 7)
    juego[numeroF][numeroC] = pieza
    return numeroF,numeroC

#Función distancia Manhattan
def distanciaMahattan(pacf,pacc,fanf,fanc):
    dist = abs(pacf - fanf)+abs(pacc-fanc)
    return dist

#Función distancia euclidiana
def distanciaEclidiana():
    dist = math.sqrt(pow(abs(pacf - fanf),2)+pow(abs(pacc-fanc),2))
    return dist


#Función para buscar el pacman(2)
def buscarPacman(juego):
    for i in range(0,7):
        for j in range(0,8):
            if juego[i][j] == 2:
                return i,j

def imprimirJuego(juego):        
    for f in juego:
        for d in range(len(f)):
            if f[d] == 1:
                print("■",end=" ")
            if f[d] == 0:
                print(".",end=" ")
            if f[d] == 2:
                print("C",end=" ")
            if f[d] == 3:
                print("Ö",end =" ")
        print()
    print("\n----------------------\n")

#Estado inicial de juego 
juego = [
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],    
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0]
]

pacf,pacc=posiPiezas(2)
fanf,fanc=posiPiezas(3)

print("JUEGO INICIAL:")
print("■ Obstaculo")
print(". Espacio libre")
print("C Pacman")
print("Ö Fantasma")
imprimirJuego(juego)


nodo1 = nodo(juego,0)
    
#Espacio de trabajo para Hill CLimbing
def generacionEspacio(nodo1, pacf, pacc):
    if (pacf - 1 >= 0 ) and nodo1.dato[pacf - 1][pacc] != 1:
        hijo = [fila.copy() for fila in nodo1.dato] 
        hijo[pacf][pacc] = 0
        hijo[pacf - 1][pacc] = 2
        nodo2 = nodo(hijo, distanciaMahattan(pacf - 1, pacc, fanf, fanc))
        nodo1.agregar_hijo(nodo2)
        
    if (pacc - 1 >= 0) and nodo1.dato[pacf][pacc - 1] != 1:
        hijo = [fila.copy() for fila in nodo1.dato] 
        hijo[pacf][pacc] = 0
        hijo[pacf][pacc - 1] = 2
        nodo2 = nodo(hijo, distanciaMahattan(pacf, pacc - 1, fanf, fanc))
        nodo1.agregar_hijo(nodo2)
    
    if (pacf + 1 <= 6) and nodo1.dato[pacf + 1][pacc] != 1:
        hijo = [fila.copy() for fila in nodo1.dato] 
        hijo[pacf][pacc] = 0
        hijo[pacf+1][pacc] = 2
        nodo2 = nodo(hijo, distanciaMahattan(pacf+1, pacc, fanf, fanc))
        nodo1.agregar_hijo(nodo2)
        
    if (pacc + 1 <= 7) and nodo1.dato[pacf][pacc+1] != 1:
        hijo = [fila.copy() for fila in nodo1.dato] 
        hijo[pacf][pacc] = 0
        hijo[pacf][pacc+1] = 2
        nodo2 = nodo(hijo, distanciaMahattan(pacf, pacc+1, fanf, fanc))
        nodo1.agregar_hijo(nodo2)

def hill_climbing(nodo1):
    agenda = [nodo1]
    tiempo_inicio = time.time()

    while agenda: 
        if time.time() - tiempo_inicio > 0.03:
            print("Tiempo límite excedido. Terminando búsqueda. No se encontró una solución")
            return None
        nodo_actual = agenda.pop(0) 
        fila,columna = buscarPacman(nodo_actual.dato)
        
        print("Seleccionado con hn =", nodo_actual.hn)
        imprimirJuego(nodo_actual.dato)
        
        if (fila == fanf and columna ==fanc):  
            return nodo_actual
        
        generacionEspacio(nodo_actual, int(fila),int(columna))
        agenda.extend(nodo_actual.hijos)
        agenda.sort(key=lambda x: x.hn)  
        if agenda:
            agenda = [agenda[0]]  
    return None

# Llamada a la función
hill_climbing(nodo1)

#Algoritmo A*
def generacionEspacio(nodo1, pacf, pacc):
    if (pacf - 1 >= 0 ) and nodo1.dato[pacf - 1][pacc] != 1:
        hijo = [fila.copy() for fila in nodo1.dato] 
        hijo[pacf][pacc] = 0
        hijo[pacf - 1][pacc] = 2
        nodo2 = nodoA(hijo, distanciaEclidiana(pacf - 1, pacc, fanf, fanc),2)
        nodo1.agregar_hijo(nodo2)
        
    if (pacc - 1 >= 0) and nodo1.dato[pacf][pacc - 1] != 1:
        hijo = [fila.copy() for fila in nodo1.dato] 
        hijo[pacf][pacc] = 0
        hijo[pacf][pacc - 1] = 2
        nodo2 = nodoA(hijo, distanciaEclidiana(pacf, pacc - 1, fanf, fanc),1)
        nodo1.agregar_hijo(nodo2)
    
    if (pacf + 1 <= 6) and nodo1.dato[pacf + 1][pacc] != 1:
        hijo = [fila.copy() for fila in nodo1.dato] 
        hijo[pacf][pacc] = 0
        hijo[pacf+1][pacc] = 2
        nodo2 = nodoA(hijo, distanciaEclidiana(pacf+1, pacc, fanf, fanc),2)
        nodo1.agregar_hijo(nodo2)
        
    if (pacc + 1 <= 7) and nodo1.dato[pacf][pacc+1] != 1:
        hijo = [fila.copy() for fila in nodo1.dato] 
        hijo[pacf][pacc] = 0
        hijo[pacf][pacc+1] = 2
        nodo2 = nodoA(hijo, distanciaEclidiana(pacf, pacc+1, fanf, fanc),1)
        nodo1.agregar_hijo(nodo2)
    
    
def a_estrella(nodo1,fanf,fanc):
    agenda = []  # Cola de prioridad (agenda)
    heapq.heappush(agenda, nodo1)  # Agregar nodo inicial
    explorados = set()  # Conjunto de nodos visitados

    while agenda:
        actual = heapq.heappop(agenda)  # Extraer nodo con menor f(n)

        # Condición de parada: si el primer nodo es la meta y los demás tienen costo mayor o igual
        if actual.dato == fin.dato and all(n.fn >= fin.fn for n in agenda):
            return actual  # Se encontró la solución óptima

        explorados.add(tuple(map(tuple, actual.dato)))  # Marcar nodo como explorado

        # Generamos los sucesores
        pacf, pacc = buscarPacman(actual.dato)  # Encuentra la posición del 2 en la matriz
        generacionEspacio(actual, pacf, pacc)

        for hijo in hijos:
            if tuple(map(tuple, hijo.dato)) not in explorados:
                heapq.heappush(agenda, hijo)  # Agregar sucesores a la agenda

    return None  # Si no encuentra solución
        
    