import networkx as nx
import matplotlib.pyplot as plt


def key_func(item):
    return len(item)


def get_sequence_order(graph):
    bordas = []
    # PEGA AS EXTREMIDADES DO GRAFO
    for node in graph.nodes:
        grau_do_no = len(G.adj[node])
        if grau_do_no == 1:
            # É EXTREMIDADE DO GRAFO
            bordas.append(node)
    # print(bordas)

    origem = bordas[0]
    destinos = bordas[1:]

    caminhos = nx.all_simple_paths(G=graph, source=origem, target=destinos)

    # ORDENAR CAMINHOS POR TAMANHO
    # ordenar as sequencias do menor para o maior caminho
    path_matrix = []
    for i, caminho in enumerate(caminhos):
        lista = list(caminho)
        # print(caminho)
        # print(lista)
        path_matrix.append(lista)
    # print(path_matrix)

    # ORDENA A MATRIZ POR TAMANHO
    path_matrix.sort(key=key_func)

    # print(path_matrix)

    # MONTAR LISTA TOTAL
    # adiciona a lista os nos na sequencia percorrendo os caminhos para cada nó novo.
    sequence_order = []
    for caminho in path_matrix:
        for node in caminho:
            if node not in sequence_order:
                sequence_order.append(node)
    print("ordem de sequencia")
    return sequence_order


G = nx.Graph()

G.add_edge(1, 2)
G.add_edge(1, 2)
G.add_edge(2, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(3, 6)
G.add_edge(5, 7)
G.add_edge(8, 4)
G.add_edge(8, 9)
G.add_edge(9, 10)

sequencia = get_sequence_order(G)
print(sequencia)

# IMPRIMIR O GRAFO
plt.figure(1)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()

