# 피보나치 수열 모듈

def fib(n):     # 피보나치 수열 출력
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # 피보나치 수열을 리스트로 반환
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# python fibo.py 50 처럼 직접 실행할 때만 동작한다.
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
