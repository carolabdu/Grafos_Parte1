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


    def DFS(self,vi):
        self.marcados = [] #inicia vetor de marcação
        self.s = Stack() #cria pilha vazia
        self.s.push(vi)  #adiciona a raiz na fila
        self.pai = np.zeros([self.v]) #inicia vetor com os pais
        self.nivel = np.zeros([self.v]) #inicia vetor dos níveis
        self.pai[vi-1] = None #indica que não tem pai pois é raiz
        self.nivel[vi -1]= 0 #nivel da raiz é zero 
        while self.s.isEmpty()==False : #enquanto pilha não estiver vazia 
            u = self.s.peek() #pega vértice no topo da lista
            self.s.pop() #remover u da pilha 
            if u not in self.marcados: # (implemetar para ver se tá na lista): 
                self.marcados += [u] #adicionar vétice aos marcados
                for k in range(self.v): #para cada vizinho de u 
                    vizinho = self.matriz[u-1][k] #verificar se elemento da matriz é 1
                    if vizinho ==1: #ou seja se é vizinho de fato
                        self.s.push(k+1)  #botar na fila 
                        if k+1 not in self.marcados:  #se k ainda não foi marcado
                            self.pai[k] = u   #escrevre que u descobriu (vai mudando ao longo do algoritmo)
                            self.nivel[k] = self.nivel[u-1] + 1  #verifica o nível do pai de k e soma 1
        print('marcados:',self.marcados)
        print('pais:', self.pai)
        print('niveis:', self.nivel)    

    def BFS(self,vi):
        self.marked = [] #list with the nodes that are being or has already been explored
        self.Q = Queue() #Creates an empty Queue
        pai = np.zeros([self.v], dtype=int) #inicia vetor com os pais
        nivel = np.zeros([self.v],dtype=int) #inicia vetor dos níveis
        pai[vi-1] = 0 #indica que não tem pai pois é raiz
    
        self.marked.append(vi) #Marks the initial node(where we start the search)
        self.Q.add(vi) #Adds the firts node in the FIRTS POSITION of the Queue
        pai[vi-1] = 0 #indica que é raiz 
        while self.Q.is_empty() == False: #The search continues until the Queue is empty, when all the nodes have been explored
            v = self.Q.pop() #Removes the last node of the Queue, which is the older one and atributes to variable v
            for w in range(self.v): #para cada vizinho de v
                    vizinho = self.matriz[v-1][w] #verificar se elemento da matriz é 1
                    if vizinho ==1: #ou seja se é vizinho de fato #Explores all of v's neighbors and mark the ones who hasn't been explores
                        if w+1 not in self.marked: 
                            pai[w]= v #if w is not marked, it means the node that discovered it was v
                            nivel[w] = nivel[v-1]+1 #hanges the level of w
                            self.marked.append(w+1) #Marks w if it's not been discovered yet
                            self.Q.add(w+1) #Adds w to the first position of the Queue

        self.maxlevel = np.argmax(nivel)
        
        print('marcados:',self.marked)
        print('pais:', pai)
        print('niveis:', nivel) 
        print('maxleel:', self.maxlevel)  