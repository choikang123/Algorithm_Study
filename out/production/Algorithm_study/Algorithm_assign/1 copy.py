import sys
input = sys.stdin.readline

k = int(input())
x, y = map(int, input().split())

num = 0
length = pow(2, k)
data = [[0] * length for _ in range(length)]
data[y- 1][x- 1] = -1

def checkHole(x, y, length):
    for i in range(x, x + length):
        for j in range(y, y + length):
            if data[i][j] != 0:
                return False
    return True

def tromino(x, y, length):
    global num
    num += 1
    halfLen = length // 2

    # 각 구역에 대한 타일링
    if checkHole(x, y, halfLen):
        data[x + halfLen - 1][y + halfLen - 1] = num
    if checkHole(x, y + halfLen, halfLen):
        data[x + halfLen - 1][y + halfLen] = num
    if checkHole(x + halfLen, y, halfLen):
        data[x + halfLen][y + halfLen - 1] = num
    if checkHole(x + halfLen, y + halfLen, halfLen):
        data[x + halfLen][y + halfLen] = num
        
    # 더 이상 분할할 수 없으면 종료
    if halfLen <= 1:  # 변경된 부분
        return

    # 재귀 호출로 4개의 구역에 대해 타일링 수행
    tromino(x, y, halfLen)
    tromino(x, y + halfLen, halfLen)
    tromino(x + halfLen, y, halfLen)
    tromino(x + halfLen, y + halfLen, halfLen)

# 트로미노 타일링 시작
tromino(0, 0, length)

# 결과 출력
for i in range(length):
    for j in range(length):
        print(data[i][j], end=' ')
    print()
