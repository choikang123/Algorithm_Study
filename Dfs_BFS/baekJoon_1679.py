import sys
from collections import deque
input=sys.stdin.readline
# 숨바꼭질 문제

n,k = map(int, input().split())
visited=[0]*100001
max=100000
def bfs(n,k):    
    # 큐 생성후 n 넣고 방문처리
    q=deque()
    q.append(n)
    visited[n]=1
    # 큐가 빌때까지 그리고 n=k 조건 부합하면 리턴하고 빠져나오기
    while q:
        n=q.popleft()
        if n==k:
            return visited[n]-1
            break

        for i in (n-1,n+1,n*2):
            if 0<=i<=max and not visited[i]: ## 범위체크 항상 먼저 해주기 중요!!
                q.append(i)
                visited[i]=1+visited[n]
print(bfs(n,k))
            
                    
        
        


