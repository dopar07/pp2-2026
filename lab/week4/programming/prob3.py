"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 03
      상자를 나타내는 Box 클래스를 작성하고, 가로/세로/높이를 100으로 설정한 뒤
      상자 정보와 부피를 출력한다. 접근자와 설정자를 모두 만들어 사용한다.
설계:
  - 클래스 Box
      인스턴스 변수: length(가로), height(세로), depth(높이)
      __init__(self, l, h, d) : 생성자
      __str__(self)           : "(l, h, d)" 형태의 문자열 반환
      getLength/setLength, getHeight/setHeight, getDepth/setDepth : 접근자와 설정자
  - test_prob3() : Box(100, 100, 100) 생성 → 정보 출력 → 접근자로 부피 계산
"""


class Box:
    def __init__(self, l, h, d):
        self.length = l
        self.height = h
        self.depth = d

    def __str__(self):
        return f"({self.length}, {self.height}, {self.depth})"

    def getLength(self):
        return self.length

    def setLength(self, l):
        self.length = l

    def getHeight(self):
        return self.height

    def setHeight(self, h):
        self.height = h

    def getDepth(self):
        return self.depth

    def setDepth(self, d):
        self.depth = d


def test_prob3():
    b1 = Box(100, 100, 100)
    print(b1)
    print("상자의 부피는", b1.getHeight() * b1.getLength() * b1.getDepth())

    # 설정자 사용
    b1.setLength(200)
    print(b1)
    print("상자의 부피는", b1.getHeight() * b1.getLength() * b1.getDepth())


if __name__ == "__main__":
    test_prob3()
