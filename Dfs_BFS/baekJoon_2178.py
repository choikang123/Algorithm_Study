import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

def dfs(x,y):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    queue=deque()
    queue.append([x,y])

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                queue.append([nx,ny])
                graph[nx][ny]=graph[x][y]+1
                
dfs(0,0)
print(graph[n-1][m-1])