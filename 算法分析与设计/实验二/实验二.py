import heapq
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim(self):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        key[0] = 0
        min_heap = [(0, 0)]
        in_heap = [True] * self.V  # 添加一个标记数组

        while min_heap:
            weight, u = heapq.heappop(min_heap)# pop最小元素
            in_heap[u] = False  # 在图中删除已添加的边

            for v, w in self.graph[u]:
                # 检查是否在图中并且是否可以更新键值
                if in_heap[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u
                    heapq.heappush(min_heap, (w, v))  # 重新将更新后的顶点加入生成树

        return parent

    def kruskal(self):
        edges = []
        for u in range(self.V):
            for v, w in self.graph[u]:
                if u < v:  # 确保每条边只添加一次
                    edges.append((w, u, v))
        # 排序边的权重
        edges.sort()

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        # 判断有没有环
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])# 递归查找是否成环
            return parent[u]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

        result = []
        for w, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                result.append((u, v, w))

        return result

m, n = map(int, input().split(','))
g = Graph(m)

# input结点和节点距离
for _ in range(n):
    u, v, w = input().split(',')
    g.add_edge(ord(u) - ord('A'), ord(v) - ord('A'), int(w))

# prim_result
parent = g.prim()
print("Prim:")
for i in range(1, m):
    print(chr(ord('A') + parent[i]), chr(ord('A') + i), sep=',', end=',')
    for v, w in g.graph[parent[i]]:
        if v == i:
            print(w)
            break

# kruskal_result
result = g.kruskal()
print("Kruskal:")
for u, v, w in result:
    print(chr(ord('A') + u), chr(ord('A') + v), w, sep=',')