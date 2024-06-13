package implement;

import java.util.ArrayList;
import java.util.Scanner;

public class BaekJoon_1546 {
    public static void main(String[] args) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double avg = 0;

        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            arrayList.add(a);
        }

        int max_value = max(arrayList);

        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += (arrayList.get(i) / (double)max_value) * 100;
        }
        avg = sum / n;

        System.out.println(avg);
    }

    private static int max(ArrayList<Integer> arrayList) {
        int max_value = arrayList.get(0);
        for (int i = 1; i < arrayList.size(); i++) {
            if (arrayList.get(i) > max_value) {
                max_value = arrayList.get(i);
            }
        }
        return max_value;
    }
}
