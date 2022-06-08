# 세개의 값을 입력받아서 두개의 변수에 나눠 담기
# split(두 단어를 나누는 기준)
x, y, z = input('두개의 단어를 입력하세요(구분자는 / 입니다) > ').split('/') 

print(x, end=' ')
print(y, end=' ')
print(z)

# 두개의 수 입력하기 1
x, y = input('두개의 수를 입력하세요(구분자는 / 입니다) > ').split('/')

print(int(x) * int(y))

# 두개의 수 입력하기 2
x, y = map(int, input('두개의 수를 입력하세요(구분자는 / 입니다) > ').split('/'))

print(x * y)

a = 'l\'m a boy \"hello!\"'
print(a)