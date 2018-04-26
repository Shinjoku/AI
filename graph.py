from colorama import init, Back, Style, Fore        # Classes relativas ao letreiro do terminal / cmd
import sys                                          # Classe relativa aos recursos gerais do sistema
import time                                         # Classe relativa aos recursos temporizadores do sistema


class Graph():
    """
        Classe respectiva ao 'grafo' que será analisado
    """

    # Variáveis
    terrain = []    # Irá conter o terreno
    robot = 0       # Irá conter a posição do robô
    dest = 0        # Irá conter a posição do destino

    # Métodos
    def print_terrain(self):
        """ Não tem retorno
            Printa a matriz representativa do terreno
        """

        # Avalia o sistema e prepara o stdout para que a cor saia corretamente
        init(autoreset = True)

        # Define uma cor específica para cada valor da matriz
        for i in range(42):
            for j in range (42):
                if( self.terrain[i][j] == 0 ):
                    print( Back.CYAN +  Fore.BLACK + '|   ', end = '')
                if( self.terrain[i][j] == 1 ):
                    print( Back.GREEN + Fore.BLACK + '|   ', end = '' )
                if( self.terrain[i][j] == 2 ):
                    print( Back.YELLOW + Fore.BLACK + '|   ', end = '')
                if( self.terrain[i][j] == 3 ):
                    print( Back.BLUE + Fore.BLACK + '|   ', end = '')
                if( self.terrain[i][j] == 4 ):
                    print( Back.RED + Fore.BLACK + '|   ', end = '')
                if( self.terrain[i][j] == 5 ):
                    print( Back.MAGENTA + Fore.BLACK + '|   ', end = '')
            print ('\n')

    def cost(self, path):
        """ Retorna um inteiro
            Realiza a soma dos valores de cada chave, dado um dicionário,
                já convertendo de acordo com as equivalências do projeto,
                sendo essas:
                    1 - 1
                    2 - 5
                    3 - 10
                    4 - 15
        """

        # Inicializa o somatório como 0
        total = 0

        # Percorre o dicionário identificando os valores das chaves e fazendo a soma
        for dict in path:
            for i in dict.keys():
                if ( dict[i] == 1 ):
                    total += 1
                if ( dict[i] == 2):
                    total += 5
                if ( dict[i] == 3):
                    total += 10
                if ( dict[i] == 4):
                    total += 15
        return total            # Retorna o total acumulado na busca


    def print_path(self, path):
        """ Não tem retorno
            Exibe o caminho que foi obtido com a busca
        """

        for dict in path:           # Para cada dicionário em path
            for i in dict:          # Para cada item do dicionário
                print(i, end = ' ') # Exibe o nome do item
        print()                     # Exibe uma linha em branco


    def create_matrix(self, path):
        """ Não tem retorno
            Cria uma matriz, abrindo o arquivo e
                modificando o terreno atual da classe
        """

        # Abre o arquivo de entrada, que deve estar localizado na mesma pasta
        graph = open(path, "r")

        # Coleta a posição inicial do robô
        self.robot = graph.readline().split(',')
        self.robot = list(map(int, self.robot))

        # Coleta a posição do destino
        self.dest = graph.readline().split(',')
        self.dest = list(map(int, self.dest))

        # Coleta a matriz que representa o terreno,
        #   com tratamento de string para evitar '\n'
        for i in range (42):
            self.terrain.append(
                graph
                .readline()
                .rstrip()
            )
            self.terrain[i] = self.terrain[i].split(',')
            self.terrain[i] = list(map(int, self.terrain[i]))

        # Define um valor inicial para identificar o robô na matriz
        self.terrain[self.robot[0]][self.robot[1]] = 0

        # Define um valor inicial para identificar o destino
        self.terrain[self.dest[0]][self.dest[1]] = 5

        # Printa o terreno
        self.print_terrain()
        print()
        print()


    def depth_search(self):
        """ Retorna True ao suceder, False ao falhar
            Realiza a busca em profundidade e calcula o custo total adquirido
                no caminho obtido.
        """

        # Inicialização das variáveis
        path = []       # Irá conter o caminho percorrido
        view = []       # Irá conter o que está em vista para ser buscado
        border = []     # Irá conter a borda do algoritmo
        passed = []     # Irá conter as posições já percorridas

        # Inicio da busca

        # Salva a posição inicial
        view.append( {'ORIGIN': 0} )
        border.append( [self.robot[0], self.robot[1]] )

        # Enquanto houver 'nós' a serem percorridos
        while( len(border) > 0 ):

            # Remove o último nó da lista para ser avaliado
            noAtual = border.pop()

            # Remove o nó que está sendo avaliado para ser levado ao caminho,
            #   pois está sendo percorrido
            path.append(view.pop())

            # Seta o valor do terreno como 0, pois já está sendo percorrido
            self.terrain[noAtual[0]][noAtual[1]] = 0

            # Verifica se é o destino
            if(noAtual == self.dest):
                self.print_terrain()
                self.print_path(path)
                print('Custo total:', self.cost(path))
                return True         # Sucesso na busca

            # Se não for o destino
            else:

                # Guarda a posição atual para simplificar citações futuras
                i = noAtual[0]
                j = noAtual[1]

                # Procura vizinho ao oeste, se for possível
                # Está primeiro para que tenha a menor prioridade
                if (j-1 in range(len(self.terrain)) and ( [i, j-1] not in passed )):
                    view.append( {'W': self.terrain[i][j-1] })
                    border.append([i, j-1])

                # Procura vizinho ao Sul, se for possível
                # Tem uma prioridade maior que o Oeste
                if (i+1 in range(len(self.terrain)) and ( [i+1, j] not in passed )):
                    view.append( {'S': self.terrain[i+1][j] })
                    border.append([i+1, j])

                # Procura vizinho ao Leste, se for possível
                # Tem prioridade maior que o Sul
                if (j+1 in range(len(self.terrain)) and ( [i, j+1] not in passed )):
                    view.append( {'E': self.terrain[i][j+1] })
                    border.append([i, j+1])

                # Procura vizinho ao Norte, se for possível
                # Tem a maior prioridade de todos
                if (i-1 in range(len(self.terrain)) and ( [i-1, j] not in passed )):
                    view.append( {'N': self.terrain[i-1][j] })
                    border.append([i-1, j])

                # Nó atual é levado à lista de nós já visitados
                passed.append(noAtual)

            print('\n')
            self.print_terrain()
        return False            # Falha na busca

# Fim da classe Graph
