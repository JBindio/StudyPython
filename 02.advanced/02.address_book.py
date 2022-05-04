# 주소록 프로그램 v1.0
# 작성일 : 2022-05-04
# 작성자 : 이정빈
# 설  명 : ?

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
    clearConsole()

    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            contact = set_contact()
            lst_contact.append(contact)
            input('입력이 완료되었습니다.') # 아무값도 받지않고 엔터대기
            clearConsole()
        elif sel_menu == 2:
            clearConsole()
            get_contact(lst_contact)
            input('출력이 완료되었습니다.')
            clearConsole()
        elif sel_menu == 3:
            clearConsole()
            name = input('삭제할 이름을 입력하세요 = ')
            del_contact(lst_contact, name)
            input('삭제가 완료되었습니다.')
            clearConsole()
        elif sel_menu == 4:
            break
        else:
            clearConsole()
           # print('잘못된 번호 입니다.')
           # print('다시 입력하세요.')

# 주소록 입력 함수
def set_contact() -> Contact:
    name, phone_num, e_mail, addr = \
    input('정보입력(이름, 핸드폰, 이메일, 주소 (구분자 /) : ').split('/')
    contact = Contact(name= name, phone_num= phone_num,
                      e_mail= e_mail, addr= addr)
    return contact

# 주소록 출력 함수
def get_contact(lst_contact):
    for contact in lst_contact:
        print(contact)

# 주소록 삭제 함수
def del_contact(lst_contact, name):
    for i, contact in enumerate(lst_contact):
        if contact.name == name:
            del lst_contact[i]

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
    menu = input('메뉴 입력 : ')
    return int(menu)

# 콘솔 클리어 함수
def clearConsole():
    command = 'clear' # mac, unix, linux 화면 클리어 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' #windows, dos 화면 클리어 명령어
    os.system(command)

# 프로그램 시작
if __name__ == '__main__': # 시작
    print('주소록 프로그램 v1.1 실행')
    run()