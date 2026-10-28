import tkinter as tk

root = tk.Tk()  # 루트를 생성
root.title("Oobuuton")  # 루트 제목을 설정
root.geometry("600x400")  # 루트 크기를 설정

def on_btn1_clicked(event):
    print(f"레벨이 클릭되었습니다.: {event}")

label = tk.Label(root, text = "객체지향윈도우프로그래밍")  # 레이블 위젯을 생성
label.bind("<Double-1>", on_btn1_clicked)  # 레이블에 이벤트를 바인딩
label.pack()  # 레이블을 배치

def on_btn1_clicked(event):
    print(f"버튼1이 클릭되었습니다.: {event}")
    label.config(text=f"버튼1이 클릭되었습니다.{event}")  # 레이블의 텍스트를 변경

btn1 = tk.Button(root, text="클릭해볼까요?", width = "100", height = 50, fg = "green")  # 버튼 위젯을 생성
btn1.bind("<Button-1>", on_btn1_clicked)  # 버튼에 이벤트를 바인딩
btn1.pack()  # 버튼을 배치



root.mainloop()  # 루트가 사용자 동작을 대기