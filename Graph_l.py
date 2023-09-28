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
            g [u-1] += 1  #tualiza os graus 
            g [v-1] += 1
        self.graus = g
    
    def vertices(self,p):
        if p ==1:
            print(self.v)
        return(self.v)
    
    def arestas(self,p):
        a = int(np.sum(self.graus))/2
        if p==1:
            print(a)
        return a

    def mostra_lista(self):
        return (self.lista) 
    
    def grau(self):
        print (self.graus)

    def graumin(self,p):
        grau_min = np.min(self.graus)
        if p==1:
            print(grau_min)
        return grau_min

    def graumax(self,p):
        grau_max = np.max(self.graus)
        if p==1:
            print(grau_max)
        return grau_max
        
    def graumed(self,p):
        soma_graus = np.sum(self.graus)
        grau_med = (soma_graus/self.v)
        if p==1:
            print(grau_med)
        return grau_med

    def mediano(self,p):
        mediano = np.median(self.graus)
        if p==1: 
            print (int(mediano))
        return (int(mediano))


    def DFS(self,vi,p):
        self.marcados = np.zeros(self.v,dtype=int) #inicia vetor de marcação
        self.s = Stack() #cria pilha vazia
        self.s.push(vi)  #adiciona a raiz na fila
        pai = np.array([-1] * self.v, dtype = int) #inicia vetor com os pais
        nivel = np.array([-1] * self.v, dtype = int)#inicia vetor dos níveis
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
        
        self.DFStree = [pai, nivel]
        if p==1:
            print('pais:', pai, 'níveis', nivel)
        return (self.DFStree)  

    def BFS(self,vi,p):
        self.marked = np.zeros(self.v,dtype=int) #list with the nodes that are being or has already been explored
        self.Q = Queue() #Creates an empty Queue
        pai = np.array([-1] * self.v, dtype = int) #inicia vetor com os pais
        nivel = np.array([-1] * self.v, dtype = int) #inicia vetor dos níveis
        pai[vi-1] = 0 #indica que não tem pai pois é raiz
        nivel[vi -1] =0
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

        self.maxlevel = np.max(nivel)

        self.BFStree = [pai, nivel,self.maxlevel]
        if p==1:
            print('pais:', pai, 'níveis', nivel)
        return (self.BFStree)

    def distancia(self, v1, v2,p):
        self.BFS(v1,0)
        if self.BFStree[0][v2 -1] == -1: 
            distancia = 'infinita' #ou seja vértices não estão conectadas
        else: 
            distancia = self.BFStree[1][v2-1]
        if p==1:
            print(distancia)
        return distancia

    def diameter(self,p):  
        if self.v < 1000:
            diameter = 0
            for i in range(1,self.v):
                self.BFS(i,0)
                print(self.maxlevel)
                if self.maxlevel > diameter:
                    diameter = self.maxlevel
            if p==1:
                print(diameter)
            return diameter
        else: 
            for i in range(1000):
                vi = random.randint(1, self.v)
                diameter = 0
                self.BFS(vi,0)
                if self.maxlevel > diameter:
                    diameter = self.maxlevel
            if p==1:
                print(diameter)
            return diameter

    
    def cc(self,p):  #não testada e fazer uma função para ordenar 
        cc = []
        vistos = np.zeros(self.v,dtype=int)
        for vi in range(1,self.v +1):
            if vistos[vi-1] == 0:
                marcados = [[],0]  #retorna os marcados e o tamanho da cc
                pais_vi = self.BFS(vi,0)[0]
                for k in range(self.v):
                    if pais_vi[k] != -1:
                        vistos[k] = 1
                        marcados[0].append(k+1) #índice é uma unidade menor que o vétice
                        marcados[1] += 1
                cc.append(marcados)
        if p==1: 
            print(cc)
        return cc  
