from queue import Queue

TEST = False
in_file = "./resources/day_25_test.txt" if TEST else "./resources/day_25_input.txt"


if TEST:
    removed = {"hfx": "pzl", "bvb": "cmg", "nvd": "jqt", "pzl": "hfx", "cmg": "bvb", "jqt": "nvd"}
else:
    removed = {"kfr": "vkp", "bff": "rhk", "qpp": "vnm", "vkp": "kfr", "rhk": "bff", "vnm": "qpp" }

import networkx as nx
import matplotlib.pyplot as plt

options = {
    "font_size": 8,
    "node_size": 250,
    # "node_color": "blue",
    # "edgecolors": "black",
    "linewidths": 0.5,
    "width": 0.5,
    "with_labels": True,
}


def file_lines():
    with open(in_file) as file:
        connections = {}
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            node, subnodes = line.split(": ")
            subnodes = subnodes.split(" ")
            if node not in connections:
                connections[node] = []
            for sub in subnodes:
                if sub not in connections:
                    connections[sub] = []
                connections[node].append(sub)
                connections[sub].append(node)
        return connections


def question_1():
    """Answer to the first question of the day"""
    answer = None
    graph = file_lines()

    # draw_graph(graph) # eye balled the graph and the connections to remove are:
    # kfr-vkp, bff-rhk, qpp-vnm

    for node in graph:
        if node in removed.keys():
            graph[node].remove(removed[node])
    # draw_graph(graph)

    # exhastive BFS on each side
    a, b = removed.popitem()
    print(a, b)

    return bfs(graph, a) * bfs(graph, b)


def draw_graph(graph):
    G = nx.Graph()
    for node in graph:
        G.add_node(node)
        for neighbour in graph[node]:
            G.add_edge(node, neighbour, distance="1")

    pos = nx.spring_layout(G)

    nx.draw_networkx(G, pos, **options)
    edge_labels = nx.get_edge_attributes(G, "distance")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)

    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()


def bfs(graph, node):
    frontier = Queue()
    frontier.put(node)
    reached = set()
    reached.add(node)

    while not frontier.empty():
        current = frontier.get()
        for next in graph[current]:
            if next not in reached:
                frontier.put(next)
                reached.add(next)
    return len(reached)

def question_2():
    """Answer to the second question of the day"""
    answer = None

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    # answer_2 = question_2()
    # print(f"Question 2 answer is: {answer_2}")
