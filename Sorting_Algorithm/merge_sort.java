/*
#https://chatgpt.com/share/3c93a673-13b7-4828-898e-0eda883308a2
# 퀵정렬 알고리즘과 병합정렬 알고리즘의 차이를 알려줌
*//*


import java.util.Arrays;

public class MergeSort {
    
    public static void main(String[] args) {
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
        int[] sortedArr = mergeSort(arr);
        System.out.println(Arrays.toString(sortedArr));
    }

    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return arr; // 배열의 길이가 1 이하이면 정렬된 상태로 반환
        }

        // 배열을 두 개로 나눈다
        int mid = arr.length / 2;
        int[] leftHalf = mergeSort(Arrays.copyOfRange(arr, 0, mid));
        int[] rightHalf = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));

        // 두 부분을 병합한다
        return merge(leftHalf, rightHalf);
    }

    public static int[] merge(int[] left, int[] right) {
        int[] sortedArr = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;

        // 두 배열을 병합한다
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                sortedArr[k++] = left[i++];
            } else {
                sortedArr[k++] = right[j++];
            }
        }

        // 남아 있는 요소들을 추가한다
        while (i < left.length) {
            sortedArr[k++] = left[i++];
        }
        while (j < right.length) {
            sortedArr[k++] = right[j++];
        }

        return sortedArr;
    }
}
*/
