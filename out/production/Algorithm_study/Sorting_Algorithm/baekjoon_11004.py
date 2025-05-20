import sys

input = sys.stdin.readline
n, k = map(int, input().split())
data_list = list(map(int, input().split()))

def quickSort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:  # 분할이 끝날 때까지 반복
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈렸다면
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽과 오른쪽을 각각 다시 정렬
    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)

# 퀵 정렬 실행
quickSort(data_list, 0, len(data_list) - 1)

# 정렬된 리스트 출력
print(data_list[k-1])
