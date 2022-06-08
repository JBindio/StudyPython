# 예외처리 2 - 예외발생 2
try:
    x, y = map(int, input('두 수를 입력하세요 > ').split(' '))

    print(f'x = {x}')
    print(f'y = {y}')
    z = x / y # 지역변수(try에서만 사용가능)
    print(f'{x} / {y} = {z}')
# except TypeError as e:
#     print(e,'문자는 사용할수 없습니다')
# except ZeroDivisionError as e:
#     print(e,'두번째 수에 0은 넣을 수 없습니다')
except Exception as e: # 그 외의 모든 에러
    print('에러가 발생했습니다','에러코드',e) 
print('나누기 종료')