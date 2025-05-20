#include <stdio.h>
#include <math.h>

int main() {
    int arr[] = {19, 2, 25, 92, 36, 45};
    int n = sizeof(arr) / sizeof(arr[0]);
    int min = arr[0], max = arr[0];
    double sum = 0, mean, variance = 0;

    // ① 배열에 저장된 원소들을 화면에 출력한다.
    printf("배열 원소: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
        if (arr[i] < min) min = arr[i];
        if (arr[i] > max) max = arr[i];
        sum += arr[i];
    }
    printf("\n");

    // ② 배열 원소 중에서 최솟값과 최댓값을 구해 출력한다.
    printf("최솟값: %d\n", min);
    printf("최댓값: %d\n", max);

    // ③ 배열 원소들의 평균을 구해 출력한다.
    mean = sum / n;
    printf("평균: %.2f\n", mean);

    // ④ 배열 원소들의 분산을 구해 출력한다.
    for (int i = 0; i < n; i++) {
        variance += pow(arr[i] - mean, 2);
    }
    variance /= n;
    printf("분산: %.2f\n", variance);

    return 0;
}