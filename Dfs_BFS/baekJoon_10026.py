import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]


def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[x][y]==graph[nx][ny]:
                dfs(nx, ny)

# 정상인 경우
visited = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

# 적록색약 변환
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

visited = [[0] * n for _ in range(n)]
cnt_1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt_1 += 1

print(cnt)
print(cnt_1)
