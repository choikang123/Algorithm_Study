import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

pivots = []

def quicksort(arr, start, end):
    if start >= end:  # 원소가 1개인 경우
        return arr
    
    start_value = arr[start]
    end_value = arr[end]
    mid_index = (start + end) // 2
    mid_value = arr[mid_index]
    
    pivot_value = sorted([start_value, end_value, mid_value])[1]  # 중간값이 피벗
    # 피벗값 저장
    pivots.append(pivot_value)
    # 배열의 시작부분과 pivot의 인덱스 위치의 값의 원소를 바꿔줌
    pivot_index = arr.index(pivot_value)  # pivot_value=3
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    
    # 포인터 설정
    pivot_index = start
    l = pivot_index + 1
    r = end
    
    # 
    while l <= r:
        # 만약 이 조건이 없으면 배열의 범위를 넘어서 인덱스 에러가 발생할 수 있겠죠.
        while l <= end and arr[l] <= arr[pivot_index]:  
            l += 1
        while start < r and arr[r] >= arr[pivot_index]:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            
    arr[r], arr[pivot_index] = arr[pivot_index], arr[r] 

    quicksort(arr, start, r - 1)
    quicksort(arr, r + 1, end)

quicksort(data, 0, len(data) - 1)

print(" ".join(map(str, data)) + " ")
print(" ".join(map(str, pivots)) + " ")

