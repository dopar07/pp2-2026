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
    빈 줄이나 형식이 잘못된 줄은 경고를 출력하고 건너뛴다.
    """
    try:
        f = open(filename, "r", encoding="utf-8-sig")
        lines = f.readlines()
    except UnicodeDecodeError:
        # 윈도우 메모장(ANSI, CP949)으로 저장된 파일이면 다시 읽는다
        f.close()
        f = open(filename, "r", encoding="cp949")
        lines = f.readlines()
    f.close()

    records = []
    for i in range(1, len(lines)):      # 첫 줄은 제목이므로 건너뛴다
        line = lines[i].strip()
        if line == "":                  # 빈 줄은 건너뛴다
            continue

        parts = line.split()
        if len(parts) != 4:
            print(f"[경고] {i + 1}번째 줄 형식 오류로 건너뜀: {line}")
            continue

        phone = parts[0]
        name = parts[1]
        try:
            height = float(parts[2])
            weight = float(parts[3])
        except ValueError:
            print(f"[경고] {i + 1}번째 줄 숫자 오류로 건너뜀: {line}")
            continue

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
