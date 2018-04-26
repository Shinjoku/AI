from graph import Graph

# Variáveis
border = []
graph = Graph()

graph.create_matrix("in")

if ( graph.depth_search() ):
    print('Busca concluída com sucesso, destino encontrado.')
else:
    print('A busca falhou, o objetivo não foi encontrado.')
