
from util import Queue
from graph import Graph
import sys
sys.path.append('../graph')


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for n in range(1, 12):
        graph.add_vertex(n)

    for edge in ancestors:
        graph.add_edge(edge[0], edge[1])

    q = Queue()
    q.enqueue(starting_node)
    count = 0

    while q.size() > 0:
        v = q.dequeue()
        print(f"v: {v}")
        edge_found = 0
        for edge in ancestors:
            if edge[1] == v:
                print(f"edge0: {edge[0]}")
                q.enqueue(edge[0])
                count += 1
                edge_found += 1
            if edge_found > 1:
                v1 = q.dequeue()
                v2 = q.dequeue()
                print(f"v1: {v1}, v2: {v2}")
                if v1 < v2:
                    q.enqueue(v1)
                else:
                    q.enqueue(v2)
                edge_found -= 1
        if count == 0:
            return -1
        if edge_found == 0:
            return v
