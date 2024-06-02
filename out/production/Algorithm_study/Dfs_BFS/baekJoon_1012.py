import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, graph):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.append([x, y])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j, graph)
                cnt += 1
    print(cnt)
