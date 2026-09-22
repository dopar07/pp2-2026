# health.txt를 읽어 BMI를 계산하고 Turtle로 표를 그리는 GUI 프로그램
#
# 실행: python bmi_table.py            (창에 표 출력)
#       python bmi_table.py --save     (표를 그린 뒤 result.png로 저장)

import os
import sys
import turtle

from bmi import read_health_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "health.txt")
RESULT_FILE = os.path.join(BASE_DIR, "result.png")

FONT_NAME = "맑은 고딕"
# 글꼴 크기를 음수로 주면 포인트가 아닌 픽셀 단위가 되어
# 윈도우 화면 배율(125%, 150% 등)과 관계없이 표 칸 크기에 맞게 그려진다.
TITLE_FONT = (FONT_NAME, -26, "bold")
HEADER_FONT = (FONT_NAME, -16, "bold")
CELL_FONT = (FONT_NAME, -16, "normal")
LEGEND_FONT = (FONT_NAME, -13, "normal")

HEADERS = ["전화번호", "이름", "키(cm)", "몸무게(kg)", "BMI", "소견"]
COL_WIDTHS = [170, 100, 100, 120, 90, 100]
ROW_HEIGHT = 36
MARGIN = 40
TITLE_SPACE = 60

HEADER_COLOR = "#4a6fa5"
STRIPE_COLOR = "#eef2f8"
CATEGORY_COLORS = {
    "저체중": "#2b7bb9",
    "정상": "#2e8b57",
    "과체중": "#e08a00",
    "비만": "#d03030",
}


def fmt_number(value: float) -> str:
    """정수면 소수점 없이, 아니면 소수 첫째 자리까지 표시한다."""
    return str(int(value)) if value == int(value) else f"{value:.1f}"


def fill_rect(t: turtle.Turtle, x: float, y: float, w: float, h: float, color: str):
    """(x, y)를 왼쪽 위 꼭짓점으로 하는 사각형을 색칠한다."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    for length in (w, h, w, h):
        t.forward(length)
        t.right(90)
    t.end_fill()


def line(t: turtle.Turtle, x1: float, y1: float, x2: float, y2: float):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()


def write_center(t: turtle.Turtle, x: float, y: float, text: str, font, color="black"):
    """(x, y)를 세로 중심으로 하여 가운데 정렬로 글자를 쓴다."""
    t.penup()
    t.goto(x, y - abs(font[1]) * 0.7)
    t.color(color)
    t.write(text, align="center", font=font)


def draw_table(t: turtle.Turtle, records: list[dict]):
    table_w = sum(COL_WIDTHS)
    table_h = ROW_HEIGHT * (len(records) + 1)
    left = -table_w / 2
    top = table_h / 2 - 5  # 제목·표·범례 전체가 창 가운데 오도록

    # 제목
    write_center(t, 0, top + TITLE_SPACE / 2, "BMI 측정 결과표", TITLE_FONT)

    # 헤더 배경 및 줄무늬 배경
    t.pencolor(HEADER_COLOR)
    fill_rect(t, left, top, table_w, ROW_HEIGHT, HEADER_COLOR)
    for i in range(len(records)):
        if i % 2 == 1:
            y = top - ROW_HEIGHT * (i + 1)
            t.pencolor(STRIPE_COLOR)
            fill_rect(t, left, y, table_w, ROW_HEIGHT, STRIPE_COLOR)

    # 격자선
    t.pencolor("#555555")
    t.pensize(1)
    for r in range(len(records) + 2):
        y = top - ROW_HEIGHT * r
        line(t, left, y, left + table_w, y)
    x = left
    for w in [0] + COL_WIDTHS:
        x += w
        line(t, x, top, x, top - table_h)
    # 바깥 테두리와 헤더 아래 선은 굵게
    t.pensize(2)
    line(t, left, top - ROW_HEIGHT, left + table_w, top - ROW_HEIGHT)
    for x1, y1, x2, y2 in [(left, top, left + table_w, top),
                           (left + table_w, top, left + table_w, top - table_h),
                           (left + table_w, top - table_h, left, top - table_h),
                           (left, top - table_h, left, top)]:
        line(t, x1, y1, x2, y2)
    t.pensize(1)

    # 글자
    centers = []
    x = left
    for w in COL_WIDTHS:
        centers.append(x + w / 2)
        x += w

    header_y = top - ROW_HEIGHT / 2
    for cx, text in zip(centers, HEADERS):
        write_center(t, cx, header_y, text, HEADER_FONT, "white")

    for i, rec in enumerate(records):
        cy = top - ROW_HEIGHT * (i + 1) - ROW_HEIGHT / 2
        cells = [
            rec["phone"],
            rec["name"],
            fmt_number(rec["height"]),
            fmt_number(rec["weight"]),
            f"{rec['bmi']:.1f}",
            rec["category"],
        ]
        for col, (cx, text) in enumerate(zip(centers, cells)):
            color = CATEGORY_COLORS.get(text, "black") if col == 5 else "black"
            write_center(t, cx, cy, text, CELL_FONT, color)

    # 범례
    legend = "소견 기준(WHO): 저체중 < 18.5 ≤ 정상 < 25 ≤ 과체중 < 30 ≤ 비만"
    write_center(t, 0, top - table_h - 25, legend, LEGEND_FONT, "#666666")


def save_screenshot(screen: turtle._Screen, path: str):
    """그려진 turtle 창 영역을 캡처해 PNG로 저장한다."""
    from PIL import ImageGrab

    canvas = screen.getcanvas()
    # 다른 창에 가려진 채로 캡처되지 않도록 창을 맨 앞으로 올린다
    root = canvas.winfo_toplevel()
    root.attributes("-topmost", True)
    root.lift()
    root.focus_force()
    root.update()
    root.after(300)
    canvas.update()
    x, y = canvas.winfo_rootx(), canvas.winfo_rooty()
    w, h = canvas.winfo_width(), canvas.winfo_height()
    ImageGrab.grab(bbox=(x, y, x + w, y + h)).save(path)
    print(f"결과 화면 저장: {path}")


def main():
    if sys.platform == "win32":
        # 고해상도 화면에서 글자가 흐려지거나 캡처 좌표가 어긋나지 않도록 설정
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass

    _, records = read_health_file(DATA_FILE)
    if not records:
        print("health.txt에 표시할 데이터가 없습니다.")
        return

    width = sum(COL_WIDTHS) + MARGIN * 2
    height = ROW_HEIGHT * (len(records) + 1) + TITLE_SPACE + MARGIN * 2 + 20

    screen = turtle.Screen()
    screen.title("BMI 계산 결과")
    screen.setup(width + 20, height + 20)
    screen.bgcolor("white")
    screen.tracer(0)  # 한 번에 그리기

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    draw_table(t, records)
    screen.update()

    if "--save" in sys.argv:
        screen.ontimer(lambda: (save_screenshot(screen, RESULT_FILE), screen.bye()), 800)

    turtle.done()


if __name__ == "__main__":
    main()
