# 주소록 프로그램 v1.5
# 작성일 : 2022-05-09
# 작성자 : 이정빈
# 설  명 : 파일DB 에서 오라클 연동

import os
import cx_Oracle as ora

# 연락처 클래스
class Contact:
    name = ''; phone_num = ''; e_mail = ''; addr = ''

    def __init__(self, name, phone_num, e_mail, addr) -> None:
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr

    def __str__(self) -> str:
        str_val = (f'==============================\n'
                   f'이  름 : {self.name}\n'
                   f'핸드폰 : {self.phone_num}\n'
                   f'이메일 : {self.e_mail}\n'
                   f'주  소 : {self.addr}\n'
                   f'==============================\n')
        return str_val

def initDB():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    return conn

# 실행 함수
def run():
    lst_contact = [] # 빈 리스트 생성
    conn = initDB() # 오라클 연결 및 연결 객체 생성
    clearConsole()

    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            isval = set_contact(conn)
            if isval:
                input('입력이 완료되었습니다.\n계속 하려면 엔터를 누르세요') # 아무값도 받지않고 엔터대기
            else:
                input('에러가 발생했습니다. \n계속 하려면 엔터를 누르세요')
            clearConsole()
        elif sel_menu == 2:
            clearConsole()
            get_contact(conn)
            input('출력이 완료되었습니다.\n계속 하려면 엔터를 누르세요')
            clearConsole()
        elif sel_menu == 3:
            clearConsole()
            name = input('삭제할 이름을 입력하세요 = ')
            del_contact(conn, name)
            input('삭제가 완료되었습니다.\n계속 하려면 엔터를 누르세요')
            clearConsole()
        elif sel_menu == 4:
            conn.close()
            break
        else:
            clearConsole()
           # print('잘못된 번호 입니다.')
           # print('다시 입력하세요.')

# 주소록 입력 함수
def set_contact(conn):
    contact = None
    isSucceed = False # 입력성공여부
    try: # 입력없이 엔터, 입력갯수 다를시 생기는 예외처리
        name, phone_num, e_mail, addr = \
        input('정보입력\n이름/핸드폰/이메일/주소 : ').split('/')
        contact = Contact(name, phone_num, e_mail, addr)
        # DB처리
        cur = conn.cursor()
        query = ('INSERT INTO addressbook '
                 'VALUES (SEQ_ADDRBOOK.nextval, :1, :2, :3, :4)')
        tup = (contact.name, contact.phone_num, contact.e_mail, contact.addr)
        cur.execute(query, tup)
        conn.commit()
        cur.close()
        isSucceed = True
    except Exception as e:
        print('에러가 발생했습니다. (에러코드 = ',e)
        isSucceed = False
    finally:
        return isSucceed # True면 입력성공, False면 입력실패

# 주소록 수정 함수
def up_contact(conn):
    contact = None
    try: # 입력없이 엔터, 입력갯수 다를시 생기는 예외처리
        name, phone_num, e_mail, addr = \
        input('정보입력\n이름/핸드폰/이메일/주소 : ').split('/')
        contact = Contact(name, phone_num, e_mail, addr)
        # DB처리
        cur = conn.cursor()
        query = ('INSERT INTO addressbook '
                 'VALUES (SEQ_ADDRBOOK.nextval, :1, :2, :3, :4)')
        tup = (contact.name, contact.phone_num, contact.e_mail, contact.addr)
        cur.execute(query, tup)
        conn.commit()
        cur.close()
        isSucceed = True
    except Exception as e:
        print('에러가 발생했습니다. (에러코드 = ',e)
        isSucceed = False
    finally:
        return isSucceed # True면 입력성공, False면 입력실패

# 주소록 출력 함수
def get_contact(conn):
    cur = conn.cursor()
    query = 'SELECT name, phone_num, e_mail, addr FROM addressbook'

    for row in cur.execute(query):
        contact = Contact(row[0], row[1], row[2], row[3])
        print(contact)
    
    cur.close()


# 주소록 삭제 함수
def del_contact(conn, name):
    cur = conn.cursor()
    query = f"DELETE FROM addressbook WHERE name = '{name}'"
    cur.execute(query)
    conn.commit()
    cur.close()

# 메뉴 입력 함수
def get_menu():
    str_menu = ('========================\n'
                '--주소록 프로그램 v1.1--\n'
                '========================\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n'
                '========================\n')
    print(str_menu)
    menu = 0 # 초기화
    # 0 ~ 9 숫자외 ValueError 발생
    try:
        menu = int(input('메뉴 입력 : '))
    except Exception as e:
        print(e)
    finally:
        return menu

# 콘솔 클리어 함수
def clearConsole():
    command = 'clear' # mac, unix, linux 화면 클리어 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' #windows, dos 화면 클리어 명령어
    os.system(command)

# 프로그램 시작
if __name__ == '__main__': # 시작
    print('주소록 프로그램 v1.5 실행')
    try:
        run()
    except KeyboardInterrupt as e:
        clearConsole()
        print('Crrl+c 종료')