# 사람 객체를 위한 클래스 Person

class Person:
   # pass # 실행은 하지만 넘어간다 (only python)
    # 속성(변수)
    __name = ''  # 이름 # 변경하고 싶지 않을때 __
    age = 0      # 나이  
    height = 180 # 키
    weight = 80  # 몸무게

    # 생성자 재정의
    # 매직 메서드(스페셜 메서드) __함수__
    def __init__(self, name = None) -> None: 
        if name == None:
            self.__name = '홍길동'
        else:
            self.__name = name
        print (f'{self.__name} 탄생!')

    # 매직 메서드 __str__ 사용 재정의
    def __str__(self) -> str:
        value = f'''객체 : {self.__name}
나이 : {self.age}
  키 : {self.height}'''
        return value

    # 행위(함수)
    def walk(self, speed):
        print(f'{self.__name}이(가) {speed}km/h 로 걷는다.')
        return
    
    def run(self, speed):
        print(f'{self.__name}이(가) {speed}km/h 로 뛴다.')
        return

p = Person('이정빈') # 객체 생성
# p.__name = '이정빈'
p.age = '30'
p.height = '180'
p.weight = '80'
p.walk(2)
p.run(10)
# print(type(p))
print(p)
