https://yiseul-coding.tistory.com/28
def check(arr, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if arr[i - 1][j - 1] != 0:
                return False
    return True

def tromino(data, num, size, x, y):
    if size == 1:
        return
    num[0] += 1
    size //= 2
    x -= size
    y -= size

    directions = [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]

    pos1 = check(data, x - (size - 1), y - (size - 1), x, y)
    pos2 = check(data, x + 1, y - (size - 1), x + size, y)
    pos3 = check(data, x - (size - 1), y + 1, x, y + size)
    pos4 = check(data, x + 1, y + 1, x + size, y + size)

    pos = [pos1, pos2, pos3, pos4]
    for i in range(4):
        if pos[i]:
            data[directions[i][0] - 1][directions[i][1] - 1] = num[0]

    tromino(data, num, size, x, y)
    tromino(data, num, size, x + size, y)
    tromino(data, num, size, x, y + size)
    tromino(data, num, size, x + size, y + size)

def main():
    k = int(input("k 값을 입력하세요: "))  # k 입력 (보드 크기 결정)
    size = 2 ** k
    data = [[0 for _ in range(size)] for _ in range(size)]

    m, n = map(int, input("채워지지 않는 한 곳을 입력하세요 (m, n): ").split())  # (채워지지 않는 한 곳 입력)
    data[m - 1][n - 1] = -1

    num = [0]  # num을 리스트로 전달하여 참조 변경 가능하도록 함
    tromino(data, num, size, size, size)

    # 결과 출력
    for row in data:
        print('  '.join(map(str, row)))

if __name__ == "__main__":
    main()
