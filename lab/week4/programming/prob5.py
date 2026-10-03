"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 05
      삼각형을 나타내는 Triangle 클래스를 작성한다. 내각의 합이 180도인지 확인한다.
설계:
  - 클래스 Triangle
      인스턴스 변수: angle1, angle2, angle3 (각 각도), numberOfSides (변의 개수, 기본값 3)
      __init__(self, a1, a2, a3) : 생성자
      __str__(self)              : 삼각형 정보를 문자열로 반환
      setAngle1/getAngle1, ... , getNumberOfSides : 접근자와 설정자
      checkAngles() : 세 각의 합이 180이면 True, 아니면 False
  - test_prob5() : 올바른 삼각형과 잘못된 삼각형을 각각 확인
"""


class Triangle:
    def __init__(self, a1, a2, a3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3
        self.numberOfSides = 3

    def __str__(self):
        return (f"Triangle(angle1={self.angle1}, angle2={self.angle2}, "
                f"angle3={self.angle3}, numberOfSides={self.numberOfSides})")

    def getAngle1(self):
        return self.angle1

    def setAngle1(self, a):
        self.angle1 = a

    def getAngle2(self):
        return self.angle2

    def setAngle2(self, a):
        self.angle2 = a

    def getAngle3(self):
        return self.angle3

    def setAngle3(self, a):
        self.angle3 = a

    def getNumberOfSides(self):
        return self.numberOfSides

    def checkAngles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


def test_prob5():
    triangle = Triangle(90, 30, 60)
    print(triangle)
    print(triangle.checkAngles())

    triangle.setAngle3(70)
    print(triangle)
    print(triangle.checkAngles())


if __name__ == "__main__":
    test_prob5()
