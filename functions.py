import networkx as nx
import matplotlib.pyplot as plt


def create_graph(nodes, edges):
    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    return g


def generate_adjacency_matrix(g):
    return nx.to_numpy_matrix(g)


def save_graph_to_file(graph, filename='plot.png'):
    plt.subplot(121)
    nx.draw(graph, pos=nx.circular_layout(graph), with_labels=True, font_weight="bold")
    plt.savefig(filename)
