package implement;

import java.util.Scanner;

public class BaekJoon_28701 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum1 = 0;
        int sum3 = 0;

        for (int i = 0; i < n; i++) {
            sum1 += (i + 1);
        }

        int result = (int) Math.pow(sum1, 2);

        for (int i = 1; i <= n; i++) {
            sum3 += i * i * i;
        }

        System.out.println(sum1+"\n"+result+"\n"+sum3);



    }
}
