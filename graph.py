from colorama import init, Back, Style, Fore
import sys
import time


class Graph():

    # Variáveis
    terrain = []
    robot = 0
    dest = 0

    # Métodos
    def print_terrain(self):
        """
            Printa a matriz representativa do terreno
        """

        # Avalia o sistema e prepara o stdout para que a cor saia corretamente
        init(autoreset = True)

        # for i in range(10):
        #     sys.stdout.write( "\r{0}>".format("=" * i) )
        #     sys.stdout.flush()
        #     time.sleep(0.5)

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
        total = 0

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
        return total

    def print_path(self, path):
        for dict in path:
            for i in dict:
                print(i, end = ' ')
        print()


    def create_matrix(self, path):
        """
            Cria uma matriz, abrindo o arquivo e
                modificando a atual da classe
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
        print()
        print()

    def depth_search(self):
        """ Retorna True ao suceder, False ao falhar
            Realiza a busca em profundidade e calcula o custo total adquirido
                no caminho obtido.
        """

        # Inicialização das variáveis
        path = []
        view = []
        border = []
        passed = []
        total = 0

        # Inicio

        # Salva a posição inicial
        view.append( {'ORIGIN': 0} )
        border.append( [self.robot[0], self.robot[1]] )


        while( len(border) > 0 ):

            # Para cada item na lista de nos adjacentes
            noAtual = border.pop()
            path.append(view.pop())
            self.terrain[noAtual[0]][noAtual[1]] = 0

            # Verifica se eh o destino
            if(noAtual == self.dest):
                self.print_terrain()
                self.print_path(path)
                print('Tamanho borda: ', len(view))
                print('Custo total:', self.cost(path))
                return True

            else:

                i = noAtual[0]
                j = noAtual[1]

                if (j-1 in range(len(self.terrain)) and ( [i, j-1] not in passed )):
                    view.append( {'W': self.terrain[i][j-1] })
                    border.append([i, j-1])

                if (i+1 in range(len(self.terrain)) and ( [i+1, j] not in passed )):
                    view.append( {'S': self.terrain[i+1][j] })
                    border.append([i+1, j])

                if (j+1 in range(len(self.terrain)) and ( [i, j+1] not in passed )):
                    view.append( {'E': self.terrain[i][j+1] })
                    border.append([i, j+1])

                if (i-1 in range(len(self.terrain)) and ( [i-1, j] not in passed )):
                    view.append( {'N': self.terrain[i-1][j] })
                    border.append([i-1, j])

                passed.append(noAtual)

        return False



# End class Node
