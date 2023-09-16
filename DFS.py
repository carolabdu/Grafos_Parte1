
class DFS(Graph,Stack):
    def __init__(self, v, a, vi):
        super().__init__(v, a) #herda vertices e arestas do grafo
        self.vi= vi #vétice que começaremos a busca
        self.marcados = [] *inicia vetor de marcação
        self.s = Stack() #cria pilha vazia
        self.s.push(self.vi)  #adiciona a raiz na fila
        self.contruir_lista() #usa matriz de adjacência para verificar os vizinhos quando for adicionar na pilha
        self.pai = [0]*self.v #inicia vetor com os pais
        self.nivel = [0]*self.v  #inicia vetor com os níveis 

    def algoritmo(self):  #faz a busca e constrói árvres simultaneamete 
        # print(self.vi)
        # print(self.pai)
        self.pai[self.vi-1] = 'é raiz' #indica que não tem pai pois é raiz
        self.nivel[self.vi -1]= 0 #niel da raiz é zero 
        while self.s.isEmpty()==False : #enquanto pilha não estiver vazia 
            u = self.s.peek() #pega vértice no topo da lista
            #print(u)
            self.s.pop() #remover u da pilha 
            if u not in self.marcados: # (implemetar para ver se tá na lista): 
                self.marcados += [u] #adicionar vétice aos marcados
                for k in self.lista[u-1]: #para cada vizinho de u 
                    self.s.push(k)  #botar na fila 
                    if k not in self.marcados:  #se k ainda não foi marcado
                        self.pai[k-1] = u   #escrevre que u descobriu (vai mudando ao longo do algoritmo)
                        self.nivel[k-1] = self.nivel[u-1] + 1  #verifica o nível do pai de k e soma 1
            # print('pilha:',self.s.items)
        print('marcados:',self.marcados)
        print('pais:', self.pai)
        print('niveis:', self.nivel)                 

    
    def mostra_arvore(self):   #imprimir resultado desejado
        self.algoritmo()
