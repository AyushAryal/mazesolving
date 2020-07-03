import queue

class Graph:
    def __init__(self, vert_num):
        self.graph = [[] for _ in range(vert_num)]

    def add_vert(self):
        self.graph.append([])

    def add_edge(self, vertA, vertB, weight = 1):
        self.graph[vertA].append((vertB, weight))

    def add_uedge(self, vertA, vertB, weight = 1):
        self.add_edge(vertA, vertB, weight)
        self.add_edge(vertB, vertA, weight)

    def __str__(self):
        return str(self.graph)

graph = Graph(5)
graph.add_uedge(0,1)
graph.add_uedge(0,4)
graph.add_uedge(4,1)
graph.add_uedge(4,3)
graph.add_uedge(1,3)
graph.add_uedge(1,2)
graph.add_uedge(2,3)


def bfs(graph, startVert, endVert):
    visited = [False] * len(graph.graph)
    q = queue.Queue(len(graph.graph))
    q.put(startVert)

    # childern -> parent
    mapping = {startVert : None}
    found = False
    while not q.empty():
        item = q.get()
        if item == endVert:
            found = True
            break
        
        adj = graph.graph[item]
        
        for vert_num, _ in adj:
            if not visited[vert_num]:
                mapping[vert_num] = item
                q.put(vert_num)
            visited[vert_num] = True
    
    if found:
        parent = endVert
        path = [endVert]
        while parent != startVert:
            parent = mapping[parent]
            path.append(parent)
        print(list(reversed(path)))

bfs(graph, 1, 4)