#include <iostream>
#include <cstring>
using namespace std;

int main(){
  int rows=5;
  char* string_arr[rows];

  // 문자열을 입력 받아야 하고
  cout << "5개의 문자열을 적어주세요: " <<endl;
  // 5번 입력 받아야 한다 최대 50자
  for(int i=0; i<=rows; i++){
    cin.getline(string_arr[i],50); // 동적으로 할당하는게 아니다
    char temp[50]; // 먼저 임시로 할당해줘야 함
    cin.getline(temp,50);
    
    //동적할당
    int len=strlen(temp);
    string_arr[i]=
  }

  // 입력받은 문자열 만큼만 동적으로 메모리 할당하고


  // 출력하고


  // 메모리 누수 방지를 위해 메모리 해제
}