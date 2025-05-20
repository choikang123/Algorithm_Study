package implement;

import java.util.Scanner;

public class Dhash {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int count = 0;
        for (int i : arr) {
            if (dHash(x) == dHash(i)) {
                count++;
            }
        }
        System.out.println(count);
    }

    private static int dHash(int value) {
        String strValue = String.valueOf(value);
        int count = 0;
        for (int i = 0; i < strValue.length(); i++) {
            char c = strValue.charAt(i);
            int parseCount = Integer.parseInt(String.valueOf(c));
            count+= parseCount;
        }
        return (count*8)%14;
    }
}
