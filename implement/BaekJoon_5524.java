package implement;

import java.util.Scanner;

public class BaekJoon_5524 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine(); // 개행 문자 제거

        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            String result = str.toLowerCase();
            System.out.println(result);
        }

        sc.close(); // 스캐너 닫기
    }
}
