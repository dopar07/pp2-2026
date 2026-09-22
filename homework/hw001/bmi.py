# BMI 계산 및 health.txt 파일 읽기 모듈


def calculate_bmi(weight: float, height_cm: float) -> float:
    """몸무게(kg)와 키(cm)로 BMI를 계산한다."""
    height_m = height_cm / 100
    return weight / (height_m ** 2)


def bmi_category(bmi: float) -> str:
    """BMI 값에 따른 소견을 반환한다. (WHO 기준)"""
    if bmi < 18.5:
        return "저체중"
    elif bmi < 25:
        return "정상"
    elif bmi < 30:
        return "과체중"
    else:
        return "비만"


def read_health_file(path: str) -> tuple[list[str], list[dict]]:
    """health.txt를 읽어 (제목 목록, 데이터 목록)을 반환한다.

    첫 줄은 제목, 이후 각 줄은 '전화번호 이름 키 몸무게' 형식이다.
    빈 줄이나 형식이 잘못된 줄은 건너뛴다.
    """
    try:
        with open(path, encoding="utf-8-sig") as f:
            lines = f.read().splitlines()
    except UnicodeDecodeError:
        # 윈도우 메모장(ANSI)으로 저장된 파일 대비
        with open(path, encoding="cp949") as f:
            lines = f.read().splitlines()

    lines = [line for line in lines if line.strip()]
    if not lines:
        return [], []

    header = lines[0].split()
    records = []
    for lineno, line in enumerate(lines[1:], start=2):
        parts = line.split()
        if len(parts) != 4:
            print(f"[경고] {lineno}번째 줄 형식 오류로 건너뜀: {line}")
            continue
        phone, name, height, weight = parts
        try:
            height = float(height)
            weight = float(weight)
        except ValueError:
            print(f"[경고] {lineno}번째 줄 숫자 오류로 건너뜀: {line}")
            continue
        bmi = calculate_bmi(weight, height)
        records.append({
            "phone": phone,
            "name": name,
            "height": height,
            "weight": weight,
            "bmi": bmi,
            "category": bmi_category(bmi),
        })
    return header, records


def test_bmi():
    assert round(calculate_bmi(72, 175), 1) == 23.5
    assert bmi_category(17.0) == "저체중"
    assert bmi_category(23.5) == "정상"
    assert bmi_category(26.0) == "과체중"
    assert bmi_category(31.0) == "비만"
    print("test_bmi 통과")


if __name__ == "__main__":
    test_bmi()
