# 콜백 함수2: 객체의 메소드를 버튼의 command로 넘긴다.
from tkinter import *

class Button3Status:
    def __init__(self):
        self.status1 = ""
        self.status2 = ""
        self.status3 = ""

    def callback1(self):
        self.status1 = "Button1 clicked"
        self.print_status()

    def callback2(self):
        self.status2 = "Button2 clicked"
        self.print_status()

    def callback3(self):
        self.status3 = "Button3 clicked"
        self.print_status()

    def get_status(self):
        return [self.status1, self.status2, self.status3]

    def reset_status(self):
        self.status1 = ""
        self.status2 = ""
        self.status3 = ""
        self.print_status()

    def __str__(self):
        return f"Button 1 status: {self.status1}, Button 2 status: {self.status2}, Button 3 status: {self.status3}"

    def print_status(self):
        print(self)

button_status = Button3Status()

window = Tk()
btn1 = Button(window, text="1 출력", command=button_status.callback1)
btn1.pack(side=LEFT)
btn2 = Button(window, text="2 출력", command=button_status.callback2)
btn2.pack(side=LEFT)
btn3 = Button(window, text="3 출력", command=button_status.callback3)
btn3.pack(side=LEFT)
btnReset = Button(window, text="Reset", command=button_status.reset_status)
btnReset.pack(side=LEFT)
quitBtn = Button(window, text="QUIT", fg="red", command=quit)
quitBtn.pack(side=LEFT)
mainloop()
