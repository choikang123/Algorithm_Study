arr=[7,5,9,0,3,1,6,2,4,8]
# 삽입 정렬

for i in range(1,len(arr)):
  for j in range(i,0,-1):
    if arr[j-1]>arr[j]:
      arr[j-1],arr[j]=arr[j],arr[j-1]
    else:
      break
print(arr) 
