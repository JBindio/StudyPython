# 네이버 웹페이지 긁어오기 1(크롤링,스크래핑)
from urllib.request import Request, urlopen

req = Request('https://www.naver.com/')
res = urlopen(req)
print(res.status) # 200 = 웹페이지 열기 성공

# 패키지 설치하기