#BMI 계산 함수

def Calculate_BMI(weight: float, height: float) -> float:
    bmi = weight / (height ** 2)
    return bmi

def Chose_BMI_Category(bmi: float) -> str:
    if bmi < 18.5:
        return "저체중"
    elif 18.5 <= bmi < 25:
        return "정상"
    elif 25 <= bmi < 30:
        return "과체중"
    else:
        return "비만"
    
def test_Calculate_BMI():
    for i in range(3):
        name = input("이름을 입력하세요: ")
        weight, height = map(float, input("체중(kg)과 키(m)를 입력하세요(예: 82 1.8): ").split())
        bmi = Calculate_BMI(weight, height)
        category = Chose_BMI_Category(bmi)
        print(f"BMI: {bmi}")
        print(f"Category: {category}")
        print("그만하시겠습니까? (y/n): ")
        if input().lower() == 'y':
            break

name = []
height = []
weight = []

test_Calculate_BMI()   