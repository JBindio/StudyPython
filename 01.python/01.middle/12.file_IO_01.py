# 파일 입출력 1 - 쓰기

f = open('./file/temp.txt', mode= 'w', encoding= 'utf-8')
# mode = w 새로생성, a 추가쓰기, r 읽기
f.write('안녕하세요\n')
f.write('제 이름은 이정빈 입니다.\n')
f.write('저는 한국인 입니다.\n')

f.close() # close 필수!!
print('파일 생성완료')