# 4번문제
import os
def run():
    clearConsole()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            try:
                i = int(input('역순으로 변환할 숫자를 입력하세요.\n'))
                clearConsole()
                print('입력한 숫자의 역순은', f'{int(str(i)[::-1])}', '입니다.')
                input('계속 하려면 엔터를 누르세요')
                clearConsole()
                continue
            except Exception as e:
                print('에러가 발생했습니다. 에러코드 = 'f'{e}')
                input('계속 하려면 엔터를 누르세요')
                clearConsole()
        elif sel_menu == 2:
            break
        else:
            clearConsole()

def get_menu():
    str_menu = ('===========================\n'
                '숫자 역순 변환 프로그램 v1.4\n'
                '===========================\n'
                '1. 숫자 역순 변환하기\n'
                '2. 종료\n'
                '===========================\n')
    print(str_menu)
    menu = 0 # 초기화
    # 0 ~ 9 숫자외 ValueError 발생
    try:
        menu = int(input('메뉴 입력 : '))
    except Exception as e:
        print(e)
    finally:
        return menu

def clearConsole():
    command = 'clear' # mac, unix, linux 화면 클리어 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' #windows, dos 화면 클리어 명령어
    os.system(command)

if __name__ == '__main__': # 시작
    try:
        run()
    except KeyboardInterrupt as e:
        clearConsole()
        print('Crrl+c 종료')