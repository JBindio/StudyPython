# 입출력

print('물어보세요 : ',end='')
name = '이름누구'
age = '몇살이야? 나이'
bye = '잘가 안녕'

while True:
    a = input()
    if a in name:
        print('홍길동 이야')
    elif a in age:
        print('99살 이야')
    elif a == bye:
        print('안녕! 또 만나')
        break
    else: print('무슨 말인지 모르겠어')
