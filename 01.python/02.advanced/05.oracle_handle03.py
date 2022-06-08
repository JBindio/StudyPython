# 오라클DB 연동 - INSERT INTO
from __future__ import division
import cx_Oracle as ora

# DB 접속함수
def myconn():
# 데이터소스 네임 객체생성(접속주소, 포트번호, 서비스명)
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
# DB연결 객체 생성
    conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn,encoding = 'utf-8')
    return conn

# DB에서 테이블 가져오기
def get_list(conn):
    cur = conn.cursor()
    for row in cur.execute('SELECT * FROM divTBL'):
        print(row)
    
    cur.close()
    conn.close()

def set_list(conn, tup):
   cur = conn.cursor()
   query = f"INSERT INTO divtbl VALUES (:1, :2)" #SQL inject 보안문제 + 사용효율성
   cur.execute(query, tup)
   conn.commit() # 완전저장

   cur.close()
   conn.commit()

if __name__ == '__main__':
    print('=== DIVTBL 데이터 조회 ===')
    get_list(myconn())
   
    print('=== DIVTBL 신규 입력 ===')
    division, names = input('(division, name) 입력 (구분자 \' \')= ').split(' ')
    tup = (division, names)
    set_list(myconn(), tup)
    
    print('=== 입력후 DIVTBL 데이터 조회 ===')
    get_list(myconn())