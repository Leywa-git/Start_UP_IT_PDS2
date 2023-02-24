import networkx as nx
import matplotlib.pyplot as plt

# 1 - creating a list from csv file and building a graph

edgelist = []
with open("cities.csv", "r") as file:
    for line in file:
        value = line.split(";")
        edgelist.append([value[0], value[1], int(value[2])])

g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight=edge[2])

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("cities.csv")
plt.show()

print("Graph of cities from file cities.csv has been built and drawn.")

# 2 - creating a function to get the minimal length of path between two cities


def path_length(graph, start_city, end_city):
    path = nx.shortest_path(graph, start_city, end_city, weight="weight")
    length = nx.shortest_path_length(graph, start_city, end_city, weight="weight")
    return print(f"The shortest path between cities {start_city} and {end_city}: {path} "
                 f"The distance: {length} km")


path_length(g, "Dnipro", "Lviv")
path_length(g, "Dnipro", "Melitopol")
path_length(g, "Dnipro", "Kyiv")
