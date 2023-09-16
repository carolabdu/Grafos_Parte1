
class DFS(Graph,Stack):
    def __init__(self, v, a, vi):
        super().__init__(v, a)
        self.vi= vi #vétice que começaremos a busca
        self.marcados = []
        self.s = Stack()
        self.s.push(self.vi)
        self.contruir_lista()

    def algoritmo(self):
        while self.s.isEmpty()==False :
            u = self.s.peek() #pega vértice no topo da lista 
            self.s.pop() #remover u da pilha 
            if u not in self.marcados: # (implemetar para ver se tá na lista): 
                self.marcados += [u]
                for k in self.lista[u-1]:
                    self.s.push(k)

    
    def mostra_marcados(self):
        self.algoritmo()
        print(self.marcados)

