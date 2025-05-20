import time

# 순차 탐색 함수
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # 찾으면 인덱스 반환
    return -1  # 찾지 못하면 -1 반환

# 파일에서 5,000,001개의 데이터를 읽는다고 가정 (여기서는 1부터 5,000,001까지의 리스트 사용)
data = list(range(1, 5000002))  # 1부터 5,000,001까지의 리스트 생성

# 최악의 상황 (마지막 값을 찾는 경우) 시간 복잡도: O(n) (선형시간)
target = 5000001
start_time = time.time()
index = linear_search(data, target)
end_time = time.time()
worst_case_time = end_time - start_time  # 최악의 경우 시간 측정

# 최선의 상황 (첫 번째 값을 찾는 경우) 시간 복잡도: O(1)
target = 1
start_time = time.time()
index = linear_search(data, target)
end_time = time.time()
best_case_time = end_time - start_time  # 최선의 경우 시간 측정

# 평균적인 상황 (중간 값을 찾는 경우) 시간 복잡도: O(n) (선형시간)
target = 2500001  # 리스트의 중간 값
start_time = time.time()
index = linear_search(data, target)
end_time = time.time()
average_case_time = end_time - start_time  # 평균적인 경우 시간 측정

# 결과 출력
print(f"최선의 경우 실행 시간: {best_case_time:.6f}초")
print(f"최악의 경우 실행 시간: {worst_case_time:.6f}초")
print(f"평균적인 경우 실행 시간: {average_case_time:.6f}초")

#순차 탐색(Linear Search)은 주어진 리스트에서 특정한 값을 찾는 알고리즘으로, 리스트의 처음부터
#끝까지 차례로 요소를 비교하며 찾고자 하는 값을 검색하는 방법입니다. 본 보고서에서는 순차 탐색의 최악, 최선, 평균적인 경우의 시간 복잡도를 분석하고 실행 시간을 측정한 결과를 제시합니다.

# 최선의 경우 실행 시간: 0.000000초
# 최악의 경우 실행 시간: 0.259147초  
# 평균적인 경우 실행 시간: 0.125157초 
