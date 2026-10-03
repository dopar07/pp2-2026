"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 01
      고양이를 클래스로 정의하고 몇 개의 인스턴스를 생성해보자. 접근자와 설정자를 사용해보자.
설계:
  - 클래스 Cat
      인스턴스 변수: name(이름), age(나이)
      __init__(self, name, age) : 생성자
      __str__(self)             : "이름 나이" 형태의 문자열 반환
      getName/setName, getAge/setAge : 접근자와 설정자
  - test_prob1() : 인스턴스 2개 생성 후 출력, 설정자로 값 변경 후 접근자로 확인
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


def test_prob1():
    missy = Cat('Missy', 3)
    lucky = Cat('Lucky', 5)
    print(missy)
    print(lucky)

    # 접근자와 설정자 사용
    lucky.setAge(lucky.getAge() + 1)
    print(lucky.getName(), "의 나이를 1 증가:", lucky.getAge())


if __name__ == "__main__":
    test_prob1()
