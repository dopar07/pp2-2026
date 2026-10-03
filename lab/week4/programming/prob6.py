"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 06
      Person이라는 클래스를 작성한다.
설계:
  - 클래스 Person
      인스턴스 변수: name(이름), mobile(핸드폰), office(직장 전화), email(이메일)
                    mobile/office/email은 기본값(빈 문자열)을 가진다.
      __init__(self, n, m="", o="", e="") : 생성자
          → 교재 예시처럼 Person("Kim", office=..., email=...) 키워드 인자로도 호출할 수 있도록
            매개변수 이름을 mobile, office, email로 둔다.
      __str__(self) : Person 정보를 문자열로 반환
      setName/getName, setMobile/getMobile, setOffice/getOffice, setEmail/getEmail
  - test_prob6() : 교재 예시대로 p1, p2 생성 후 설정자 사용, 출력
"""


class Person:
    def __init__(self, name, mobile="", office="", email=""):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        return (f"{self.name}\n"
                f"mobile phone:  {self.mobile}\n"
                f"office phone:  {self.office}\n"
                f"email address: {self.email}")

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getMobile(self):
        return self.mobile

    def setMobile(self, mobile):
        self.mobile = mobile

    def getOffice(self):
        return self.office

    def setOffice(self, office):
        self.office = office

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email


def test_prob6():
    p1 = Person("Kim", office="1234567", email="kim@company.com")
    p2 = Person("Park", office="2345678")
    p2.setEmail("park@company.com")
    print(p1)
    print()
    print(p2)


if __name__ == "__main__":
    test_prob6()
