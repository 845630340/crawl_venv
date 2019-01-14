# -*- coding:utf8 -*-

import requests
from bs4 import BeautifulSoup

url = 'https://www.toutiao.com/group/6645951471437234696/'
url2 = 'https://www.toutiao.com/group/6645953773015400967/'
headers = {
            "accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://www.toutiao.com/",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "cookie": """tt_webid=6642930114115356168; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1681d2ce83d562-0ee42d42f41f97-10336653-13c680-1681d2ce83edb4; tt_webid=6642930114115356168; csrftoken=7dd3951af35b50bf3d31720879f7995a; uuid="w:5d95a3d5775e407b8ab2617da925d965"; CNZZDATA1259612802=491698772-1546675650-https%253A%252F%252Fwww.google.com%252F%7C1547193903; __tasessionId=8uun05bwi1547195138926"""
        }
r = requests.get(url2, headers=headers).text
base_data = BeautifulSoup(r, 'lxml')
date = base_data.find_all('script')[6].text

index = date.index('time')
print 'time is:', date[index+7:index+26]