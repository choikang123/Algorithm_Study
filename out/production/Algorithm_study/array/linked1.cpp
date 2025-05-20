#include <iostream>
#include <string>
#include <limits>
#include <locale>

class Node {
public:
    std::string name;
    int count;
    Node* next;

    Node(const std::string& name, int count) : name(name), count(count), next(nullptr) {}
};

class FriendList {
private:
    Node* head;

public:
    FriendList() : head(nullptr) {}

    // 친구 삽입 (정렬 유지: 연락횟수 내림차순)
    void insertNode(const std::string& name, int count) {
        Node* newNode = new Node(name, count);

        // 리스트가 비어있거나 제일 앞에 삽입해야 하는 경우
        if (head == nullptr || head->count < count) {
            newNode->next = head;
            head = newNode;
            return;
        }

        Node* current = head;
        while (current->next && current->next->count > count) {
            current = current->next;
        }

        newNode->next = current->next;
        current->next = newNode;
    }

    // 이름으로 삭제
    void deleteNode(const std::string& name) {
        Node* current = head;
        Node* prev = nullptr;

        while (current) {
            if (current->name == name) {
                if (prev == nullptr) { // 첫 노드
                    head = current->next;
                }
                else {
                    prev->next = current->next;
                }
                delete current;
                std::cout << "'" << name << "' 삭제 완료." << std::endl;
                return;
            }
            prev = current;
            current = current->next;
        }

        std::cout << "해당 이름의 친구를 찾을 수 없습니다." << std::endl;
    }

    // 전체 리스트 출력
    void printList() const {
        if (!head) {
            std::cout << "친구 리스트가 비어있습니다." << std::endl;
            return;
        }

        Node* current = head;
        int rank = 1;
        std::cout << "\n[카톡 친구 리스트]" << std::endl;
        while (current) {
            std::cout << rank++ << "위: " << current->name << " (연락 " << current->count << "회)" << std::endl;
            current = current->next;
        }
    }

    // 소멸자: 메모리 해제
    ~FriendList() {
        Node* current;
        while (head) {
            current = head;
            head = head->next;
            delete current;
        }
    }
};

int main() {
    // 한글 처리를 위한 로케일 설정
    std::locale::global(std::locale(""));
    std::wcout.imbue(std::locale());
    std::wcin.imbue(std::locale());

    FriendList friendList;
    int choice, count;
    std::string name;

    while (true) {
        std::cout << "\n===== 카톡 친구 관리 프로그램 =====" << std::endl;
        std::cout << "1. 친구 추가\n2. 친구 삭제\n3. 친구 목록 보기\n4. 종료" << std::endl;
        std::cout << "메뉴를 선택하세요: ";
        std::cin >> choice;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        switch (choice) {
        case 1: {
            std::cout << "이름 입력: ";
            std::getline(std::cin, name);

            if (name.empty()) {
                std::cout << "이름이 비어있어 추가할 수 없습니다." << std::endl;
                break;
            }

            std::cout << "연락 횟수 입력: ";
            std::cin >> count;
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

            friendList.insertNode(name, count);
            std::cout << "'" << name << "'님이 추가되었습니다." << std::endl;
            break;
        }
        case 2: {
            std::cout << "삭제할 친구 이름 입력: ";
            std::getline(std::cin, name);
            friendList.deleteNode(name);
            break;
        }
        case 3:
            friendList.printList();
            break;
        case 4:
            std::cout << "프로그램 종료." << std::endl;
            return 0;
        default:
            std::cout << "잘못된 입력입니다. 다시 선택하세요." << std::endl;
        }
    }

    return 0;
}
