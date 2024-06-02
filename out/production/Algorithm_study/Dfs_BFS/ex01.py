import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

# 세로 n 가로 m이 주어진다
n,m=map(int,input().split())

# 얼음 틀의 형태
# graph=[]
# for i in range(n):
#     graph.append(map(int,input()))
# graph를 리스트에 넣을때 map 객체 대신 리스트로 변환해주어야 함
# 얼음 틀의 형태
# 얼음 틀의 형태
graph=[]
for i in range(n):
    graph.append(list(map(int,input().rstrip())))


# 이동할 네방향 정의
dx=[0,0,-1,1]
dy=[1,-1,0,0]
# bfs 
def bfs(x,y):
    # 그래프의 0을 1로 변환
    graph[x][y]=1
    # 큐 생성과 삽입
    queue=deque()
    queue.append((x,y))

    # 큐가 빌때까지 반복
    while(queue):
        x,y=queue.popleft() 
        ## x와 y에 왜 활당해주는지 잘 모르겠음그냥 queue.popleft() 해주면 되는거 아닌가? x와y는 bfs 함수에서 이미 정의되어있는데
        ## 이 답은 매개변수가 xy가 아니라 a,b 이런식으로 오게 되는 경우도 있기 때문에
        #현재 위치에서 네방향 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=1
                queue.append((nx,ny))

# 아이스크림의 개수 출력
cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            bfs(i,j)
            cnt+=1
print(cnt)

# n,m=4,5일때
#   0 1 2 3 4 5
# 0 1 1 1 1 1
# 1 1
# 2 1
# 3 1
# 4
# 이렇게 되기 때문에 if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
