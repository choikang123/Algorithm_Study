package array;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class pr_3 {
    public static void main(String[] args) {
        //정수 배열을 받는다
        int[] arr = {4, 2, 2, 1, 3, 4};
        //배열의 중복값을 제거하고 내림차순 정렬해 반환하는 메서드를 호출한다
        System.out.println(Arrays.toString(distinctAndSort(arr)));
    }
    private static int[] distinctAndSort(int[] arr) {
        return Arrays.stream(arr)
                .boxed()
                .distinct()
                .sorted(Collections.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
