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
