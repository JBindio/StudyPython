# 첫번째 간단한 로또
import random as rnd # random 모듈 호출

numbers = [i for i in range(1,46)] # for를 활용한 리스트 만들기
lotto = [] # 로또 번호 저장

for i in range(6): # 6번 반복
    lotto.append(rnd.choice(numbers))

lotto.sort()
print(lotto)
# 중복이 발생하므로 완벽하진 않다