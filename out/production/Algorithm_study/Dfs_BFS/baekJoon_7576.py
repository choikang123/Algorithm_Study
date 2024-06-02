import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
q=deque()
# 그래프에서 1인 좌표 큐에 담아주기 
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append([i,j])

def bfs():
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=1+graph[x][y]
                q.append([nx,ny])
bfs() #bfs 실행하고 나면 그래프에 거리가 적힘
max_distance=0
for i in graph: # i에 행전체
    for j in i: # j에 행의 요소
        if j==0: # 요소중에 0이 있다면
            print(-1)
            exit(0) # 프로그램 종료
    else:
        max_distance=max(max_distance,max(i))
print(max_distance-1)




