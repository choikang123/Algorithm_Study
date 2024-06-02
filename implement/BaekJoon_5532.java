package implement;

import java.util.Scanner;

public class BaekJoon_5532 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();

        int a_result;
        int b_result;
        int result;

        if (a % c == 0) {
             a_result = (a / c);
        } else {
             a_result = (a/c)+1;
        }

        if (b % d == 0) {
             b_result = (b / d);
        } else {
             b_result = (b/d)+1;
        }

        System.out.println(a_result>b_result ? l-a_result:l-b_result);


        // 전체 일수에서 숙제를 다하는 일자를 빼준 값 출력
        // 숙제를 다하는 일자는 a와 b중에서 더큰 일자를 가져와서 빼기
    }
}
