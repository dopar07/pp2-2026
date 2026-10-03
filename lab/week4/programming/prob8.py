"""
작성자: 이찬민 (202611838)
작성일: 2026-10-03
문제: 파이썬 EXPRESS 8장 Programming 08
      노래 가사를 리스트로 받아 저장하고, sing() 메소드로 한 줄에 한 항목씩 출력하는 클래스를 작성한다.
      (문제 본문은 printSong이라고 되어 있으나 예시 코드는 Song을 사용하므로 Song으로 작성)
설계:
  - 클래스 Song
      인스턴스 변수: lyrics (가사 문자열 리스트)
      __init__(self, lyrics) : 가사 리스트를 객체 내부에 저장
      sing(self)             : 리스트에서 문자열을 하나씩 꺼내 출력
  - test_prob8() : 교재 예시 가사로 객체 생성 후 sing() 호출
"""


class Song:
    def __init__(self, lyrics):
        self.lyrics = list(lyrics)   # 외부 리스트가 바뀌어도 영향받지 않도록 복사

    def sing(self):
        for line in self.lyrics:
            print(line)


def test_prob8():
    aSong = Song(["TWINKLE, twinkle, little star,",
                  "How I wonder what you are!",
                  "Up above the world so high,",
                  "Like a diamond in the sky."])
    aSong.sing()


if __name__ == "__main__":
    test_prob8()
