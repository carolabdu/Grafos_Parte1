# Teoria-dos-Grafos

Essa biblioteca pode fornecer as seguintes informações em um arquivo de saída .txt:

1. Informações básica como:
     - Número de arestas do grafo
     - Número de vértices do grafo
     - Graus máximo e mínimo
     - Média dos graus
     - Mediana dos graus
2. Tipo de reprensentação (Lista ou Matriz de Adjacência)
3. Árvore de busca em largura(BFS) de determinado vértice
4. Árvore de busca em profundidade(DFS) de determinado vértice
5. A distância entre dois vértices especificados
6. O diâmetro do grafo
7. O número de componentes conexas, assim o número de vértices da maior e da menor

## Uso da biblioteca:

Para acessar as informações detalhadas acima, criamos um função 'infos_grafo', que possui como parâmetros:

- arq: O nome do arquivo sem a extensão
- representacao: 'L' para lista e 'M' para matriz 
- bfs=False: Um inteiro representando o vértice que se deseja obter a árvore geradora BFS
- dfs=False: Um inteiro representando o vértice que se deseja obter a árvore geradora DFS
- dist=False: Uma lista ou tupla com os vértices os quais se deseja saber a distância
- diameter=False: Se 'True' retorna o diamtro do grafo escolhido
- cc=False: Se 'True' retorna as informações das componentes conexas

Exmeplo de uso:
infos_grafo('grafo_1', 'L', 9, 2, (10,20), True, True)

