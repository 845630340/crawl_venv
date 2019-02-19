import requests
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime

headers = {
    "accept": "text/javascript, text/html, application/xml, text/xml, */*",
    "content-type": "application/x-www-form-urlencoded",
    "referer": "https://www.toutiao.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "cookie": """tt_webid=6642930114115356168; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1681d2ce83d562-0ee42d42f41f97-10336653-13c680-1681d2ce83edb4; tt_webid=6642930114115356168; csrftoken=7dd3951af35b50bf3d31720879f7995a; uuid="w:5d95a3d5775e407b8ab2617da925d965"; CNZZDATA1259612802=491698772-1546675650-https%253A%252F%252Fwww.google.com%252F%7C1547193903; __tasessionId=8uun05bwi1547195138926"""
}
home_url = 'https://www.toutiao.com/a6647636878411432451/'
r = requests.get(home_url, headers=headers)
print(r.status_code)
base_data = BeautifulSoup(r.text, 'lxml')
try:
    date = ''
    date_list = base_data.find_all('script')[:]
    for each in date_list:
        if 'time' in each.text:
            date = each.text
    index = date.index('time')
    str_time = date[index + 7:index + 26]
    release_time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    #print(date)
    print(index)
    print(str_time)
except (ValueError, IndexError):
    print('happen error')
