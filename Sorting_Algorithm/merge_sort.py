def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # 배열의 길이가 1 이하이면 정렬된 상태로 반환

    # 배열을 두 개로 나눈다
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # 두 부분을 병합하는 함수 호출
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    # 두 배열을 병합한다
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 남아 있는 요소들을 추가한다
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# 테스트
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
sorted_arr = merge_sort(arr)
print(sorted_arr)
