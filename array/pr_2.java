package array;

import java.util.Arrays;

public class pr_2 {
    public static void main(String[] args) {
        int[] arr = {2,6,3,5,1};
        int[] sort = sort(arr);
        System.out.println(Arrays.toString(arr));
        System.out.println(Arrays.toString(sort));
    }

    private static int[] sort(int[] arr) {
        int[] clone = arr.clone();
        Arrays.sort(clone);
        return clone;
    }
}
