from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#웹페이지 요청을 하는 코드이다. 특정 url을 적으면 웹페이지에 대한 소스코드들을 볼 수 있다.

# pprint(html.text)
#html 이라는 변수에 저장된 소스코드들 중 텍스트들을 pprint로 정렬한걸 눈으로 확인한다.

soup = BeautifulSoup(html.text, 'html.parser')
#소스코드들을 가지고 왔다 그런데 이것들은 모두 html 파일이다.
#그래서 위에서 처럼 Beautifulsoup를 이용하여 파싱을 해주어야 한다.

data1 = soup.find('div', {'class': 'weather_box'})

find_status = data1.find('p', {'class':'cast_txt'}).text
print('날씨 현황:' + find_status)

find_address = data1.find('span', {'class':'btn_select'}).text
print('현재 위치: '+find_address)

find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
print('현재 온도: '+find_currenttemp+'℃')

data2 = data1.findAll('dd')
find_dust = data2[0].find('span', {'class':'num'}).text
find_ultra_dust = data2[1].find('span', {'class':'num'}).text
find_ozone = data2[2].find('span', {'class':'num'}).text
print('현재 미세먼지: '+find_dust)
print('현재 초미세먼지: '+find_ultra_dust)
print('현재 오존지수: '+find_ozone)