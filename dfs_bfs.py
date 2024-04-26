#python dfs bfs graph implementation
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edges(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        que = deque([start])   #need to pass list parameter and importdeque from collections
        traversal = []

        while que:
            vertex = que.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex) 
                for neighbor in self.graph[vertex]:  #it will iterate through values of key here key is vertex
                    que.append(neighbor)  # Enqueue all neighbors regardless of visitation status

        return traversal
    def dfs(self, start):
        visited = set()
        stack = [start]   #list
        traversal = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                for neighbor in self.graph[vertex]:
                    stack.append(neighbor)

        return traversal

    def display(self):
        print(self.graph)

# Main code
g = Graph()
print("Enter number of edges you want:")
edges = int(input())

print("Enter edges in format u v:")
for _ in range(edges):
    u = int(input("Enter vertex 1: "))
    v = int(input("Enter vertex 2: "))
    g.add_edges(u, v)

print("Graph:")
g.display()

start_vertex = int(input("Enter the start index for BFS: "))
res = g.bfs(start_vertex)
res2 = g.dfs(start_vertex)

print(res)
print("dfs traversal")
print(res2)

#output:
Enter number of edges you want:
5
Enter edges in format u v:
Enter vertex 1: 0
Enter vertex 2: 2
Enter vertex 1: 0
Enter vertex 2: 1
Enter vertex 1: 0
Enter vertex 2: 3
Enter vertex 1: 2
Enter vertex 2: 3
Enter vertex 1: 2
Enter vertex 2: 4
Graph:
{0: [2, 1, 3], 2: [0, 3, 4], 1: [0], 3: [0, 2], 4: [2]}
Enter the start index for BFS: 0
[0, 2, 1, 3, 4]
dfs traversal
[0, 3, 2, 4, 1]


