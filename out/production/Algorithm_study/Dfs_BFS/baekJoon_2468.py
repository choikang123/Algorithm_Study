import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

def bfs(x,y,h):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]>h and visited[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny]=1
                                      
def solve(h):
    cnt=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>h and visited[i][j]==0:
                bfs(i,j,h)
                cnt+=1
    return cnt
# 물의 높이마다 - 반복문, bfs를 돌려줘야 함 최대값
max_safe=0
for high in range(100):
    visited=[[0]*n for _ in range(n)] # 각 높이마다 방문배열 초기화
    max_safe=max(max_safe,solve(high))
print(max_safe)



