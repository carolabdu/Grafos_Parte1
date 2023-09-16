class Graph: 
    def __init__(self, v, a): #adicionar tipo (lista ou matriz)):
        self.v = v
        self.a = a
        self.matriz = [[0]*self.v for i in range (self.v)]
        self.lista = [[] for i in range(self.v)] #não sabemos quantos elementos tem em cada linha
    

    def arestas_matriz(self, v1, v2):
        #resolver como fazer isso do arquivo
        self.matriz[v1-1][v2-1] = 1 #se os vértices estão conecatados 
        self.matriz[v2-1][v1-1]=1 #grafo não é direcionado, 'espelhamos' o resultado

    def contruir_matriz(self): #pegar do vetor que contém as arestas e botar na matriz
        for i in range(len(self.a)):
            self.arestas_matriz(self.a[i][0], self.a[i][1]) 
    
    def mostra_matriz(self):
        self.contruir_matriz()
        for i in range(self.v):
            print(self.matriz[i])     
         
    def arestas_lista(self, u, v):
        self.lista[u-1].append(v) #adicionar vértice v na linha u
        self.lista[v-1].append(u)

    def contruir_lista(self): #pegar do vetor que contém as arestas e botar na lista
        for i in range(len(self.a)):
            self.arestas_lista(self.a[i][0], self.a[i][1])  
    
    def mostra_lista(self):
        self.contruir_lista()  
        print (self.lista) 

def grau (self):
        self.contruir_lista()
        graus= [] #contruir lista com o grau de cada vértice
        for i in range(self.v):
            gi = len(self.lista[i])
            graus += [gi]
        
        graumin= self.v
        graumax = 0
        graumed =0
        mediana = 0  #ideia: botar graus em ordem e ver valor do meio
        gm=0
        for k in range(self.v):  #em uma iteração tentar resolver tdos os problemas
            if graus[k] < graumin:
                graumin = graus[k]
            if graus[k] > graumax:
                graumax = graus[k]
            gm += graus[k]  #talvez substituir por 2a/v
        graumed = gm/self.v

        print(graus)
        print("Grau mínimo:",graumin)
        print("Grau máximo:",graumax)
        print("Grau médio:", graumed)
        print("Grau mediano:",0)
    
    def saidas(self): #talvez tenha que criar outra classe pra saída
        print('Número de vértices', self.v)
        print("Número de arestas:", len(self.a))
        self.grau()
        self.mostra_lista
        self.mostra_matriz
