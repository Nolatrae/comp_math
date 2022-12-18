import networkx as nx
from matplotlib import pyplot as plt
from itertools import product

def find_way(counter):
  x = []
  for i in range(len(counter)):
    x.append(i+1)
  return x

def getModa(counter):#Находим моду
  moda = 0
  max = 0
  sum = 0
  for i in range(len(counter)):
      sum += counter[i]
      if counter[i] > max:
          max = counter[i]
          moda = i + 1
  return [moda, sum]

def getMediana(counter):#Находим медиану
  med_counter = getModa(counter)[1] / 2
  min = max(counter)
  mediana = 1
  for i in range(len(counter)):
      if abs(med_counter - counter[i]) < min:
          min = abs(med_counter - counter[i])
          mediana = i + 1
  return mediana


edges , nodes = nx.read_edgelist("facebook.txt"), nx.read_adjlist("facebook.txt")#Вершины и ребра
graph = nx.Graph()#создали граф
graph.add_edges_from(edges.edges())#Присоединили вершины к графу
graph.add_nodes_from(nodes)# Присоединили ребра к графу

counter = [] #счётчик вершин
# empty = [] # счётчик несвязных графов



print("подсчёт")
for node_A, node_B in product(graph.nodes, graph.nodes): # Проверяем сколько вершин надо пройти
        if node_A != node_B:
            try:#защита от краша
                n= nx.shortest_path_length(graph, node_A, node_B)
                if len(counter) < n:
                    for i in range(n):
                        if len(counter) < n:
                            counter += [0]
                    counter[n - 1] += 1
                else:
                    counter[n - 1] += 1
            except nx.NetworkXNoPath:
                pass


print('Количество вершин = ', len(nodes), '\n')
print('Количество ребер = ', len(edges.edges), '\n')
print('Мода = ', getModa(counter)[0], '\n')
print('Медиана = ', getMediana(counter), '\n')


################################
container = plt.figure()
window = container.add_subplot(111)
window.set_title("Теория 6 рукопожатий")
window.set_xlabel("Длина пути между вершинами")
window.bar(find_way(counter), counter)
for bar in window.patches:
    window.annotate(bar.get_height(), (bar.get_x() + bar.get_width(), bar.get_height()), ha="center", va="bottom")
plt.show()
################################

