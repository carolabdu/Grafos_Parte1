
import time
import psutil
import random
import sys

#Questão 1
MB = 1048576
#Matriz de Adjacencia
mem_antes_matriz = psutil.virtual_memory()._asdict()['available']
grafo_matriz = Graph_m(nodes, edges)
mem_depois_matriz = psutil.virtual_memory()._asdict()['available']
consumo_matriz = mem_antes_matriz - mem_depois_matriz
print('Memória utilizada pela matriz:', consumo_matriz/MB, 'Megabytes')

# Lista de Adjacencia
mem_antes_lista = psutil.virtual_memory()._asdict()['available']
grafo_lista = Graph_l(nodes,edges)
mem_depois_lista = psutil.virtual_memory()._asdict()['available']
consumo_lista = mem_antes_lista - mem_depois_lista
print('Memória utilizada pela lista:', consumo_lista/MB, 'Megabytes')

grau_max= grafo_lista.graumax(0)
grau_min= grafo_lista.graumin(0)
grau_medio= grafo_lista.graumed(0)
grau_mediano= grafo_lista.mediano(0)
print (f'Grau médio = {grau_medio} \n Grau mediano = {grau_mediano} \n Grau máximo = {grau_max} \n Grau mínimo = {grau_min}\n')

numero_vertices = grafo_lista.vertices(0)
numero_arestas = grafo_lista.arestas(0)
print (f'Número de arestas = {numero_arestas} \n Número de vértices = {numero_vertices}')



#Questão 2 e 3:

busca_matriz_largura= 0
busca_lista_largura = 0
busca_matriz_profundidade = 0
busca_lista_profundidade = 0

for i in range(1000):
    vertice = random.randint(1,grafo_lista.v)
    
    inicio_matriz_l = time.time()
    grafo_matriz.BFS(vertice,0)
    fim_matriz_l = time.time()

    inicio_matriz_p = time.time()
    grafo_matriz.DFS(vertice,0)
    fim_matriz_p = time.time()

    inicio_lista_l = time.time()
    grafo_lista.BFS(vertice,0)
    fim_lista_l = time.time()

    inicio_lista_p = time.time()
    grafo_lista.DFS(vertice,0)
    fim_lista_p = time.time()
    
    busca_matriz_largura += fim_matriz_l - inicio_matriz_l
    busca_lista_largura += fim_lista_l - inicio_lista_l
    busca_matriz_profundidade += fim_matriz_p - inicio_matriz_p
    busca_lista_profundidade += fim_lista_p - inicio_lista_p
   

print(f'Tempo médio de busca largura matriz = {busca_matriz_largura/1000} segundos')
print(f'Tempo médio de busca largura lista = {busca_lista_largura/1000} segundos')
print(f'Tempo médio de busca profundidade matriz = {busca_matriz_profundidade/1000} segundos')
print(f'Tempo médio de busca profundidade lista = {busca_lista_profundidade/1000} segundos')


#Questão 4:

pais1_bfs = grafo_matriz.BFS(1,0)[0]
pais2_bfs = grafo_matriz.BFS(2,0)[0]
pais3_bfs = grafo_matriz.BFS(3,0)[0]
print(f'BFS no 1: Pai do 10: {pais1_bfs[10-1]} - Pai do 20: {pais1_bfs[20-1]} - Pai do 30: {pais1_bfs[30-1]}')
print(f'BFS no 2: Pai do 10: {pais2_bfs[10-1]} - Pai do 20: {pais2_bfs[20-1]} - Pai do 30: {pais2_bfs[30-1]}')
print(f'BFS no 3: Pai do 10: {pais3_bfs[10-1]} - Pai do 20: {pais3_bfs[20-1]} - Pai do 30: {pais3_bfs[30-1]}')

pais1_dfs = grafo_matriz.DFS(1,0)[0]
pais2_dfs = grafo_matriz.DFS(2,0)[0]
pais3_dfs = grafo_matriz.DFS(3,0)[0]
print(f'DFS_matriz no 1: Pai do 10: {pais1_dfs[10-1]} - Pai do 20: {pais1_dfs[20-1]} - Pai do 30: {pais1_dfs[30-1]}')
print(f'DFS_matriz no 2: Pai do 10: {pais2_dfs[10-1]} - Pai do 20: {pais2_dfs[20-1]} - Pai do 30: {pais2_dfs[30-1]}')
print(f'DFS_matriz no 3: Pai do 10: {pais3_dfs[10-1]} - Pai do 20: {pais3_dfs[20-1]} - Pai do 30: {pais3_dfs[30-1]}')

pais1_bfs = grafo_lista.BFS(1,0)[0]
pais2_bfs = grafo_lista.BFS(2,0)[0]
pais3_bfs = grafo_lista.BFS(3,0)[0]
print(f'BFS_lista no 1: Pai do 10: {pais1_bfs[10-1]} - Pai do 20: {pais1_bfs[20-1]} - Pai do 30: {pais1_bfs[30-1]}')
print(f'BFS_lista no 2: Pai do 10: {pais2_bfs[10-1]} - Pai do 20: {pais2_bfs[20-1]} - Pai do 30: {pais2_bfs[30-1]}')
print(f'BFS_lista no 3: Pai do 10: {pais3_bfs[10-1]} - Pai do 20: {pais3_bfs[20-1]} - Pai do 30: {pais3_bfs[30-1]}')

pais1_dfs = grafo_lista.DFS(1,0)[0]
pais2_dfs = grafo_lista.DFS(2,0)[0]
pais3_dfs = grafo_lista.DFS(3,0)[0]
print(f'DFS_lista no 1: Pai do 10: {pais1_dfs[10-1]} - Pai do 20: {pais1_dfs[20-1]} - Pai do 30: {pais1_dfs[30-1]}')
print(f'DFS_lista no 2: Pai do 10: {pais2_dfs[10-1]} - Pai do 20: {pais2_dfs[20-1]} - Pai do 30: {pais2_dfs[30-1]}')
print(f'DFS_lista no 3: Pai do 10: {pais3_dfs[10-1]} - Pai do 20: {pais3_dfs[20-1]} - Pai do 30: {pais3_dfs[30-1]}')


#Questão 5:
distancia10_20 = grafo_matriz.distancia(10,20,0)
distancia10_30 = grafo_matriz.distancia(20,30,0)
distancia20_30 = grafo_matriz.distancia(20,30,0)

distancia10_20l = grafo_lista.distancia(10,20,0)
distancia10_30l = grafo_lista.distancia(20,30,0)
distancia20_30l = grafo_lista.distancia(20,30,0)

print(f'Matriz : (10,20) = {distancia10_20} - (10,30) = {distancia10_30} - (20,30) = {distancia20_30}\n') 
print(f'Lista : (10,20) = {distancia10_20l} - (10,30) = {distancia10_30l} - (20,30) = {distancia20_30l}')


#Questão 6:
grafo_matriz.cc(1)
grafo_lista.cc(1)



#Questão 7:
diametro_lista = grafo_lista.diameter(1)
#print(f'{diametro_lista}')
