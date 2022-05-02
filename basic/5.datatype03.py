## 복합형
# 리스트(배열)[대괄호]
b = [1, 2, 3, 4]
b.append(5) # 배열 뒤에 값 추가
print(b)

b.insert(3, 10) # 3번 째 순서에 10 추가 ★시작은 0부터
print(b)

b.sort() # 오름차순 정렬 (ASC)
print(b)

b.reverse() # 내림차순 정렬 (DESC)
print(b)

b.remove(10) # 원소 삭제
print(b)

print(type(b))
print(b[2]) # b의 2번째 값 0,1,2 <-

# 딕셔너리(사전) key : value 쌍의 집합 {중괄호} ★제일 많이 쓰게될 자료구조
spiderman = {
    'name' : '피터 파커',
    'age' : 18,
    'weapon' : '웹슈터',
    'memberOfAvengers' : True
}
print(spiderman)
print(spiderman['name']) # key 출력시 대괄호 사용
print(spiderman['memberOfAvengers']) # 대소문자 구분

# 튜플(소괄호)
c = (1, 2, 3, 4)
print(c)
 #c.append(5) # Error! 튜플에서는 값 추가 불가