package stack;

import java.util.*;

public class BaekJoon_10828 {
    public static void main(String[] args) {
        Deque<Integer> stack = new ArrayDeque<>();
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();  // nextInt() 후 남은 줄바꿈 문자를 소비합니다.

        for (int i = 0; i < n; i++) {
            String command = sc.nextLine();

            if (command.startsWith("push")) {
                int value = Integer.parseInt(command.split(" ")[1]);
                stack.push(value);
            } else if (command.equals("pop")) {
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(stack.pop());
                }
            } else if (command.equals("size")) {
                System.out.println(stack.size());
            } else if (command.equals("empty")) {
                System.out.println(stack.isEmpty() ? 1 : 0);
            } else if (command.equals("top")) {
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(stack.peek());
                }
            }
        }
    }
}
