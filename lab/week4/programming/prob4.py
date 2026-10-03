"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 04
      사각형을 나타내는 Rectangle 클래스를 작성한다. 면적 계산과 두 사각형의 겹침 여부를 판단한다.
설계:
  - 클래스 Rectangle
      인스턴스 변수: x, y (좌측 상단 좌표), width, height (너비와 높이)
      __init__(self, x, y, w, h) : 생성자
      __str__(self)              : 좌표와 크기를 문자열로 반환
      setX/getX, setY/getY, setWidth/getWidth, setHeight/getHeight : 접근자와 설정자
      getArea()  : width * height 반환
      overlap(r) : 두 사각형이 겹치면 True, 아니면 False
          → 한 사각형이 다른 사각형의 완전히 왼쪽/오른쪽/위/아래에 있으면 겹치지 않음.
            (화면 좌표계: y가 아래로 갈수록 증가한다고 가정)
  - test_prob4() : 겹치는 경우와 겹치지 않는 경우를 모두 확인
"""


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getWidth(self):
        return self.width

    def setWidth(self, w):
        self.width = w

    def getHeight(self):
        return self.height

    def setHeight(self, h):
        self.height = h

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        if self.x + self.width <= r.x or r.x + r.width <= self.x:
            return False   # 좌우로 떨어져 있음
        if self.y + self.height <= r.y or r.y + r.height <= self.y:
            return False   # 위아래로 떨어져 있음
        return True


def print_overlap(name1, r1, name2, r2):
    if r1.overlap(r2):
        print(f"{name1}과 {name2}는 서로 겹칩니다.")
    else:
        print(f"{name1}과 {name2}는 서로 겹치지 않습니다.")


def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)
    r3 = Rectangle(200, 200, 50, 50)
    print(r1, "면적:", r1.getArea())
    print(r2, "면적:", r2.getArea())
    print(r3, "면적:", r3.getArea())
    print_overlap("r1", r1, "r2", r2)
    print_overlap("r1", r1, "r3", r3)


if __name__ == "__main__":
    test_prob4()
