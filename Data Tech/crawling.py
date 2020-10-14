# https://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=2020&mm=6&obs=1&x=28&y=3

import requests
import calendar
import datetime
from bs4 import BeautifulSoup

data = []
now = datetime.datetime.now()
y = now.strftime('%Y')
m = now.strftime('%m')
response = requests.get(
    'http://www.kma.go.kr/weather/climate/past_cal.jsp?stn=108&yy='+str(y)+'&mm='+str(m)+'&obs=1')
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'table_develop'})

count = 0
point = [''] * 7
pointt = [''] * 7
fstr = [''] * 7
tstr = [''] * 7
mstr = [''] * 7
estr = [''] * 7
temp = [''] * 7
temptop = [''] * 7
tempmin = [''] * 7
rain = [''] * 7

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))

    if tds:
        for i in range(0, 7):
            point[i] = tds[i].text

        if count % 2 != 0:
            for j in range(0, 7):
                pointt[j] = point[j].translate({ord('일'): ''})

        if count % 2 == 0:
            for k in range(0, 7):
                fstr[k] = point[k].find('최고기온')
                tstr[k] = point[k].find('최저기온')
                mstr[k] = point[k].find('평균운량')
                estr[k] = point[k].find('일강수량')
                temp[k] = point[k][5:fstr[k]].translate({ord('℃'): ''})
                temptop[k] = point[k][fstr[k]+5:tstr[k]
                                      ].translate({ord('℃'): ''})
                tempmin[k] = point[k][tstr[k]+5:mstr[k]
                                      ].translate({ord('℃'): ''})
                rain[k] = point[k][estr[k] +
                                   5:].translate({ord(' '): '', ord('-'): '0.0', ord('m'): ''})

            if pointt[0] == '\xa0' or temp[0] == '':
                sun = ""
            else:
                sun = str(
                    y)+'-'+str(m)+'-'+pointt[0]+' '+temp[0]+' '+temptop[0]+' '+tempmin[0]+' '+rain[0]
                data.append([sun])

            if pointt[1] == '\xa0' or temp[1] == '':
                mon = ""
            else:
                mon = str(
                    y)+'-'+str(m)+'-'+pointt[1]+' '+temp[1]+' '+temptop[1]+' '+tempmin[1]+' '+rain[1]
                data.append([mon])

            if pointt[2] == '\xa0' or temp[2] == '':
                tue = ""
            else:
                tue = str(
                    y)+'-'+str(m)+'-'+pointt[2]+' '+temp[2]+' '+temptop[2]+' '+tempmin[2]+' '+rain[2]
                data.append([tue])

            if pointt[3] == '\xa0' or temp[3] == '':
                wed = ""
            else:
                wed = str(
                    y)+'-'+str(m)+'-'+pointt[3]+' '+temp[3]+' '+temptop[3]+' '+tempmin[3]+' '+rain[3]
                data.append([wed])

            if pointt[4] == '\xa0' or temp[4] == '':
                thu = ""
            else:
                thu = str(
                    y)+'-'+str(m)+'-'+pointt[4]+' '+temp[4]+' '+temptop[4]+' '+tempmin[4]+' '+rain[4]
                data.append([thu])

            if pointt[5] == '\xa0' or temp[5] == '':
                fri = ""
            else:
                fri = str(
                    y)+'-'+str(m)+'-'+pointt[5]+' '+temp[5]+' '+temptop[5]+' '+tempmin[5]+' '+rain[5]
                data.append([fri])

            if pointt[6] == '\xa0' or temp[6] == '':
                sat = ""
            else:
                sat = str(
                    y)+'-'+str(m)+'-'+pointt[6]+' '+temp[6]+' '+temptop[6]+' '+tempmin[6]+' '+rain[6]
                data.append([sat])

            print(sun)
            print(mon)
            print(tue)
            print(wed)
            print(thu)
            print(fri)
            print(sat)
    count += 1

with open('weather/weather.txt', 'w') as file:
    for i in data:
        file.write('{0}\n'.format(i[0]))
