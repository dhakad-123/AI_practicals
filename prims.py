
# python program to implement prims algorithm 
import heapq  #heap propery with priority que

class Graph:
    def __init__(self):
        self.graph = {}  #dictionary for adjacency matrix

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {} #this will have value as dictionary
        if v not in self.graph:
            self.graph[v] = {} #this will have value as dictionary
        self.graph[u][v] = w  # Assign weight w to edge (u, v)
        self.graph[v][u] = w  # Assign weight w to edge (v, u)

    def prim_mst(self):
        mst = []  # List to contain tuples (weight, parent, vertex)
        pq = []   # Priority queue with tuple elements
        visited = set()  # Set to keep track of visited vertices
        
        start_vertex = list(self.graph.keys())[0]  # Get the first key of the graph
        heapq.heappush(pq, (0, None, start_vertex))  # Push the first vertex with weight 0 and no parent to pq
        
        while pq:
            weight, parent, vertex = heapq.heappop(pq)  # Pop the smallest element from pq
            if vertex not in visited: #checking vertex is visited or not
                visited.add(vertex)
                if parent is not None: 
                    mst.append((weight, parent, vertex)) #adding touple
                for neb, edge_weight in self.graph[vertex].items(): #adding neigbor of vertex with weight
                    if neb not in visited:
                        heapq.heappush(pq, (edge_weight, vertex, neb))  # Push adjacent vertices to pq
        return mst

# program starts
g = Graph()
n=int(input("number of edges do u want"))
for i in range(n):
    u,v,w=map(int,input("enter u v w:").split())
    g.add_edge(u,v,w)
print(g.graph)

minimum_spanning_tree = g.prim_mst()
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")


#output:

number of edges do u want3
enter u v w:1 2 10
enter u v w:2 3 4
enter u v w:1 3 5
{1: {2: 10, 3: 5}, 2: {1: 10, 3: 4}, 3: {2: 4, 1: 5}}
Minimum Spanning Tree:
Edge: 5 - 1, Weight: 3
Edge: 4 - 3, Weight: 2
