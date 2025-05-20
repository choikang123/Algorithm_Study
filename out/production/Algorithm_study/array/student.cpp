#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int studentNumbers[10];
    int korean[10];
    int english[10];
    int math[10];
    int total[10];
    double average[10];

    for (int i = 0; i < 10; i++) {
        cout << "학생 " << i + 1 << "의 학번, 국어, 영어, 수학 성적 입력: ";
        cin >> studentNumbers[i]; 
        cin >> korean[i];       
        cin >> english[i];        
        cin >> math[i];         


        total[i] = korean[i] + english[i] + math[i];


        average[i] = total[i] / 3.0;
    }

    cout << "학번   국어   영어   수학   총점   평균" << endl;
    cout << "*****************************************" << endl;

    for (int i = 0; i < 10; i++) {
        cout << setw(3) << studentNumbers[i]
            << setw(4) << korean[i]
            << setw(4) << english[i]
            << setw(4) << math[i]
            << setw(4) << total[i]
            << setw(5) << fixed << setprecision(1) << average[i]
            << endl;
    }

    return 0;
}
