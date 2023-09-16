
class DFS(Graph,Stack):
    def __init__(self, v, a, vi):
        super().__init__(v, a)
        self.vi= vi #vétice que começaremos a busca
        self.marcados = []
        self.s = Stack()
        self.s.push(self.vi)

    def algoritmo():
        while self.s != []:
            u = self.s.peek() #pega vértice no topo da lista 
            self.s.pop() #remove u da pilha 
            if u not in self.marcados: # (implemetar para ver se tá na lista): 
                self.marcados += [u]
                #Para cada aresta (u,v) incidente a u
                #Adicionar v em P // no topo


