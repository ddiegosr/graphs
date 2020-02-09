import functions as fn

nodes = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]
graph = fn.create_graph(nodes, edges)
filename = 'graph.png'

fn.save_graph_to_file(graph, filename)
print('The generated graph for this example can be seen in {} file in this directory'.format(filename))

adjacency_matrix = fn.generate_adjacency_matrix(graph)
print('Adjacency Matrix can be seen below:')
print(adjacency_matrix)

