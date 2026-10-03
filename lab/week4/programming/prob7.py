"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 07
      사람들의 연락처를 저장하는 PhoneBook 클래스를 작성한다. 딕셔너리를 이용하여 연락처를 저장한다.
설계:
  - 클래스 PhoneBook
      인스턴스 변수: contacts (딕셔너리)
          키: name, 값: {"mobile": ..., "office": ..., "email": ...} 딕셔너리
      __init__(self) : 빈 딕셔너리 생성
      __str__(self)  : 저장된 모든 연락처를 문자열로 변환 (값이 None인 항목은 생략)
      add(self, name, mobile=None, office=None, email=None) : 한 사람의 연락처 추가
  - test_prob7() : 교재 예시대로 두 명을 추가하고 출력
"""


class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = {"mobile": mobile, "office": office, "email": email}

    def __str__(self):
        labels = {"mobile": "mobile phone:", "office": "office phone:", "email": "email address:"}
        entries = []
        for name, info in self.contacts.items():
            lines = [name]
            for key, label in labels.items():
                if info[key] is not None:
                    lines.append(f"{label:<15}{info[key]}")
            entries.append("\n".join(lines))
        return "\n\n".join(entries)


def test_prob7():
    obj = PhoneBook()
    obj.add("Kim", office="1234567", email="kim@company.com")
    obj.add("Park", office="2345678", email="park@company.com")
    print(obj)


if __name__ == "__main__":
    test_prob7()
