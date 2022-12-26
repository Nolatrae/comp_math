import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

with open("input.txt", "r") as f:
    peaks = int(f.readline().rstrip())
    all_edge = []
    for line in f.readlines():
        line_arr = [int(i) for i in line.split()]
        all_edge += [line_arr[0]] + [line_arr[1]]
        G.add_edge(*(tuple(line_arr)))

for i in range(1, peaks + 1):
    if not (i in all_edge):
        G.add_node(*(tuple([i])))

print(G.number_of_nodes() - G.number_of_edges() - 1)

nx.draw(G, with_labels=True)

plt.show()
