class Graph():

    # Variables
    terrain = []
    robot = 0
    dest = 0

    # Methods
    def print_terrain(self):
        """
            Printa a matriz representativa do terreno
        """

        for i in range (42):
            for j in range (42):
                print (self.terrain[i][j], ' ', end='')
            print ('\n')


    def create_matrix(self, path):
        """
            Cria uma matriz, abrindo o arquivo e
                modificando a atual da classe
        """

        graph = open(path, "r")

        self.robot = graph.readline().split(',')
        self.robot = list(map(int, self.robot))

        self.dest = graph.readline().split(',')
        self.dest = list(map(int, self.dest))

        print (self.robot, self.dest)

        for i in range (42):
            self.terrain.append(
                graph
                .readline()
                .rstrip()
            )
            self.terrain[i] = self.terrain[i].split(',')
            self.terrain[i] = list(map(int, self.terrain[i]))

        self.terrain[self.robot[0]][self.robot[1]] = 0

        self.terrain[self.dest[0]][self.dest[1]] = 5

        self.print_terrain()


    """def depth_search(self, vi, cost):

    	menorCusto = 9999999
    	melhorCaminho = ""
        border = []
        axis = []

        # Inicio
    	border.append({'ORIGIN': 0})

    	while(border.length):
            # Para cada item na lista de nos adjacentes
    		node = self.border.remove()
            auxAxis = axis.remove()

            # Verifica se eh o destino
    		if(auxAxis == self.dest):
    			if(node.y < menorCusto):
    				menorCusto = node.y
    				melhorCaminho = node.x

    		else:
                if (i < self.terrain.length):
                    border.append({'N': self.terrain[i+1][j]})
                    axis.append((i+1, j))

                if (j < self.terrain.length):
                    border.append({'W': self.terrain[i][j+1]})
                    axis.append((i, j+1))


    	print (melhorCaminho, menorCusto)
"""

# End class Node
