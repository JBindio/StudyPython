## while 문 = True 인 경우 반복 실행
hit = 0
while (hit < 100):
    hit += 1
    
    print(f'나무를 {hit}번 찍었습니다.')
    if (hit == 10):
        print('나무가 넘어갑니다.')
        break # while 은 break를 자주 사용
    else: print('나무가 넘어가지 않았습니다')

print('나무 베기 완료!')