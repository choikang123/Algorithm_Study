package implement;

import java.util.Scanner;

public class BaekJoon_4344 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();
        for (int i = 0; i < testCase; i++) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            double sum = 0;
            for (int j = 0; j < n; j++) {
                int val = sc.nextInt();
                arr[j] = val;
                sum += val;
            }
            double mean = sum / n;
            double cnt = 0;
            for (int j = 0; j < n; j++) {
                if (arr[j] > mean) {
                    cnt++;
                }
            }
            System.out.printf("%.3f%%\n", (cnt / n) * 100);;
        }

    }
}
