from collections import deque  # BFS 구현을 위해 deque 모듈을 import (선입선출 큐)

# 입력 받기
n, m = map(int, input().split())  # 지역 수 n, 버스 노선 수 m을 입력받아 정수로 변환

# 인접 리스트 초기화 (1번 노드부터 n번 노드까지 사용하므로 n+1 크기로 생성)
graph = [[] for _ in range(n + 1)]

# m개의 간선 정보 입력 받기
for _ in range(m):
    u, v = map(int, input().split())  # 정점 u에서 정점 v로 향하는 단방향 간선 입력
    graph[u].append(v)  # u번 노드에서 v번 노드로 이동 가능함을 인접 리스트에 추가

x = int(input())  # 출발 지역 x를 입력받음

# BFS 탐색 준비
visited = [False] * (n + 1)  # 각 노드의 방문 여부를 저장하는 리스트 (초기에는 모두 미방문)
queue = deque()  # BFS에 사용할 큐 생성
queue.append(x)  # 출발 노드를 큐에 넣음
visited[x] = True  # 출발 노드를 방문 처리
count = 1  # 방문한 지역 수를 세기 위한 변수 (출발 지역 포함이므로 1로 시작)

# BFS 알고리즘 실행
while queue:
    now = queue.popleft()  # 큐에서 가장 앞에 있는 노드를 꺼냄
    for neighbor in graph[now]:  # 현재 노드와 연결된 모든 이웃 노드에 대해
        if not visited[neighbor]:  # 아직 방문하지 않았다면
            visited[neighbor] = True  # 방문 처리
            queue.append(neighbor)  # 이웃 노드를 큐에 추가하여 다음에 탐색할 수 있게 함
            count += 1  # 방문한 지역 수 증가

# 모든 연결된 지역을 방문한 후, 방문한 지역 수 출력
print(count)



