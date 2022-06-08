## 문자열 연산 (+, *)
first = 'Hello'
Second = 'World!'
print(first + Second) # 문자열 + 문자열 (합치기)
print(first , Second) # 문자열 , 문자열 (합치기, 공백)
print(first * 3) # 문자열 * 문자열 (곱하기)

# 문자열 길이 구하기(내장함수 len)
print(len('한글'))
print(len(first))

# 리스트 연산
print(first[0])  # first의 문자열 위치값
print(first[-1]) # first의 문자열 위치값 반대로

## 문자열 자르기
current_date = '2022-05-02 14:23:45'
year = current_date[0:4] # 순서는 N+1
year = current_date[:4]  # 0은 생략가능
month = current_date[5:7]
day = current_date[8:10]
hour = current_date[11:13]
min = current_date[-5:-3]
sec = current_date[-2:]
print(year,'년', month,'월', day,'일')
print(hour,'시', min,'분', sec,'초')

# 문자는 변경 할 수 없다 (insert 불가)
p = 'python'
print(p)
#p[0] = 'P' # Error
p2 = 'P' + p[1:]
print('P' + p[1:])
print(p2)

## 대소문자 변경 (클래스.upper / 클래스.lower)
print(p.upper()) # 클래스p를 대문자로 변경
print(p.lower()) # 클래스p를 소문자로 변경