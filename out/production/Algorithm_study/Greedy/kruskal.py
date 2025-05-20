class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)  
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if ds.union(u, v):  # If u and v are not connected
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight

if __name__ == "__main__":
    # Input: number of vertices and edges
    n, m = map(int, input().split())
    edges = []

    # Input: edges information
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    # Finding the minimum spanning tree using Kruskal's algorithm
    mst, total_weight = kruskal(n, edges)

    # Output: edges of the minimum spanning tree
    for u, v, w in sorted(mst, key=lambda x: x[2]):  # Sort edges by weight for output
        print(f"{u} {v} {w}")
    
    # Output: total weight of the minimum spanning tree
    print(total_weight)
