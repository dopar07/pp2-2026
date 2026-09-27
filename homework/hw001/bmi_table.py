# health.txt를 읽어 BMI를 계산하고 Turtle로 표를 그리는 프로그램
#
# 실행 방법: hw001 폴더에서  python bmi_table.py

import turtle
from bmi import read_health_file

# 표의 제목 줄과 각 칸의 너비
HEADERS = ["전화번호", "이름", "키(cm)", "몸무게(kg)", "BMI", "소견"]
COL_WIDTHS = [170, 100, 100, 120, 90, 100]
ROW_HEIGHT = 36
MARGIN = 40                             # 표 바깥 여백
TITLE_SPACE = 60                        # 표 위 제목 공간

# 글꼴 (크기를 음수로 쓰면 픽셀 단위라 화면 배율이 달라도 칸에 맞게 나온다)
TITLE_FONT = ("맑은 고딕", -26, "bold")
CELL_FONT = ("맑은 고딕", -16, "normal")
LEGEND_FONT = ("맑은 고딕", -13, "normal")


def draw_rect(t, x, y, width, height, color):
    """(x, y)를 왼쪽 위 꼭짓점으로 하는 색칠된 사각형을 그린다."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)                     # 오른쪽을 보게 한다
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()


def write_text(t, x, y, text, font, color):
    """(x, y) 위치에 글자를 가운데 정렬로 쓴다."""
    t.penup()
    t.goto(x, y - 10)                   # 글자가 칸 세로 가운데 오도록 조금 내린다
    t.color(color)
    t.write(text, align="center", font=font)


def fmt_number(value):
    """175.0처럼 정수인 값은 175로, 아니면 소수 첫째 자리까지 글자로 만든다."""
    if value == int(value):
        return str(int(value))
    return str(round(value, 1))


def category_color(category):
    """소견에 따라 글자 색을 정한다."""
    if category == "저체중":
        return "blue"
    elif category == "정상":
        return "green"
    elif category == "과체중":
        return "orange"
    else:
        return "red"


def draw_row(t, left, top, cells, bg_color, text_color):
    """한 줄(행)을 그린다. cells는 칸에 들어갈 글자 리스트."""
    x = left
    for i in range(len(cells)):
        width = COL_WIDTHS[i]
        t.pencolor("gray")
        draw_rect(t, x, top, width, ROW_HEIGHT, bg_color)

        color = text_color
        if i == 5 and text_color == "black":     # 소견 칸은 색을 다르게
            color = category_color(cells[i])
        write_text(t, x + width / 2, top - ROW_HEIGHT / 2, cells[i], CELL_FONT, color)

        x = x + width


def draw_table(t, records):
    """제목, 제목 줄, 데이터 줄 순서로 표 전체를 그린다."""
    table_width = sum(COL_WIDTHS)
    left = -table_width / 2
    top = ROW_HEIGHT * (len(records) + 1) / 2

    # 표 제목
    write_text(t, 0, top + 35, "BMI 측정 결과표", TITLE_FONT, "black")

    # 제목 줄
    draw_row(t, left, top, HEADERS, "steelblue", "white")

    # 데이터 줄
    for i in range(len(records)):
        phone, name, height, weight, bmi, category = records[i]
        cells = [phone, name, fmt_number(height), fmt_number(weight), f"{bmi:.1f}", category]

        if i % 2 == 0:                  # 줄무늬 배경
            bg_color = "white"
        else:
            bg_color = "aliceblue"

        row_top = top - ROW_HEIGHT * (i + 1)
        draw_row(t, left, row_top, cells, bg_color, "black")

    # 표 아래 소견 기준(범례)
    legend = "소견 기준(WHO): 저체중 < 18.5 ≤ 정상 < 25 ≤ 과체중 < 30 ≤ 비만"
    table_bottom = top - ROW_HEIGHT * (len(records) + 1)
    write_text(t, 0, table_bottom - 20, legend, LEGEND_FONT, "gray")


def main():
    records = read_health_file("health.txt")
    if len(records) == 0:
        print("health.txt에 표시할 데이터가 없습니다.")
        return

    # 데이터 줄 수에 맞춰 창 크기를 정한다
    width = sum(COL_WIDTHS) + MARGIN * 2
    height = ROW_HEIGHT * (len(records) + 1) + TITLE_SPACE + MARGIN * 2 + 20

    screen = turtle.Screen()
    screen.title("BMI 계산 결과")
    screen.setup(width + 20, height + 20)
    screen.tracer(0)                    # 그리는 과정을 생략하고 한 번에 보여준다

    t = turtle.Turtle()
    t.hideturtle()
    draw_table(t, records)

    screen.update()
    turtle.done()


if __name__ == "__main__":
    main()
