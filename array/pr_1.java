package array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class pr_1 {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        int[] arr2 = new int[]{1, 2, 3, 4, 5};
        int[] arr3 = new int[5];

        System.out.println(Arrays.toString(arr));

        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        System.out.println(list);

        ArrayList<Integer> lists2 = new ArrayList<>(list);
        System.out.println(lists2);

        int[] arr5 = {1, 2, 4, 5, 3};
        System.out.println(arr.length); // 5
        Arrays.sort(arr5); // 정렬 [1, 2, 3, 4, 5]
        System.out.println(Arrays.toString(arr5)); // 출력 [1, 2, 3, 4, 5]

        ArrayList<Integer> list5 = new ArrayList<>(Arrays.asList(1, 2, 4, 5, 3));
        list.size();
        Collections.sort(list5);
    }
}
