from collections import defaultdict, deque

def has_eulerian_path(N, edges):
    # 그래프 구성
    graph = defaultdict(list)
    degree = [0] * (N + 1)
    
    # 간선 정보 추가 및 차수 계산
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # 홀수 차수를 가진 정점의 개수 세기
    odd_degree_count = sum(1 for i in range(1, N + 1) if degree[i] % 2 != 0)
    
    # 그래프에 간선이 있는지 확인
    has_edges = any(degree[i] > 0 for i in range(1, N + 1))
    
    # 간선이 없는 경우 (문제 조건에 따라 T 반환)
    if not has_edges:
        return True
    
    # 그래프가 연결되어 있는지 확인
    if not is_connected(N, graph, degree):
        return False
    
    # 오일러 경로 조건:
    # 1. 홀수 차수를 가진 정점이 정확히 0개 또는 2개여야 함
    return odd_degree_count == 0 or odd_degree_count == 2

def is_connected(N, graph, degree):
    # 차수가 0보다 큰 첫 번째 정점 찾기
    start = next((i for i in range(1, N + 1) if degree[i] > 0), -1)
    
    # 간선이 없는 경우
    if start == -1:
        return True
    
    # BFS로 연결된 모든 정점 방문
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # 모든 차수가 0보다 큰 정점이 방문되었는지 확인
    for i in range(1, N + 1):
        if degree[i] > 0 and not visited[i]:
            return False
    
    return True

def main():
    # 입력 받기
    N, M = map(int, input().split())
    edges = []
    
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # 오일러 경로 존재 여부 확인
    result = "T" if has_eulerian_path(N, edges) else "F"
    
    # 결과 출력
    print(result)

if __name__ == "__main__":
    main()