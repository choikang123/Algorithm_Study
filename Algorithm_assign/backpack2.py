def fractional_knapsack(items, capacity):
    # 각 아이템의 가치/무게 비율 계산 및 인덱스 추가
    for i, item in enumerate(items):
        weight, value = item
        item.append(value / weight)  # 단위 무게당 가치
        item.append(i)  # 원래 인덱스 저장

    # 단위 무게당 가치를 기준으로 내림차순 정렬
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    selected_items = []  # (인덱스, 비율) 형태로 저장

    for weight, value, ratio, orig_idx in items:
        if capacity == 0:
            break

        # 전체 아이템을 넣을 수 있는 경우
        if weight <= capacity:
            fraction = 1.0
            total_value += value
            capacity -= weight
        # 일부만 넣을 수 있는 경우
        else:
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0

        if fraction > 0:
            selected_items.append((orig_idx, fraction))

    # 원래 인덱스 순서로 정렬
    selected_items.sort()

    return selected_items, total_value

def main():
    # 입력 받기
    n = int(input())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append([w, v])  # 리스트로 생성하여 나중에 ratio 추가 가능하도록 함
    capacity = int(input())

    # 부분 배낭 문제 해결
    selected_items, total_value = fractional_knapsack(items, capacity)

    # 결과 출력
    for idx, fraction in selected_items:
        print(f"{idx} {fraction:.1f}")  # 소수점 첫째 자리까지 출력
    print(int(total_value))  # 총 가치 출력

if __name__ == "__main__":
    main()
