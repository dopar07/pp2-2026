# PP2-2026 · 파이썬 프로그래밍 2

파이썬 프로그래밍 수업의 주차별 실습 코드와 과제를 정리한 저장소입니다.

- 이름: 이찬민
- 학번: 202611838
- GitHub: [dopar07](https://github.com/dopar07)
- 시작일: 2026-09-02

## 폴더 구조

```
pp2-2026/
├── README.md            # 저장소 소개 (이 파일)
├── hello.py             # 첫 파이썬 실행 확인
├── markdown.md          # Markdown 문법 연습
├── mynotebook.ipynb     # Jupyter Notebook 사용 연습
├── lab/                 # 주차별 수업 실습
│   ├── week2/           # 함수, 타입힌트, BMI 계산
│   ├── week3/           # 리스트, 튜플·세트·딕셔너리, 연락처 미니프로젝트
│   └── week4/           # 객체와 클래스
└── homework/            # 과제
    └── hw001/           # HW01 BMI 계산 결과표 (Turtle GUI, 팀 과제)
```

## 주차별 학습 내용

| 주차 | 주제 | 주요 파일 | 설명 |
|---|---|---|---|
| 1주차 | 개발 환경, Markdown, Notebook | `hello.py`, `markdown.md`, `mynotebook.ipynb` | VS Code, Git/GitHub, Markdown과 Jupyter 사용법 |
| [2주차](lab/week2/README.md) | 변수와 자료형, 함수 | `happy.py`, `bmi.py` | 함수 정의와 호출, 타입힌트, 테스트 함수 작성 |
| [3주차](lab/week3/README.md) | 리스트, 튜플·세트·딕셔너리 | `listex.ipynb`, `collections.ipynb`, `typehint.ipynb`, `problem.py`, `miniproject.py` | 컬렉션 자료형 연산, 반복 입력 처리, 딕셔너리 기반 연락처 관리 |
| 4주차 | 객체와 클래스 | `learn8.ipynb` | 클래스 정의, `Counter` 클래스 구현 |

## 과제

| 과제 | 내용 |
|---|---|
| [HW01](homework/hw001/README.md) | `health.txt`를 읽어 BMI를 계산하고 Turtle로 결과표를 그리는 GUI 프로그램 (팀 과제, 팀장) |

## 실행 방법

Python 3.10 이상에서 실행합니다.

```bash
git clone https://github.com/dopar07/pp2-2026.git
cd pp2-2026
python lab/week2/bmi.py
python lab/week3/miniproject.py
```

`.ipynb` 파일은 VS Code의 Jupyter 확장이나 Jupyter Notebook에서 열어 실행합니다.
