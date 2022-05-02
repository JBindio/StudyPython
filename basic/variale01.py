# 주석입니다. 주석은 프로그래밍에 영향X

# 변수(Variable)
# 홑, 쌍 따옴표 혼용가능 "안녕하세요"
# '가 들어가야 할 경우 쌍따옴표 사용 ex) "i'm a boy"
a = '안녕하세요'
print(a)

a = True
print(a)

a = 3.14
print(a)

a= 1/10
print(a)

# 출력 방식2 - 자동으로 공백 ,로 구분 갯수 상관X
print('값은', a, '입니다')

a = 3
b = 3.141592
c = 'python'
d = (1, 2, 3) # 튜플 - 소괄호() 수정 불가
e = [4, 5, 6] # 리스트 - 대괄호[] 수정,삭제 가능
f = [7, '8', True]
g = False
print('변수의 값', 'a=', a, 'b=', b, 'c=',c, 'd=', d)
print('변수의 값', 'e=', e, 'f=', f, 'g=',g)

#변수명 사용불가 (숫자,공백,특수문자(_제외), 대소문자 구분)
Var5 = 5
var5 = '8'
print(Var5, var5)

# 주소값 설정 (id(변수명))
print(id(a))
print(id(b))
print(id(c))
