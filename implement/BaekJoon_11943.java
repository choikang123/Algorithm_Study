package implement;

import java.util.Scanner;

public class BaekJoon_11943 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 첫번째 바구니의 사과 + 두번째 바구니의 오렌지
        // 첫번째 바구니의 오렌지+ 두번째 바구니의 사과
        // 1,2의 최솟값을 구하면 된다.
        int a = sc.nextInt(), b= sc.nextInt();
        int c = sc.nextInt(), d = sc.nextInt();
        System.out.println(Math.min(a + c, b + d));
    }

}
