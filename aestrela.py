from pyamaze import maze,agent
from queue import PriorityQueue

'''
Função base do algorítomo a* f(n) = g(n) - h(n)
    
    g(x): Representa a função de custo 
    h(x): Representa a heurística, custo que se tem até o fim 

'''

#Criando o mapa, e o "personagen"
mapa = maze(100,100)
mapa.CreateMaze(20,30 , loopPercent= 90) # mudando o destino final para ser na coordenada 20,30 e nível de dificuldade 60%

#desbravador = agent(mapa, 15,18, filled=True, footprints=True) # criando o personagem que vai explorar o mapa dando como parâmetros que nos mostram visualmente e seu spaw
desbravador = agent(mapa, filled=True, footprints=True)


destino = (20,30) # tem que ser o mesmo que colocar lá de cima 

# função para calcular o h(n) (Quantos passos faltam para chegar ao destino)
def h(posicao, destino):
    linha_posi = posicao[0]
    coluna_posi = posicao[1]

    linha_destino = destino[0]
    coluna_destino = destino[1]
    
    return abs(coluna_posi - coluna_destino) + abs(linha_posi-linha_destino) # abs para mostrar que é pra retornar valores absolutos

# função para calcular o a*
'''


Caminha a partir da primeira casa explorando os vizinhos 
    Só vai poder ir se: 
        Não ter parede
        Se não ter parede:
            Calcula o f(n) dos vizinhos
            Se o f(n_atual) < f(n_anterior):
                O f(n_atual) passa a ser o principal, substituindo o antigo é claro 
                Para escolher o caminho para seguir ele tem:
                    O menor f(n)
                    Se f(n) forem iguais, pega o que tiver menor h(n)
'''

def a_estrela(mapa):
    #Cria a labirinto com todos o f(n) com vvalores infinitos
    f = {posicao: float("inf") for posicao in mapa.grid}
    g = {}
    posicao_inicial = (mapa.rows, mapa.cols) # tem que ser a mesma posição incial do desbravador 

    #Calcula o valor do primeiro movimento 
    g[posicao_inicial] = 0
    f[posicao_inicial] = g[posicao_inicial] + h(posicao_inicial, destino)
    #print(f) 

    fila = PriorityQueue()
    item = (f[posicao_inicial], h(posicao_inicial, destino), posicao_inicial)
    fila.put(item)

    veio_de = {}
    veio_de[posicao_inicial] = None

    while not fila.empty():
        posicao = fila.get()[2]


        if posicao == destino:
            break

        for direcao in "NSEW":  #Mostra a posição e onde tá liberado para ir 
            if mapa.maze_map[posicao][direcao] == 1:
                linha_posicao = posicao[0]
                coluna_posicao = posicao[1]

                if direcao == "N":
                    proxima_posicao = (linha_posicao - 1, coluna_posicao)
                elif direcao == "S":
                    proxima_posicao = (linha_posicao +1, coluna_posicao)
                elif direcao == "W":
                    proxima_posicao = (linha_posicao , coluna_posicao -1)
                elif direcao == "E":
                    proxima_posicao = (linha_posicao, coluna_posicao +1)
                
                if proxima_posicao in mapa.grid:  # da uma conferida pra ver se não passa do limite do mapa 
                    novo_g = g[posicao] + 1
                    novo_f = novo_g + h(proxima_posicao, destino)
                

                    if novo_f < f[proxima_posicao]:
                        f[proxima_posicao] = novo_f
                        g[proxima_posicao] = novo_g
                        item = (novo_f, h(proxima_posicao, destino), proxima_posicao)
                        fila.put(item)
                        veio_de[proxima_posicao] = posicao



    #Construindo o percurso 
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






