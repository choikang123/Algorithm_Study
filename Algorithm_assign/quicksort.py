n = int(input())  # 입력 크기
data = list(map(int, input().split()))  # 배열 입력

pivots = []  # 피벗 값을 저장할 리스트

def quicksort(arr, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return arr
    
    start_value = arr[start]
    end_value = arr[end]
    mid_index = (start + end) // 2  # 배열의 중간값 계산
    mid_value = arr[mid_index]
    
    # 중간값을 피벗으로 선택
    pivot_value = sorted([start_value, end_value, mid_value])[1]
    
    # 피벗값 저장
    pivots.append(pivot_value)
    
    # 피벗 값의 인덱스를 구함
    if pivot_value == start_value:
        pivot_index = start
    elif pivot_value == mid_value:
        pivot_index = mid_index
    else:
        pivot_index = end
    
    # 배열의 시작 부분과 피벗 값을 교환
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]

    # 포인터 설정
    pivot_index = start
    l = start + 1
    r = end
    
    # 배열을 분할하는 과정
    while l <= r:
        while l <= end and arr[l] < pivot_value:
            l += 1
        while r > start and arr[r] > pivot_value:
            r -= 1
        if l <= r:  # 교차하지 않았으면 l과 r 교환
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    #피벗과 r 교환
    arr[start], arr[r] = arr[r], arr[start]
    # 재귀적으로 왼쪽 오른쪽 정렬
    quicksort(arr, start, r - 1)
    quicksort(arr, r + 1, end)


quicksort(data, 0, len(data) - 1)

print(" ".join(map(int, pivots)) + " ")
print(" ".join(map(int, data)) + " ")
