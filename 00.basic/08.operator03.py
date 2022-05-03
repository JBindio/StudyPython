## 문자열 포맷팅 (원하는 위치에 변하는 값 넣기)
from posixpath import split


name = '이정빈'
login_str = '{0}님 로그인 중'.format(name) # 변하는 값의 위치에 {0}.format(값)
print(login_str)
print('{0}, {1}, {2}'.format('하나', 2, True))
print(f"{'하나'}, {2}, {login_str}") # f를 사용하면 효율적이다

# 소수점 표현
PI = 3.14159268
print('{0:0.2f}'.format(PI)) # 소수점 2번째 짜리까지 출력하고 반올림
print(f'{PI:0.3f}')          # 소수점 3번째 짜리까지 출력하고 반올림

# 문자열을 '' 잘라서 리스트화
full_name = 'Hugo MG Sung'
sp_names = full_name.split()
print(sp_names)

# 문자열을 , 로 잘라서 리스트화
greeting = 'Hello, World'
word = greeting.split(',')
print(word)

# 공백 붙히기
hi = '     Hello~     '
print(hi.lstrip()) #왼쪽 붙히기   (오라클의 LTRIM)
print(hi.rstrip()) #오른쪽 붙히기 (오라클의 RTRIM)
print(hi.strip())  #양쪽 붙히기   (오라클의 TRIM)
print(word[1].strip())

# 특정 단어, 문자열 값 변경
print(full_name.replace('Hugo MG', 'Ashley')) # Hugo Mg 를 Ashley 로 변경


# 리스트 연산
arr = ['1', 2, 3, '4', 5]
print(arr[2] + arr[1]) # 숫자 + 숫자 = 3 + 2 = 5
print(arr[3] + arr[0]) # 문자열 + 문자열 = '4'+'1' = 41
print(arr[3] * arr[2])  # 문자열 * 숫자 = '4'를 3번 반복출력 = 444

# 이중 리스트
arr2 = [1, 2, 3.14, ['Hi', 'My', 'Friends']]
print(arr2[3])       # 3번째에 있는 배열
print(arr2[3][1])    # 4번째에 있는 배열의 2번째 값 (2차원 배열)
print(arr2[3][1][0]) # 4번째에 있는 배열의 2번째의 1번째 값 (3차원 배열)

arr3 = arr + arr2
print(arr3)