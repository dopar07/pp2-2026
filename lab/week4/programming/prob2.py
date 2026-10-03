"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 02
      로켓을 나타내는 Rocket 클래스를 작성해보자.
설계:
  - 클래스 Rocket
      인스턴스 변수: x, y (현재 로켓의 위치)
      __init__(self, x=0, y=0) : 생성자 (Rocket()으로도 생성할 수 있도록 기본값 0)
      __str__(self)            : 로켓의 위치를 문자열로 반환
      moveUp(self)             : y좌표를 1 증가
  - test_prob2() : 로켓 생성 → 높이 출력 → moveUp() → 높이 출력
"""


class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"로켓의 위치: ({self.x}, {self.y})"

    def moveUp(self):
        self.y += 1


def test_prob2():
    myRocket = Rocket()
    print("로켓의 높이:", myRocket.y)

    myRocket.moveUp()
    print("로켓의 높이:", myRocket.y)
    print(myRocket)


if __name__ == "__main__":
    test_prob2()
