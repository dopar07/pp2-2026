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
        try:
            weight, height = map(float, input("체중(kg)과 키(m)를 입력하세요(예: 82 1.8): ").split())
        except ValueError:
            print("체중과 키를 숫자 두 개로 입력하세요.")
            continue
        bmi = Calculate_BMI(weight, height)
        category = Chose_BMI_Category(bmi)
        print(f"{name}님의 BMI: {bmi:.2f}")
        print(f"Category: {category}")
        if input("그만하시겠습니까? (y/n): ").lower() == 'y':
            break

if __name__ == "__main__":
    test_Calculate_BMI()
