package implement;

import java.util.Scanner;

public class DSA {
    // 이진 트리를 배열로 표현하는 정적 변수
    // 인덱스 1부터 사용하여 부모-자식 관계를 쉽게 계산
    static int[] tree;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 트리의 노드 개수 입력
        int k = sc.nextInt();

        // 트리 배열 초기화 (인덱스 0은 사용하지 않음)
        tree = new int[k + 1];

        // 트리의 각 노드 값을 입력받아 배열에 저장
        // 인덱스 1부터 시작하여 완전 이진 트리 형태로 저장
        for (int i = 1; i <= k; i++) {
            tree[i] = sc.nextInt();
        }

        // 루트 노드(인덱스 1)부터 중위 순회 시작
        inOrder(1);
    }

    // 중위 순회(In-order Traversal) 재귀 함수
    // 순서: 왼쪽 서브트리 → 현재 노드 → 오른쪽 서브트리
    static void inOrder(int idx) {
        // 기저 조건: 현재 인덱스가 배열 범위를 벗어나면 종료
        // 즉, 존재하지 않는 노드에 도달했을 때 재귀 종료
        if (idx >= tree.length) return;

        // 1단계: 왼쪽 자식 노드 방문
        // 완전 이진 트리에서 왼쪽 자식의 인덱스는 부모 인덱스 * 2
        inOrder(idx * 2);

        // 2단계: 현재 노드 처리 (값 출력)
        // 왼쪽 서브트리를 모두 방문한 후 현재 노드 출력
        System.out.print(tree[idx] + " ");

        // 3단계: 오른쪽 자식 노드 방문
        // 완전 이진 트리에서 오른쪽 자식의 인덱스는 부모 인덱스 * 2 + 1
        inOrder(idx * 2 + 1);
    }
}

