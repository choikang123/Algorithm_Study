package implement;

import java.util.Scanner;

public class BaekJoon_10871 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), x = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        for (int a : arr) {
            if (a < x) {
                System.out.print(a+" ");
            }
        }
    }
}
