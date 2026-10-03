"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 09
      터틀 그래픽에서 각각의 거북이는 객체이다. 2개의 거북이를 생성하여 서로 다른 방향으로 움직이도록 한다.
설계:
  - turtle.Turtle 클래스의 인스턴스 2개(kim, lee)를 생성 → 각 객체는 자신의 위치/방향/색을 따로 가진다.
  - make_turtle(color, x, y, heading) : 거북이 객체를 생성하고 시작 위치/방향을 설정하여 반환
  - move_stairs(t, steps)           : 거북이를 "앞으로 → 오른쪽 90도 → 조금 전진 → 왼쪽 90도"
                                      반복으로 계단 모양 경로로 이동시킴
  - test_prob9() : 오른쪽으로 가는 거북이와 왼쪽으로 가는 거북이를 만들어 번갈아 이동
"""
import turtle


def make_turtle(color, x, y, heading):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.dot(15)          # 시작 위치 표시
    t.pendown()
    return t


def move_stairs(t, steps):
    for _ in range(steps):
        t.forward(80)
        t.right(90)
        t.forward(20)
        t.left(90)
    t.forward(80)


def test_prob9():
    screen = turtle.Screen()
    screen.title("prob9 - 두 거북이 객체")

    kim = make_turtle("black", -250, 50, 0)     # 오른쪽(동쪽)으로 이동
    lee = make_turtle("blue", 250, -50, 180)    # 왼쪽(서쪽)으로 이동

    # 두 객체를 번갈아 움직여 서로 다른 방향으로 이동하는 모습을 보여준다.
    for _ in range(2):
        move_stairs(kim, 1)
        move_stairs(lee, 1)

    screen.exitonclick()


if __name__ == "__main__":
    test_prob9()
