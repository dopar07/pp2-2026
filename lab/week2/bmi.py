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
    bmi = Calculate_BMI(82, 1.8)
    category = Chose_BMI_Category(bmi)
    print(f"BMI: {bmi}")
    print(f"Category: {category}")

test_Calculate_BMI()      