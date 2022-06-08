a = 1   # 전역변수
print(a)

def vartest(): # 지역변수
    global a   # 전역변수 a를 가져온다
    print(a)
    a += 10
    return a

a = vartest()
print(a)