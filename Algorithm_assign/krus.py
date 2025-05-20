import heapq

def prim(n, graph):
    visited = [False] * n  # 각 정점의 방문 여부
    min_heap = [(0, 0, -1)]  # (가중치, 현재 정점, 이전 정점)
    mst_edges = []  # 최소 신장 트리에 포함된 간선 저장
    total_weight = 0  # 전체 가중치 (필요 시 사용)
    
    while min_heap:
        weight, current, prev = heapq.heappop(min_heap)

        if visited[current]:
            continue

        visited[current] = True

        # 시작 정점이 아닌 경우 간선을 기록
        if prev != -1:
            mst_edges.append((prev, current, weight))

        # 현재 정점에서 연결된 모든 간선을 확인
        for next_weight, next_vertex in graph[current]:
            if not visited[next_vertex]:
                heapq.heappush(min_heap, (next_weight, next_vertex, current))
    
    return mst_edges

def main():
    n, m = map(int, input().split())
    
    # 인접 리스트로 그래프 초기화
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    # 프림 알고리즘 실행
    mst_edges = prim(n, graph)
    
    # 결과 출력
    for u, v, w in mst_edges:
        print(u, v, w)

# 실행 예시
# main()을 호출하면 입력을 받아 프림 알고리즘을 수행합니다.
if __name__ == "__main__":
    main()
