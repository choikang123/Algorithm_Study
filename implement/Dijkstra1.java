package implement;

import java.util.Scanner;

public class Dijkstra1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();

        int[][] graph = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if(i==j) continue; //자바에서 int 배열은 기본적으로 0으로 초기화 됨
                graph[i][j]=Integer.MAX_VALUE;
            }
        }

        for(int i = 1; i <= m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            graph[u][v]=Math.min(graph[u][v],w);
        }
        dijkstra(n,s,graph);
    }

    private static void dijkstra(int n, int start, int[][] graph) {
        boolean[] s = new boolean[n + 1]; // 찾은 정점들의 집합
        int[] distance=new int[n+1];
        s[start]=true; // 처음 2번을 s에 넣어주고 시작정점을 넣어줌
/*        S = [false, false, true, false, false, false]
        인덱스  0      1      2     3      4      5     */

    }
/*  5 5 2 정점의 갯수 간선의 갯수 시작 정점
    2 1 3 시작 끝 가중치
    2 3 8
    1 4 2
    3 4 1
    4 5 5*/
}
