import sys
import math

# 두 점 사이의 거리 계산
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# 최근접 점 쌍을 찾는 함수 (브루트 포스)
def brute_force(points):
    min_dist = float('inf')
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist

    return min_dist

def closest_pair(points):
    n = len(points)

    if n <= 3:
        return brute_force(points)

    mid = n // 2
    mid_point = points[mid]

    # 좌우 부분 집합
    left_half = points[:mid]
    right_half = points[mid:]

    # 각 부분에서 최소 거리 찾기
    d_left = closest_pair(left_half)
    d_right = closest_pair(right_half)

    # 최소 거리 찾기
    d = min(d_left, d_right)

    # 중간 영역의 점들
    strip = [point for point in points if abs(point[0] - mid_point[0]) < d]

    # 중간 영역에서 최소 거리 찾기
    strip.sort(key=lambda point: point[1])  # y 좌표 기준으로 정렬

    min_dist = d
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:  # y 좌표 차이가 min_dist 이상이면 중단
                break
            
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist

    return min_dist

if __name__ == "__main__":
    points = []

    # 전체 점의 개수 입력
    n = int(input().strip())

    # 각 점의 좌표 입력
    for _ in range(n):
        line = input().strip()  # 입력을 받고 양 끝의 공백 제거
        x, y = map(int, line.split(', '))
        points.append((x, y))
    
    # 점을 x좌표 기준으로 정렬
    points.sort(key=lambda point: point[0])
    
    # 최근접 점 쌍의 최소 거리 찾기
    min_distance = closest_pair(points)

    # 결과 출력 (소수점 이하 6자리)
    print(f"{min_distance:.6f}")
