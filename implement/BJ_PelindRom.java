package implement;

import java.util.Scanner;

public class BJ_PelindRom {
    public static void main(String[] args) {//10988
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();
        int left=0;
        int right=str.length()-1;
        boolean isPelindRom = true;

        while(left<right){
            if (str.charAt(left) == str.charAt(right)) {
                left++;
                right--;
            } else {
                isPelindRom = false;
                break;
            }
        }
        System.out.println(isPelindRom ? 1 : 0);
    }
}
