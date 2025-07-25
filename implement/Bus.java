package algo;

import java.util.*;

public class Bus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // 지역 수
        int m = sc.nextInt(); // 버스 노선 수

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) { // 1번부터 n번 지역이므로 0번은 안 씀
            graph.add(new ArrayList<>());
        }

        // 간선 입력
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph.get(u).add(v);
        }

        int start = sc.nextInt(); // 출발 지역

        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();

        // BFS 시작
        visited[start] = true;
        queue.offer(start);

        int count = 1; // 출발 지역도 포함하므로 1부터 시작

        while (!queue.isEmpty()) {
            int current = queue.poll();

            for (int next : graph.get(current)) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(next);
                    count++;
                }
            }
        }
     /* 8 7
        3 4
        2 7
        2 6
        3 7
        5 1
        6 2
        6 5
        6

        5 (6,2,5,7,1)
        */
        System.out.println(count);
    }
}
