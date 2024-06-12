from pyamaze import maze,agent
from queue import PriorityQueue

'''
Função base do algorítomo a* f(n) = g(n) - h(n)
    
    g(x): Representa a função de custo 
    h(x): Representa a heurística, custo que se tem até o fim 

'''
# Pedindo a linha e coluna do ponto de partida 
cord_x_str = input("digite a linha: ")
cord_x = int(cord_x_str)

cord_y_str = input("digite a coluna: ")
cord_y = int(cord_y_str)

#Inicializando o mapa,chama o mapa salvo  cria  o "personagen"
mapa = maze(11,11)
mapa.CreateMaze(1,6, loadMaze="maze--2024-06-12--10-14-55.csv")  

desbravador = agent(mapa, cord_x,cord_y, filled=True, footprints=True)


destino = (1,6) # tem que ser o mesmo que colocar lá de cima 

# função para calcular o h(n) (Quantos passos faltam para chegar ao destino)
def h(posicao, destino):
    linha_posi = posicao[0]
    coluna_posi = posicao[1]

    linha_destino = destino[0]
    coluna_destino = destino[1]
    
    return abs(coluna_posi - coluna_destino) + abs(linha_posi-linha_destino) # abs para mostrar que é pra retornar valores absolutos

# função para calcular o a*


def a_estrela(mapa):
    # Cria o labirinto com todos os f(n) com valores infinitos
    f = {posicao: float("inf") for posicao in mapa.grid}
    g = {}
    posicao_inicial = (cord_x, cord_y)

    # Calcula o valor do primeiro movimento
    g[posicao_inicial] = 0
    f[posicao_inicial] = g[posicao_inicial] + h(posicao_inicial, destino)

    fila = PriorityQueue()
    item = (f[posicao_inicial], h(posicao_inicial, destino), posicao_inicial)
    fila.put(item)

    veio_de = {}
    veio_de[posicao_inicial] = None

    while not fila.empty():
        posicao = fila.get()[2]

        if posicao == destino:
            break

        for direcao in "NSEW":
            linha_posicao = posicao[0]
            coluna_posicao = posicao[1]

            if direcao == "N":
                proxima_posicao = (linha_posicao - 1, coluna_posicao)
            elif direcao == "S":
                proxima_posicao = (linha_posicao + 1, coluna_posicao)
            elif direcao == "W":
                proxima_posicao = (linha_posicao, coluna_posicao - 1)
            elif direcao == "E":
                proxima_posicao = (linha_posicao, coluna_posicao + 1)

            if proxima_posicao in mapa.grid and mapa.maze_map[posicao][direcao] != 0:
                novo_g = g[posicao] + 1
                novo_f = novo_g + h(proxima_posicao, destino)

                if novo_f < f.get(proxima_posicao, float("inf")):
                    f[proxima_posicao] = novo_f
                    g[proxima_posicao] = novo_g
                    item = (novo_f, h(proxima_posicao, destino), proxima_posicao)
                    fila.put(item)
                    veio_de[proxima_posicao] = posicao

    # Construindo o percurso
    percurso = []
    posicao = destino
    while posicao:
        percurso.append(posicao)
        posicao = veio_de[posicao]
    percurso.reverse()

    return percurso
 



percurso = a_estrela(mapa)
mapa.tracePath({desbravador: percurso}, delay=100)
mapa.run()






