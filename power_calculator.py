# power_calculator.py

def main():
    try:
        # 숫자 입력 및 형변환
        base_input = input("Enter number: ")
        base = float(base_input)
    except ValueError:
        print("Invalid number input.")
        return

    try:
        # 지수 입력 및 형변환
        exponent_input = input("Enter exponent: ")
        exponent = int(exponent_input)
    except ValueError:
        print("Invalid exponent input.")
        return

    result = 1.0

    # 음수 지수일 경우 처리
    if exponent < 0:
        for _ in range(-exponent):
            result *= base
        result = 1 / result
    else:
        for _ in range(exponent):
            result *= base

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
