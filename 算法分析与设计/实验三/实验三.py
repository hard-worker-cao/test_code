from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * self.V
        queue = deque([s])
        visited[s] = True
        bfs_result = []

        while queue:
            s = queue.popleft()
            bfs_result.append(s)

            for i in sorted(self.graph[s]):
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return bfs_result

    def DFSUtil(self, v, visited, dfs_result):
        visited[v] = True
        dfs_result.append(v)

        for i in sorted(self.graph[v]):
            if not visited[i]:
                self.DFSUtil(i, visited, dfs_result)

    def DFS(self, v):
        visited = [False] * self.V
        dfs_result = []
        self.DFSUtil(v, visited, dfs_result)
        return dfs_result

# 示例输入
m, n = map(int, input().split(','))
g = Graph(m)
edges = []

for _ in range(n):
    u, v = input().split(',')
    edges.append((u, v))

# 添加边
for u, v in edges:
    g.add_edge(ord(u) - ord('A'), ord(v) - ord('A'))

# 遍历开始的顶点
start_vertex = ord(input().strip()) - ord('A')

# 输出BFS和DFS遍历结果
print("BFS:", ','.join([chr(ord('A') + i) for i in g.BFS(start_vertex)]))
print("DFS:", ','.join([chr(ord('A') + i) for i in g.DFS(start_vertex)]))
