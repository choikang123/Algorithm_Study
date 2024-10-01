array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i # 첫번째 인덱스
    for j in range(i+1,len(array)): # 두번째 인덱스부터 배열 끝까지 반복
        if array[min_index] > array[j]: # 만약 첫번째 인덱스의 값보다 작다면 작은 값의 인덱스를 저장하고 담아두기
            min_index=j
    array[i],array[min_index]=array[min_index],array[i] # temp 이용하지 않고 바로 바뀌기

print(array)

