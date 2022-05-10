# 3번문제
import os
def run():
    clearConsole()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            word = list(input('여러 단어를 입력하세요.(구분자는 /)\n').split('/'))
            clearConsole()
            print('입력하신 단어들은', f'{word}', '입니다.')
            print('입력하신 단어의 수는', f'{len(word)}개', '입니다.')
            input('계속 하려면 엔터를 누르세요')
            clearConsole()
            continue
        elif sel_menu == 2:
            break
        else:
            clearConsole()

def get_menu():
    str_menu = ('===========================\n'
                '단어 갯수 계산 프로그램 v1.3\n'
                '===========================\n'
                '1. 단어 갯수 구하기\n'
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