#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#define CONTACT_MAX 100

using namespace std;

// 주소록 관리 클래스
class PhoneBook {
private:
    // 연락처 정보 구조체
    struct Person {
        char fullName[20];
        char phoneNumber[20];
        char homeAddress[120];
        char birthDate[15];
    };

    Person contactList[CONTACT_MAX];  // 연락처 배열
    int totalContacts = 0;            // 현재 저장된 연락처 수

public:
    // 1. 전체 목록 출력 기능
    void showAllContacts() {
        if (totalContacts == 0) {
            cout << "※ 저장된 연락처가 없습니다.\n";
            return;
        }
        
        cout << "\n===== 연락처 목록 =====\n";
        for (int i = 0; i < totalContacts; i++) {
            cout << "[" << i + 1 << "] ";
            cout << "이름: " << contactList[i].fullName << ", ";
            cout << "연락처: " << contactList[i].phoneNumber << ", ";
            cout << "주소: " << contactList[i].homeAddress << ", ";
            cout << "생년월일: " << contactList[i].birthDate << "\n";
        }
        cout << "=====================\n\n";
    }

    // 2. 새 연락처 추가 기능
    void insertContact(const char* name, const char* phone, const char* address, const char* birth) {
        if (totalContacts >= CONTACT_MAX) {
            cout << "※ 주소록이 가득 찼습니다. (최대 " << CONTACT_MAX << "개)\n";
            return;
        }

        // 안전하게 복사
        strncpy(contactList[totalContacts].fullName, name, sizeof(contactList[totalContacts].fullName) - 1);
        strncpy(contactList[totalContacts].phoneNumber, phone, sizeof(contactList[totalContacts].phoneNumber) - 1);
        strncpy(contactList[totalContacts].homeAddress, address, sizeof(contactList[totalContacts].homeAddress) - 1);
        strncpy(contactList[totalContacts].birthDate, birth, sizeof(contactList[totalContacts].birthDate) - 1);
        
        // 문자열 끝에 null 문자 추가
        contactList[totalContacts].fullName[sizeof(contactList[totalContacts].fullName) - 1] = '\0';
        contactList[totalContacts].phoneNumber[sizeof(contactList[totalContacts].phoneNumber) - 1] = '\0';
        contactList[totalContacts].homeAddress[sizeof(contactList[totalContacts].homeAddress) - 1] = '\0';
        contactList[totalContacts].birthDate[sizeof(contactList[totalContacts].birthDate) - 1] = '\0';

        totalContacts++;
        cout << "✓ " << name << "님의 연락처가 추가되었습니다.\n";
    }

    // 3. 연락처 검색 기능
    int findContact(const char* searchNumber) {
        if (totalContacts == 0) {
            cout << "※ 저장된 연락처가 없습니다.\n";
            return -1;
        }

        for (int i = 0; i < totalContacts; i++) {
            if (strcmp(contactList[i].phoneNumber, searchNumber) == 0) {
                cout << "\n▶ 검색 결과:\n";
                cout << "이름: " << contactList[i].fullName << "\n";
                cout << "연락처: " << contactList[i].phoneNumber << "\n";
                cout << "주소: " << contactList[i].homeAddress << "\n";
                cout << "생년월일: " << contactList[i].birthDate << "\n\n";
                return i;
            }
        }
        
        cout << "※ " << searchNumber << " 번호를 가진 연락처를 찾을 수 없습니다.\n";
        return -1;
    }

    // 4. 연락처 삭제 기능
    void deleteContact(const char* phoneNumber) {
        int position = findContact(phoneNumber);
        
        if (position == -1) {
            return; // 이미 findContact에서 오류 메시지 출력됨
        }
        
        // 해당 위치 이후의 연락처들을 한 칸씩 앞으로 이동
        for (int i = position; i < totalContacts - 1; i++) {
            contactList[i] = contactList[i + 1];
        }
        
        totalContacts--;
        cout << "✓ 연락처가 성공적으로 삭제되었습니다.\n";
    }
};

int main() {
    PhoneBook addressBook;
    
    // 기본 연락처 추가
    addressBook.insertContact("박서준", "010-1111-2222", "서울시 마포구", "1988-10-16");
    addressBook.insertContact("김유정", "010-3333-4444", "서울시 송파구", "1989-09-22");
    addressBook.insertContact("정해인", "010-5555-6666", "부산시 해운대구", "1990-04-01");
    
    // 전체 목록 출력
    addressBook.showAllContacts();
    
    // 연락처 검색
    cout << "연락처 검색 테스트:\n";
    addressBook.findContact("010-3333-4444");
    
    // 연락처 삭제
    cout << "연락처 삭제 테스트:\n";
    addressBook.deleteContact("010-3333-4444");
    
    // 삭제 후 목록 다시 출력
    cout << "삭제 후 연락처 목록:\n";
    addressBook.showAllContacts();
    
    return 0;
}
