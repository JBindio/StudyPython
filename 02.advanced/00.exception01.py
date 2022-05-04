# 예외처리 1 - 예외 발생
# 디버깅
# try 문은 1번밖에 실행되지 않는다

""" 
F5 -디버깅 시작 / 중단점까지 계속 진행하기
Shift + F5 - 디버깅 중지
F9 - 중단점 설정/해제
F10 - 프로시저 단위로 실행(한 라인씩 진행)
F11 - 한 단계씩 코드 실행(함수 안으로 진행) 
"""

def mul (a, b):
    res = a * b
    return res

def div (a, b):
    res = 0
    try:
        res = a / b
    except Exception as e:
        print(f'에러가 발생했습니다. 에러코드 = {e}')
    finally:
        return res

if __name__ == '__main__':
    
    value = 7
    
    print('곱셈/나눗셈')
    print(div(6, 0))
    print(mul(6, 6))
    print('프로그램 종료')