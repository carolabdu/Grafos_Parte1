import numpy as np 
class Graph_m: #grafo em matriz 
    def __init__(self, v, a):
        self.v = v
        self.a = a
        self.matriz = np.zeros([self.v, self.v], dtype=int)
        for i in range(len(self.a)):
            v1= self.a[i][0]
            v2= self.a[i][1]
            self.matriz[v1-1][v2-1] = 1 #se os vértices estão conecatados 
            self.matriz[v2-1][v1-1]=1 #grafo não é direcionado, 'espelhamos' o resultado

    def vertices(self):
        return self.v

    def aresta(self):
        return len(self.a)
    
    def mostra_matriz(self):
        for i in range(self.v):
            print(self.matriz[i])    
    
    def grau (self):
        graus = np.sum(self.matriz, axis=0)
        print(graus)

    def graumin(self):
        graus = np.sum(self.matriz, axis=0)
        grau_min = np.argmin(graus)
        print(grau_min)

    def graumax(self):
        graus = np.sum(self.matriz, axis=0)
        grau_max = np.argmax(graus)
        print(grau_max)
        
    
    def graumed(self):
        graus = np.sum(self.matriz, axis=0)
        soma_graus = np.sum(np.sum(self.matriz, axis=0), axis=0)
        grau_med = (soma_graus/self.v)
        print(grau_med)
