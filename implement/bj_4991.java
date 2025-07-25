package implement;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Point {
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class bj_4991 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken()); //열
            int h = Integer.parseInt(st.nextToken()); //행

            if(w == 0 && h == 0) break;

            char[][] map = new char[h][w];
            for (int i = 0; i < h; i++) {
                map[i] = br.readLine().toCharArray();
            }

            Point start = null;
            List<Point> dirtyPoints = new ArrayList<>();

            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if(map[i][j] == 'o') {
                        start = new Point(i, j);
                    } else if(map[i][j] == '*') {
                        dirtyPoints.add(new Point(i, j));
                    }
                }
            }


        }
    }
}