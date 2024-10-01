import sys
input=sys.stdin.readline

def binary(array,target,start,end):
  while(start<=end):
    mid=(start+end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid]==target:
      return target
    # 중간점의 값보다 찾고자 하는 값이 큰 경우
    elif array[mid]<target:
      start=mid+1
    else:
      end=mid-1
  return None

n=int(input())
array=list(map(int,input().split()))
array.sort()

m=int(input())
x=list(map(int,input().split()))


for i in x:
  result=binary(array,i,0,n-1)
  if result!=None:
    print("yes",end=" ")
  else:
    print("no",end=" ")
