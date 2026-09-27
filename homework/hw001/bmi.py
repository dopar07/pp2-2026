# BMI 계산 및 health.txt 파일 읽기 함수 모음


def calculate_bmi(weight, height_cm):
    """몸무게(kg)와 키(cm)로 BMI를 계산한다."""
    height_m = height_cm / 100          # cm -> m
    return weight / (height_m * height_m)


def bmi_category(bmi):
    """BMI 값에 따른 소견을 반환한다. (WHO 기준)"""
    if bmi < 18.5:
        return "저체중"
    elif bmi < 25:
        return "정상"
    elif bmi < 30:
        return "과체중"
    else:
        return "비만"


def read_health_file(filename):
    """health.txt를 읽어 사람별 정보 리스트를 반환한다.

    반환 예: [["010-1234-5678", "홍길동", 175.0, 72.0, 23.5, "정상"], ...]
    """
    f = open(filename, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()

    records = []
    for line in lines[1:]:              # 첫 줄은 제목이므로 건너뛴다
        parts = line.split()
        if len(parts) != 4:             # 빈 줄 등은 건너뛴다
            continue

        phone = parts[0]
        name = parts[1]
        height = float(parts[2])
        weight = float(parts[3])

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        records.append([phone, name, height, weight, bmi, category])

    return records


def test_bmi():
    assert round(calculate_bmi(72, 175), 1) == 23.5
    assert bmi_category(17.0) == "저체중"
    assert bmi_category(23.5) == "정상"
    assert bmi_category(26.0) == "과체중"
    assert bmi_category(31.0) == "비만"
    print("test_bmi 통과")


if __name__ == "__main__":
    test_bmi()
