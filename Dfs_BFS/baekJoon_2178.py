import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

def bfs(x,y):
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
                
bfs(0,0)
#dfs(1,1)이라고 처음에 실행했는데 주의
print(graph[n-1][m-1])
#graph[nx-1][ny-1]이라고 썼는데 함수 안에서 쓴 변수는
#나와서 쓸 수 없음 주의
