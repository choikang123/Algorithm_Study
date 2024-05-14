import sys
from collections import deque
input = sys.stdin.readline
#촌수 계산
n=int(input())
graph=[[] for _ in range(n+1)]
s,e=map(int,input().split())
m=int(input())

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(s,e):
    visited=[0]*(n+1) # 각 정점까지의 거리를 저장할 리스트
    q=deque()
    q.append(s) # q.append([s]) 리스트로 저장하는게 아님 정점으로 저장 헷갈리지 않기
    visited[s]=1 #

    while q:
        s=q.popleft()
        if s==e:
            return visited[e]-1  # 처음 나 자신이 1로 시작하기 때문에 -1을 해줘야 함
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i]=1+visited[s]
    return -1

print(bfs(s,e))
    