contacts = {}

while True:
    print("연락처 추가")
    print("연락처 삭제")
    print("연락처 검색")
    print("연락처 출력")
    print("종료")
    i = int(input("메뉴 항목을 선택하세요: "))

    if i == 1:
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        contacts[name] = phone
        print(f"{name}의 연락처가 추가되었습니다.")
    elif i == 2:
        name = input("삭제할 이름을 입력하세요: ")
        if name in contacts:
            del contacts[name]
            print(f"{name}의 연락처가 삭제되었습니다.")
        else:
            print(f"{name}의 연락처가 존재하지 않습니다.")
    elif i == 3:
        name = input("검색할 이름을 입력하세요: ")
        if name in contacts:
            print(f"{name}의 전화번호는 {contacts[name]}입니다.")
        else:
            print(f"{name}의 연락처가 존재하지 않습니다.")
    elif i == 4:
        print("연락처 목록:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif i == 5:
        print("프로그램을 종료합니다.")
        break

