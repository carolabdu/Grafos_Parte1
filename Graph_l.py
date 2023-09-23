class Graph_l:
    def __init__(self, v, a):
        self.v = v
        self.a = a
        self.num_arestas = len(self.a)
        self.lista = [[] for i in range(self.v)] #não sabemos quantos elementos tem em cada linha
        g = np.zeros(self.v,dtype=int)
        for i in range(self.num_arestas):
            u=self.a[i][0]
            v= self.a[i][1]
            self.lista[u-1].append(v) #adicionar vértice v na linha u
            self.lista[v-1].append(u)
            g [u-1] += 1
            g [v-1] += 1
        self.graus = g
    
    def vertices(self):
        return(sef.v)
    
    def arestas(self):
        a = int(np.sum(self.graus))/2
        return a

    def mostra_lista(self):
        return (self.lista) 
    
    def grau(self):
        print (self.graus)

    def graumin(self):
        grau_min = np.argmin(self.graus)
        print(grau_min)

    def graumax(self):
        grau_max = np.argmax(self.graus)
        print(grau_max)
        
    def graumed(self):
        soma_graus = np.sum(self.graus)
        grau_med = (soma_graus/self.v)
        print(grau_med)

    def mediano(self):
        mediano = np.median(self.graus)
        print (int(mediano))


    def DFS(self,vi):
        self.marcados = np.zeros(self.v,dtype=int) #inicia vetor de marcação
        self.s = Stack() #cria pilha vazia
        self.s.push(vi)  #adiciona a raiz na fila
        pai = np.zeros([self.v], dtype=int) #inicia vetor com os pais
        nivel = np.zeros([self.v],dtype=int) #inicia vetor dos níveis
        pai[vi-1] = 0 #indica que não tem pai pois é raiz
        nivel[vi -1]= 0 #nivel da raiz é zero 
        while self.s.isEmpty()==False : #enquanto pilha não estiver vazia 
            u = self.s.peek() #pega vértice no topo da lista
            self.s.pop() #remover u da pilha 
            if self.marcados[u-1]==0: # (implemetar para ver se tá na lista): 
                self.marcados[u-1]=1 #adicionar vétice aos marcados
                for k in self.lista[u-1]: #para cada vizinho de u 
                    self.s.push(k)  #botar na fila 
                    if self.marcados[k-1]==0:  #se k ainda não foi marcado
                        pai[k-1] = u   #escrevre que u descobriu (vai mudando ao longo do algoritmo)
                        nivel[k-1] = nivel[u-1] + 1  #verifica o nível do pai de k e soma 1
        print('marcados:',self.marcados)
        print('pais:', pai)
        print('niveis:', nivel)  

    def BFS(self,vi):
        self.marked = np.zeros(self.v,dtype=int) #list with the nodes that are being or has already been explored
        self.Q = Queue() #Creates an empty Queue
        pai = np.zeros([self.v], dtype=int) #inicia vetor com os pais
        nivel = np.zeros([self.v],dtype=int) #inicia vetor dos níveis
        pai[vi-1] = 0 #indica que não tem pai pois é raiz
        self.marked[vi-1]=1#Marks the initial node(where we start the search)
        self.Q.add(vi) #Adds the firts node in the FIRTS POSITION of the Queue
        pai[vi-1] = 0 #indica que é raiz 
        while self.Q.is_empty() == False: #The search continues until the Queue is empty, when all the nodes have been explored
            v = self.Q.pop() #Removes the last node of the Queue, which is the older one and atributes to variable v
            for w in self.lista[v-1]: #para cada vizinho de v
                if self.marked[w-1]==0: 
                    pai[w-1]= v #if w is not marked, it means the node that discovered it was v
                    nivel[w-1] = nivel[v-1]+1 #hanges the level of w
                    self.marked[w-1]=1 #Marks w if it's not been discovered yet
                    self.Q.add(w) #Adds w to the first position of the Queue

        self.maxlevel = np.argmax(nivel)

        print('marcados:',self.marked)
        print('pais:', pai)
        print('niveis:', nivel) 
        print('maxleel:', self.maxlevel)  
