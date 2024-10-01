arr=[7,5,9,0,3,1,6,2,4,8]
# 삽입 정렬

for i in range(1,len(arr)):
  for j in range(i,0,-1):
    if arr[j-1]>arr[j]:
      arr[j-1],arr[j]=arr[j],arr[j-1]
    else:
      break
print(arr) 

# 이미 정렬된 상태라면 퀵정렬보다 삽입정렬이 훨씬 빠름


# 