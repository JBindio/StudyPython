# 계산기 프로그램
'''
함수 선언구조
def 함수명(매개변수):
    처리로직1
    처리로직2
'''
# --- 함수선언 ---
from bdb import Breakpoint

#return 값 = 호출한 쪽에 값을 주고 함수를 종료한다.
#값이 없으면 그냥 함수를 종료한다. (for문의 break)
def plus(a, b):
    res = a + b
    return

def minus(a, b):
    res = a - b
    return res

def mul(a, b):
    res = a * b
    return res

def div(a, b):
    if b == 0:
        return 0 # 0으로 나눌때 0이라는 값을 할당한다 아니면 Error!
    res = a // b
    return res

def mul_and_div(a, b):
    return (a * b, a / b) #튜플

def mul_and_minus_and_mul_and_div(a, b):
    return (a + b, a - b, a * b, a / b)

(mul_val, div_val) = mul_and_div(16,2)
print(mul_val)
print(div_val)
print(mul_and_div(16,2))
print(mul_and_minus_and_mul_and_div(17,5))


# --- 함수선언 완료 ---

""" print('[계산기_0.1v]')

num = 0
x = 0 
y = 0
val = 0

while True:
    print('''실행하실 연산을 선택하세요.
1. 더하기
2. 빼기   
3. 곱하기    
4. 나누기
5. 계산기 종료
입력 :''',end=' ')
    num = int(input())

    if num == 1:
        print('[더하기] 첫번째 값을 입력하세요.')
        print('첫번째 값 :', end=' ')
        x = int(input())
        print('[더하기] 두번째 값을 입력하세요.')
        print('두번째 값 :', end=' ')
        y = int(input())
        val = plus(x,y)
        print(f'[더하기] {x} + {y} = {x+y} 입니다.') # return에 값을 할당하지 않았을 때
    elif num == 2:
        print('[빼기] 첫번째 값을 입력하세요.')
        print('첫번째 값 :', end=' ')
        x = int(input())
        print('[빼기] 두번째 값을 입력하세요.')
        print('두번째 값 :', end=' ')
        y = int(input())
        val = minus(x,y)
        print(f'[빼기] {x} - {y} = {val} 입니다.')
    elif num == 3:
        print('[곱하기] 첫번째 값을 입력하세요.')
        print('첫번째 값 :', end=' ')
        x = int(input())
        print('[곱하기] 두번째 값을 입력하세요.')
        print('두번째 값 :', end=' ')
        y = int(input())
        val = mul(x,y)
        print(f'[곱하기] {x} x {y} = {val} 입니다.')
    elif num == 4:
        print('[나누기] 첫번째 값을 입력하세요.')
        print('첫번째 값 :', end=' ')
        x = int(input())
        print('[나누기] 두번째 값을 입력하세요.')
        print('두번째 값 :', end=' ')
        y = int(input())
        val = div(x,y)
        print(f'[나누기] {x} ÷ {y} = {val} 입니다.')
    elif num == 5:
        break
    else:
        continue """