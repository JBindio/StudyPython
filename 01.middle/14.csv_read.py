# CSV 파일 읽기
import csv # csv 모듈 사용

file_name = './busanbus_211231.csv'

f = open(file_name, mode= 'r', encoding= 'utf-8')
reader = csv.reader(f, delimiter=',') # 구분자가 , 일경우

next(reader) # 첫 줄(제목줄)이 있을때 건너뛰기
for line in reader:
    print(line)

f.close() ## close 필수!!