# 5번문제
import os
def run():
    clearConsole()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            try:
                x = int(input('수행할 구구단의 숫자를 입력하세요.\n'))
                if x == 0:
                    clearConsole()
                    print('0단은 없습니다')
                    input('계속 하려면 엔터를 누르세요.')
                    clearConsole()
                    continue
                clearConsole()
                print(f'[{x}단을 실행합니다.]')
                for y in range(1, 10):
                    print(f'{x}*{y}={x*y:2d}',end=' ')
                    print()
                print(f'[{x}단 실행을 완료했습니다.]')
                input('계속 하려면 엔터를 누르세요.')
                clearConsole()
                continue
            except Exception as e:
                print('에러가 발생했습니다. 에러코드 = 'f'{e}')
                input('계속 하려면 엔터를 누르세요.')
                clearConsole()
        elif sel_menu == 2:
            break
        else:
            clearConsole()

def get_menu():
    str_menu = ('===========================\n'
                '구구단 프로그램 v1.5\n'
                '===========================\n'
                '1. 구구단 실행하기\n'
                '2. 종료\n'
                '===========================')
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