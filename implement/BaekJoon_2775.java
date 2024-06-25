package implement;

import java.util.Scanner;

public class BaekJoon_2775 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int[][] apt = new int[15][15];

        for (int i = 0; i < 15; i++) {
            apt[0][i] = i; // 0층 i호
            apt[i][1] = 1; // i층 1호
        }

        for (int i = 1; i < 15; i++) {
            for (int j = 2; j < 15; j++) {
                apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
                // 같은 층의 전호수 + 아래층의 같은호수
            }
        }
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int k = sc.nextInt();
            int n = sc.nextInt();
            System.out.println(apt[k][n]);
        }
    }
}
