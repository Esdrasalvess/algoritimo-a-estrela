# Algoritimo-a-estrela
Trabalho desenvolvido para a Disciplina de Projeto e Análise de Algorítimos 

 Aplicação de Algoritmo de busca A* em problema do Labirinto


1st Esdrás A. Santos
Vitória da Conquista , Bahia
esdrasalvesdossantos2002@gmail.com

2nd Gabriel B. Anjos
Vitória da Conquista , Bahia
gabrielbarrosba@gmail.com

3rd José Henrique F. O. Soares
Vitória da Conquista , Bahia
jhferraz70@gmail.com

4th Luiz Felipe S. Carvalho
Vitória da Conquista , Bahia
lipecarvalholink@gmail.com

5th Rafael A. Santos
Vitória da Conquista , Bahia
rafaelowki@gmail.com


# Introdução

Os labirintos, presentes em diversas culturas e contextos desde o entretenimento até rituais religiosos, fascinam a humanidade há séculos. Segundo Algeo [1], um labirinto se define como um caminho complexo em forma de circuito que leva de um ponto de partida a um destino específico.

Resolver labirintos envolve encontrar o caminho que minimize um critério de custo, como distância ou tempo [2]. Na computação, esse problema é crucial em diversas áreas, como navegação de robôs autônomos, planejamento de rotas em sistemas de transporte e geração procedural de conteúdos em jogos.

Este estudo implementa e avalia o algoritmo A* (A-estrela), popular algoritmo de busca de caminho conhecido por sua eficiência, para solucionar o problema de busca em um armazém. O objetivo é que um agente inteligente (por exemplo, um robô de carga) se desloque de qualquer posição no armazém (labirinto) até a área de descarga, percorrendo o melhor caminho possível.

# Algoritmo A*

Algoritmos de busca operam em uma série de caminhos pré-definidos, buscando o caminho mais curto entre dois pontos específicos (A e B). Uma representação comum para esse tipo de problema é através de grafos, onde os vértices representam os pontos de interesse e as arestas os caminhos que os conectam. Labirintos também podem ser utilizados, com o caminho a ser percorrido delimitado pelas paredes.

Para funcionar, os algoritmos de busca necessitam de três elementos principais: um ponto inicial, um ponto final e um caminho já conhecido. Ao conhecer todos os estados e elementos de um sistema e como ele se comporta, podemos descrevê-lo logicamente e recriá-lo por meio de algoritmos.

A busca escolhida para este trabalho foi o A*, que combina o algoritmo de busca em largura (Breadth First Search) com a aproximação de funções heurísticas. Estas funções avaliam os estados de um problema combinando uma função que verifica o custo para alcançar cada estado, com outra que verifica o custo para ir do estado atual (n) até o estado objetivo [3].

A função heurística de A* é definida como: f(n) = g(n) + h(n)

Onde:

    g(n) representa o custo do caminho desde o estado inicial até o estado atual (n).
    h(n) representa o custo estimado do caminho de menor custo desde o estado atual (n) até o estado objetivo.

Assim, para encontrar a solução de menor custo, exploramos primeiro o nó com o menor valor de f(n) + h(n).

Desde que a função heurística h(n) satisfaça certas condições e seja admissível, a busca A* será completa e ótima. Como g(n) é o custo exato para alcançar n, então f(n) nunca irá superestimar o custo real de uma solução passando por n.

O algoritmo A* se mostra ideal para este estudo, que busca resolver o problema de um labirinto onde o objetivo é minimizar o custo de deslocamento de um ponto inicial (A) para um ponto final (B). Sua finalidade é a busca entre vértices em grafos, baseada em funções heurísticas que retornam o menor custo de deslocamento de um ponto de origem até o destino.

# Metodologia

O algoritmo A* foi implementado na linguagem de programação Python, utilizando a biblioteca pyamaze para facilitar a criação e visualização do labirinto.

Para obter uma representação gráfica do caminho percorrido pelo algoritmo no labirinto, foi aplicado o parâmetro footprints = True, demonstrando a visualização prática do algoritmo. À medida que o agente se move pelo labirinto, ele deixa "pegadas", permitindo a visualização do caminho percorrido.

O pseudocódigo do algoritmo A* pode ser descrito da seguinte forma:

Caminha a partir da primeira casa explorando os vizinhos >
Só vai poder ir se: >
   Não ter parede >
   Se não ter parede: >
       Calcula o f(n) dos vizinhos >
       Se o f(n_atual) < f(n_anterior): >
          O f(n_atual) passa a ser o principal, substituindo o antigo é claro >
          Para escolher o caminho para seguir ele tem: >
             O menor f(n)

                    
No entanto, o projeto pode ser facilmente adaptado às necessidades do usuário, permitindo a modificação de diversos parâmetros, como tamanho do mapa, posição de destino.


# Referências
[1] ALGEO, J. The Laburinth: A Brief Introduction to its History, Meaning and Use. 2001.
[2] L. da S. Costa and F. Tonidandel, "Análise de Algoritmos de Path-Planning," in *Proceedings of the Semana de Iniciação Científica da FEI (SICFEI)*, São Bernardo do Campo, Brazil, 2018, pp. 1-6. [Online]. Available: https://fei.edu.br/sites/sicfei/2018/cc/SICFEI_2018_paper_61.pdf. [Accessed: Jun. 12, 2024].
[3] RUSSELL, Stuart J.; NORVIG, Peter; Inteligência artificial. Rio de Janeiro, Elsevier, 1021p. 2004. 

