package implement;
import java.util.Scanner;

public class BaekJoon_1977 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int sum = 0;
        int min = 0;
        for (int i = 1; i <= 100; i++) {
            int pow = i * i; //제곱 수
            if (m <= pow && pow <= n) {
                if (sum == 0) {
                    min = pow;
                }
                sum += pow;
            }


        }
        if (sum == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sum + "\n" + min);
        }
    }
}

