# 생일 축하 함수

def say_happy_birthday(name:str) -> None:
    print("안녕하세요!")
    print(f"{name}님 생일축하합니다!")

def test_say_happy_birthday() :
    say_happy_birthday("찬민")
    say_happy_birthday("서준")
    say_happy_birthday("우성")
    say_happy_birthday("재중")

def test_say_happy_birthday2() :
    for name in ["찬민", "서준", "우성", "재중"]:
        say_happy_birthday(name)

def test_say_happy_birthday3() :
    say_happy_birthday(3.141592)
    say_happy_birthday(100)
    say_happy_birthday([1, 2, 3])

if __name__ == "__main__":
#    test_say_happy_birthday()
#   test_say_happy_birthday2()
    test_say_happy_birthday3()