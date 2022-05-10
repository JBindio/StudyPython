# 2번문제
import os
def run():
    clearConsole()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            dic = {'수성':'Mercury', '금성':'Venus', '지구':'Earth', '화성':'Mars',
                   '목성':'Jupiter', '토성':'Saturn', '천왕성':'Uranus', '혜왕성':'Neptune '}
            try:
                name = input('찾으실 행성의 한글이름을 입력하세요.\n')
                clearConsole()
                print('입력하신 행성은', f'{name}', '입니다.')
                print('입력하신 행성의 영문이름은', f'{dic[name]}', '입니다.')
                input('계속 하려면 엔터를 누르세요')
                clearConsole()
                continue
            except Exception:
                print('에러가 발생했습니다.' f'{name}','은(는)없는 행성입니다')
                input('계속 하려면 엔터를 누르세요')
                clearConsole()
        elif sel_menu == 2:
            break
        else:
            clearConsole()

def get_menu():
    str_menu = ('===========================\n'
                '행성이름 찾기 프로그램 v1.1\n'
                '===========================\n'
                '1. 행성이름 영문검색\n'
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