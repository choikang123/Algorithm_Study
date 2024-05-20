import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().rstrip())) for _ in range(n)]
cnt=0
result=[]

def dfs(x,y):
    global cnt
    graph[x][y]=0    
    cnt+=1

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            dfs(i,j)
            result.append(cnt)
            cnt=0

result.sort()
print(len(result),*result, sep="\n")

