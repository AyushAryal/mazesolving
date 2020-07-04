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

    def bfs(self, startVert, endVert):
        visited = [False] * len(self.graph)
        q = queue.Queue(len(self.graph))
        q.put(startVert)

        # childern -> parent
        mapping = {startVert : None}
        found = False
        while not q.empty():
            item = q.get()
            if item == endVert:
                found = True
                break
            
            adj = self.graph[item]
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
            return list(reversed(path))
        return []