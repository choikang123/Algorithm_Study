package array;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class pr_4 {
    public static void main(String[] args) {
        //정수 배열을 받는다

        //solution 함수를 완성하는데 (서로 다른 수 2개를 뽑아 더해 나온 모든 수를 오름차순된 배열로 반환)
        // 1. 배열에서 두수를 선택하는 모든 경우의 수
        // 2. 중복값 제거
        // 3. 오름차순 정렬 반환
    }

    private static int[] solution(int[] arr) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 1; j < arr.length; j++) {
                set.add(arr[i]+arr[j]);
            }
        }
        return set.stream()
                .sorted()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
