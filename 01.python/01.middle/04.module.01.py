# 모듈 학습
# 모듈 math를 불러온뒤 m 으로 명명 (import 모듈 as 별명)
import math as m
# 모듈 math에서 pow, log10, pi 만 사용 (from 모듈 import 가져올 모듈)
from math import pow, log10, pi

print(pi)
print(m.log10(30))
print(m.pow(2, 10))