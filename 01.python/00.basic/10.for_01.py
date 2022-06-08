## for(반복) = for 변수 in 변수:
'''
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for x in range(1, 101): # range(1(부터), 101(100까지), 2(씩 증가)) = 1-100까지(101-1) 2씩 증가
     result = result + x
print('배열의 합 =', result)

# 튜플, 포맷팅 사용
arr2 = ('me', 'my', 'friend', 'jane')
for item in arr2:
    print(f'{item:>10}')

# 1- 10까지 수 중에 짝수 구분하기
for num in range(1, 11):
    if (num % 2) == 0:
        print(f'{num}는(은) 짝수 입니다.')
    else:
        print(f'{num}는(은) 홀수 입니다.')
'''

# for문 내에서 사용하는 continue, break
# brake 반복 탈출, continue 무시
values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
num = 0 
for item in values:
    num += 1
    if (num % 2) == 0:
        #break # 반복문 탈출
        continue # if 조건만 무시 하고 다음 값 진행
    else:
        print(f'{num}번 수는 {item}입니다.')