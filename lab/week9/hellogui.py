from tkinter import *    # tkinter 모듈을 포함

window = Tk()                                # 루트 윈도우를 생성
window.title("Hello 이찬민")                  # 윈도우 제목을 설정
window.geometry("400x200")                   # 윈도우 크기를 설정

label = Label(window, text="Hello, GUI!")    # 레이블 위젯을 생성
label.pack()                                 # 레이블 위젯을 윈도우에 배치

window.mainloop()                            # 윈도우가 사용자 동작을 대기