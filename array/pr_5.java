package array;

import java.util.ArrayList;
import java.util.Arrays;

public class pr_5 {
    public static int[] solution(int[] answer) {
        int[][] supo = {
                {1,2,3,4,5},
                {2,1,2,3,2,4,2,5},
                {3,3,1,1,2,2,4,4,5,5}
        };

        int[] score = new int[3];

        for (int i = 0; i < supo.length; i++) {
            for (int j = 0; j < answer.length; j++) {
                if(answer[j] == supo[i][j % supo[i].length]) {
                    score[i]++; //각 수포자에 대한 점수가 쌓임
                }
            }
        }

        //score가 높은 score의 수포자를 결과로 내는데 값이 같으면 수포자 번호 오름차순 1부터
        int maxScore = Arrays.stream(score).max().getAsInt();
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            if(score[i] == maxScore) {
                result.add(i+1);
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
