# 주소록 프로그램 v1.1
# 작성일 : 2022-05-04
# 작성자 : 이정빈
# 설  명 : 파이썬 학습 기반 주소록 프로그램 만들기

import os

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

# 실행 함수
def run():
    lst_contact = [] # 빈 리스트 생성
    load_contact(lst_contact) # 파일DB 불러오기
    clearConsole()

    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            contact = set_contact()
            if contact is None:  # contact가 비어있을 경우 리스트추가 불가
                input('입력 갯수를 확인하세요.\n계속 하려면 엔터를 누르세요')
                clearConsole()
                continue
            lst_contact.append(contact)
            input('입력이 완료되었습니다.\n계속 하려면 엔터를 누르세요') # 아무값도 받지않고 엔터대기
            clearConsole()
        elif sel_menu == 2:
            clearConsole()
            get_contact(lst_contact)
            input('출력이 완료되었습니다.\n계속 하려면 엔터를 누르세요')
            clearConsole()
        elif sel_menu == 3:
            clearConsole()
            name = input('삭제할 이름을 입력하세요 = ')
            del_contact(lst_contact, name)
            input('삭제가 완료되었습니다.\n계속 하려면 엔터를 누르세요')
            clearConsole()
        elif sel_menu == 4:
            save_contact(lst_contact) # 파일DB 저장
            break
        else:
            clearConsole()
           # print('잘못된 번호 입니다.')
           # print('다시 입력하세요.')

# 주소록 입력 함수
def set_contact() -> Contact:
    contact = None
    try: # 입력없이 엔터, 입력갯수 다를시 생기는 예외처리
        name, phone_num, e_mail, addr = \
        input('정보입력\n이름/핸드폰/이메일/주소 : ').split('/')
        contact = Contact(name= name, phone_num= phone_num,
                          e_mail= e_mail, addr= addr)
    except Exception as e:
        print('에러가 발생했습니다 (에러코드 = ',e)
    finally:
         return contact # 잘못되면 None 리턴, contact 객체 리턴

# 주소록 출력 함수
def get_contact(lst_contact:list):
    for contact in lst_contact:
        print(contact)

# 주소록 삭제 함수
def del_contact(lst_contact:list, name):
    for i, contact in enumerate(lst_contact):
        if contact.name == name:
            del lst_contact[i]

# 주소록 파일DB 저장 함수
def save_contact(lst_contact:list):
    f = open('./02.advanced/db_contact.txt', mode='w', encoding='utf-8')
    for contact in lst_contact:
        f.write(contact.name + '/')
        f.write(contact.phone_num + '/')
        f.write(contact.e_mail + '/')
        f.write(contact.addr + '\n')

    f.close() # close 필수!!

# 주소록 파일DB 불러오기 함수
def load_contact(lst_contact:list):
    f = open('./02.advanced/db_contact.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line: break

        lines = line.rstrip('\n').split('/') # 마지막 \n제거하고, /로 나누고 리스트로
        if len(lines) != 4: continue # 2200506 11:11 엔터로 인한 오류 예외처리
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        lst_contact.append(contact)

    f.close()

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
    print('주소록 프로그램 v1.1 실행')
    try:
        run()
    except KeyboardInterrupt as e:
        clearConsole()
        print('Crrl+c 종료')