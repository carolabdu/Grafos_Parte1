
with open('grafo_n.txt', 'r') as arquivo:
        texto = [int(vertice) for vertice in arquivo.read().split() if vertice.isdigit()] #Cria uma lista com o conteúdo presente no arquivo de teste
        vertices = texto[0] #Pega o primeiro elemento da lista acima, que correnspode ao número de vértices do grafo
        arestas = [] #Lista vazia que vai conter todos os pares de arestas do grafo
        for i in range(len(texto[1:])//2):
            arestas += [texto[2*i+1:2*i+3]] #Atualiza a lista de arestas, criando sublistas com os pares de arestas
#print (arestas)
