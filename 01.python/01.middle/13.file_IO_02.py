# 파일 입출력 2 - 읽기

f = open('./file/temp.txt', mode= 'r', encoding= 'utf-8')

# t = f.read() # 전체 읽기(잘 쓰지않음)
while True:
    line = f.readline() # 1줄 씩 읽기
    if not line: break
    
    print(line, end='')

f.close() # close 필수!!
print('파일 읽기 완료')