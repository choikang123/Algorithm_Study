import sys
from random import randint
input = sys.stdin.readline

def partition(arr,left,right):
  #left와 right중에 랜덤한 피벗인덱스 설정
  pivot=randint(left,right) 
  
  # 피벗이 맨 왼쪽이 아니라면 바꿔주기
  if(pivot!=left):
    arr[left],arr[pivot]=arr[pivot],arr[left]
  
  pivot=left
  l=pivot+1
  r=right
  # 퀵정렬 시작
  while(l<=r):
    while(l<=right and arr[l]<arr[pivot]):
      l+=1
    while(r>left and arr[r]>arr[pivot]):
      r-=1
    if(l<=r):
      arr[l],arr[r]=arr[r],arr[l]
    else:
      arr[pivot],arr[r]=arr[r],arr[pivot]
  return r #피벗의 인덱스 반환

def quick_selection(arr, left, right, k):
    # Partition 함수를 사용해 피벗의 위치를 찾는다
    pivot = partition(arr, left, right)
    
    # S = Small group의 크기 = (pivot - 1) - left + 1
    S = pivot - left  # 피벗 왼쪽에 있는 원소 수
    
    # k가 Small group에 있는 경우 (k <= S)
    if k <= S:
        return quick_selection(arr, left, pivot - 1, k)
    
    # 피벗이 k번째 작은 값인 경우 (k == S + 1)
    elif k == S + 1:
        return arr[pivot]
    
    # k가 Large group에 있는 경우 (k > S + 1)
    else:
        # Large group에서 찾기 위해 k를 조정
        return quick_selection(arr, pivot + 1, right, k - S - 1)

# 배열과 k값 설정 (k는 1 기반)
# sublist는 숫자들이 있는 리스트입니다.
array=list(map(int,input().split()))
k = 6
value = quick_selection(array, 0, len(array) - 1, k)
print(value)

