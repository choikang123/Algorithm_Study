#include<iostream>
using namespace std;

// 전역 변수 선언: 두 행렬의 행과 열 정보를 저장하는 변수
int N, M, I, J;

// 두 행렬의 덧셈 또는 뺄셈을 수행하는 함수
void add_or_sub_matrix(int** mat1, int** mat2, char opr) {
    // 행렬의 크기가 다르면 연산 불가능 -> 오류 출력
    if (N != I || M != J) {
        cout << "n" << endl << endl;  // 형식에 맞게 줄 바꿈 포함
        return;
    }

    int R = N;  // 결과 행렬의 행 수
    int C = M;  // 결과 행렬의 열 수

    // 결과 행렬을 위한 동적 메모리 할당
    int** ret = new int* [R];
    for (int i = 0; i < R; i++) {
        ret[i] = new int[C];
    }

    // 행렬 덧셈 또는 뺄셈 수행
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (opr == '+') {
                ret[i][j] = mat1[i][j] + mat2[i][j];
            } else {
                ret[i][j] = mat1[i][j] - mat2[i][j];
            }
        }
    }

    // 결과 행렬 출력
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cout << ret[i][j];
            if (j < C - 1) cout << " ";  // 마지막 열이 아니면 공백 추가
        }
        cout << endl;
    }
    cout << endl;

    // 결과 행렬 메모리 해제
    for (int i = 0; i < R; i++) {
        delete[] ret[i];
    }
    delete[] ret;
}

// 행렬 곱셈 수행 함수
void multi_matrix(int** mat1, int** mat2) {
    // 곱셈이 가능한지 확인: mat1의 열 수 == mat2의 행 수
    if (M != I) {
        cout << "n" << endl << endl;
        return;
    }

    // 행렬 곱셈 수행
    for (int i = 0; i < N; i++) {       // 결과 행
        for (int j = 0; j < J; j++) {   // 결과 열
            int sum = 0;
            for (int k = 0; k < M; k++) {
                sum += mat1[i][k] * mat2[k][j];
            }
            cout << sum;
            if (j < J - 1) cout << " ";  // 마지막 열이 아니면 공백 추가
        }
        cout << endl;
    }
    cout << endl;
}

// 행렬식(Determinant) 계산 함수: n x n 정방행렬만 가능
int determinant(int** mat, int n) {
    // 기본 조건: 1x1 행렬의 경우 행렬식은 자기 자신
    if (n == 1) {
        return mat[0][0];
    }

    int det = 0; // 결과 행렬식 저장

    // 부분 행렬(여인수) 생성을 위한 메모리 할당
    int** sub_matrix = new int* [n - 1];
    for (int i = 0; i < n - 1; i++) {
        sub_matrix[i] = new int[n - 1];
    }

    // 첫 번째 행 기준으로 여인수 전개
    for (int j = 0; j < n; j++) {
        // sub_matrix 구성: 0행, j열을 제외한 나머지로 구성
        for (int row = 1; row < n; row++) {
            int col_index = 0;  // 부분 행렬의 열 인덱스
            for (int col = 0; col < n; col++) {
                if (col == j) continue;  // j열 제외
                sub_matrix[row - 1][col_index++] = mat[row][col];
            }
        }

        // 부호 결정: (-1)^(행+열) = (-1)^j, i=0
        int sign = (j % 2 == 0) ? 1 : -1;

        // 재귀적으로 행렬식 계산 및 누적
        det += sign * mat[0][j] * determinant(sub_matrix, n - 1);
    }

    // sub_matrix 메모리 해제
    for (int i = 0; i < n - 1; i++) {
        delete[] sub_matrix[i];
    }
    delete[] sub_matrix;

    return det;
}

int main(void) {
    // 입출력 속도 향상 및 C와의 동기화 해제
    cin.tie(0);
    ios_base::sync_with_stdio(0);

    // 두 행렬의 크기 입력
    cin >> N >> M >> I >> J;

    // 첫 번째 행렬 동적 메모리 할당
    int** matrix1 = new int* [N];
    for (int i = 0; i < N; i++) {
        matrix1[i] = new int[M];
    }

    // 두 번째 행렬 동적 메모리 할당
    int** matrix2 = new int* [I];
    for (int i = 0; i < I; i++) {
        matrix2[i] = new int[J];
    }

    // 첫 번째 행렬 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> matrix1[i][j];
        }
    }

    // 두 번째 행렬 입력
    for (int i = 0; i < I; i++) {
        for (int j = 0; j < J; j++) {
            cin >> matrix2[i][j];
        }
    }

    // 덧셈, 뺄셈 결과 출력
    add_or_sub_matrix(matrix1, matrix2, '+');
    add_or_sub_matrix(matrix1, matrix2, '-');

    // 곱셈 결과 출력
    multi_matrix(matrix1, matrix2);

    // 첫 번째 행렬의 행렬식 출력 (정방행렬일 때만)
    if (N == M) {
        cout << determinant(matrix1, N) << endl << endl;
    } else {
        cout << "n" << endl << endl;
    }

    // 두 번째 행렬의 행렬식 출력 (정방행렬일 때만)
    if (I == J) {
        cout << determinant(matrix2, I);
    } else {
        cout << "n" << endl << endl;
    }

    // 메모리 해제
    for (int i = 0; i < N; i++) {
        delete[] matrix1[i];
    }
    delete[] matrix1;

    for (int i = 0; i < I; i++) {
        delete[] matrix2[i];
    }
    delete[] matrix2;

    return 0;
}