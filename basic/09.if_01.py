## if (만약 ~라면 True = 실행 False = else 실행)
name = '홍길동'
gender = '여'
if name == '홍길동' and not gender =='남': # 파이썬은 콜론 사용
        print('진료실로 들어갑니다.')
        print('의사선생님께 인사합니다.') # ★파이썬은 줄맞춤(들여쓰기) 필수
else:
    print('기다리세요.')
    print('궁시렁거립니다.')

# != ~가 아니면 True
num = 10
if num != 9:
        print('9가 아닙니다.')
else: print('9입니다.')