class Graph_l: #Classe de grafos seguindo a representação de lista de adjacência
    def __init__(self, v, a): #(número de vértices, número de arestas)
        self.aqruivo_saida = [] #Lista que vai receber os resultados desejados
        self.v = v
        self.a = np.array(a)
        self.num_arestas = len(self.a) 
        self.lista = [[] for i in range(self.v)] #Não sabemos quantos elementos tem em cada linha (quantos vizinhos cada vértice tem)
        g = np.zeros(self.v,dtype=int) #Vetor de zeros, onde vamos guardar o grau de cada vértice
        for i in range(self.num_arestas):
            u=self.a[i][0] #Pega o primeiro vértice do par de arestas
            v= self.a[i][1] #Pega o segundo vértice do par de arestas
            self.lista[u-1].append(v) #Adiciona o vértice v na linha u (o índice é u-1, pois i se inicia no 0)
            self.lista[v-1].append(u) #Adiciona o vértice u na linha v
            g [u-1] += 1  #Atualiza os graus 
            g [v-1] += 1
        self.graus = g

    #Algumas funções possuem o padrão "p", que define se o resultado dele ser escrito no arquivo de saída ou não
    def vertices(self,p): #Retorna o número de vértices do grafo 
        if p ==1:
            self.arquivo_saida.append(f'\nNúmero de vértices: {self.v}')
        return self.v 
    
    def arestas(self,p): #Retorna o número de arestas do grafo
        a = int(np.sum(self.graus))/2 #Usamos a relação: Grau = 2*#Arestas
        if p==1:
            self.arquivo_saida.append(f'\nNúmero de arestas: {int(a)}')
        return a

    def mostra_lista(self): #Retorna a lista de adjacência
        return self.lista 
    
    def mostra_grau(self): #Retorna a lista de graus
        return self.graus

    def graumin(self,p): #Retorna o grau mínimo
        grau_min = np.min(self.graus)
        if p==1:
            self.arquivo_saida.append(f'\nGrau mínimo: {grau_min}')
        return grau_min

    def graumax(self,p): #Retorna o grau máximo
        grau_max = np.max(self.graus)
        if p==1:
            self.arquivo_saida.append(f'\nGrau máximo: {grau_max}')
        return grau_max
        
    def graumed(self,p): #Retorna a média dos graus
        grau_med = np.mean(self.graus)
        if p==1:
            self.arquivo_saida.append(f'\nGrau médio: {grau_med}')
        return grau_med

    def mediano(self,p):
        mediano = np.median(self.graus)
        if p==1: 
            self.arquivo_saida.append(f'\nMediana dos graus: {mediano}')
        return int(mediano)


    def DFS(self,vi,p): #Implementação da busca em profundidade
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
                        pai[k-1] = u   #escreve que u descobriu (vai mudando ao longo do algoritmo)
                        nivel[k-1] = nivel[u-1] + 1  #verifica o nível do pai de k e soma 1
        
        self.DFStree = [pai, nivel]
        if p==1:
            self.arquivo_saida.append(f'\nBusca DFS:\nPais: {pai}\nNíveis: {nivel}')
        return (self.DFStree)  

    def BFS(self,vi,p): #Implementação da busca em largura
        self.marcados = np.zeros(self.v,dtype=int) #Lista com os nós que já foram explorados
        self.Q = Queue() #Cria uma fila vazia
        pai = np.array([-1] * self.v, dtype = int) #inicia vetor com os pais
        nivel = np.array([-1] * self.v, dtype = int) #inicia vetor dos níveis
        nivel[vi -1] = 0
        self.marcados[vi-1]=1#Marca vi, que é o nó em que começamos a busca
        self.Q.add(vi) #Adciona o nó na fila
        pai[vi-1] = 0 #Indica que é raiz 
        while self.Q.is_empty() == False: #A busca continua até a lista ficar vazia(Até todos os vértices serem explorados)
            v = self.Q.pop() #Remove o último vértice da fila, que corresponde ao vértice mais antigo
            for w in self.lista[v-1]: #Visita os vizinhos de v
                if self.marcados[w-1]==0: 
                    pai[w-1]= v #Se w não tiver sido marcado, o vértice que o descobriu(seu pai) foi v
                    nivel[w-1] = nivel[v-1]+1 #Muda o nível atual para o nível de w
                    self.marcados[w-1]=1 #Marca w se não foi descoberto ainda
                    self.Q.add(w) #Adiciona w na primeira poição da fila

        self.maxlevel = np.max(nivel) #Pega o nível máximo

        self.BFStree = [pai, nivel, self.maxlevel] 
        if p==1:
            self.arquivo_saida.append(f'\nBusca BFS:\nPais: {pai}\nNíveis: {nivel}')
        return (self.BFStree)

    def distancia(self, v1, v2): #Retorna a distâncoa entre dois vértices
        self.BFS(v1) #Roda a BFS para o primeiro vértice
        if self.BFStree[0][v2 -1] == -1: #Checa se o segundo vértice está conectado ao primeiro(caso ele tenha um pai na BFStree, então os dois são conectados)
            distancia = 'infinita' #Ou seja vértices não estão conectadas
        else: 
            distancia = self.BFStree[1][v2-1] #O nível será a distância entre os vértices
        if p==1:
            self.arquivo_saida.append(f'\nDistância entre {v1} e {v2}: {distancia}')
        return distancia

    def diameter(self,p=0):  #Retorna o diãmetro do grafo
        if self.v < 1000: #Para otimizar o código, escolhemos 1000 vértices aleatórios de cada grafo para aproximar o diâmetro
            diameter = 0
            for i in range(1,self.v):
                self.BFS(i) #Roda a BFS para cada vértice
                #print(self.maxlevel)
                if self.maxlevel > diameter: #Procura o maior nível dentre os vértices, que será o diâmetro
                    diameter = self.maxlevel 
        else: 
            for i in range(1000):
                vi = random.randint(1, self.v)
                diameter = 0
                self.BFS(vi) #Roda a BFS para 1000 vértices aleatórios
                if self.maxlevel > diameter: #Procura o maior nível dentre os vértices, que será o diâmetro
                    diameter = self.maxlevel
        if p==1:
            self.arquivo_saida.append(f'\nDiâmetro do grafo: {diameter}')
        return diameter

    
    def cc(self,p):  #Retorna o número de componentes conexas, a maior componente e a menor
        cc = [] #Lista das componentes conexas
        vistos = np.zeros(self.v,dtype=int) #Array zerado para indicar se o vértice foi visto ou não
        for vi in range(1,self.v +1):
            if vistos[vi-1] == 0: 
                marcados = [[],0]  #Retorna os vértices da componente e o tamanho dela
                pais_vi = self.BFS(vi,0)[0] #Pega os pais de todos os vértices
                for k in range(self.v): 
                    if pais_vi[k] != -1: #Se o vértice tiver pai, ele está na componente conexa
                        vistos[k] = 1 #Altera o vetor definindo que o vértice foi visto
                        marcados[0].append(k+1) #Adiciona o vétice na lista de componentes conexas(índice é uma unidade menor que o vétice)
                        marcados[1] += 1 #Atualiza o número total de componentes
                cc.append(marcados[1]) #Adiciona as componentes à lista de componentes
        fim = np.asarray(cc)
        if p==1: 
            self.arquivo_saida.append(f'\nNúmero de componentes conexas no grafo: {len(fim)}\nMaior componente conexa: {np.max(fim)}\nMenor componente conexa: {np.min(fim)}')
        return cc   
