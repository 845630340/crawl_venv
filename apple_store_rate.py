#!/usr/bin/python
# -*- coding:utf8 -*-

import requests
from bs4 import BeautifulSoup
import re

url = 'https://itunes.apple.com/app/id473610119'
r = requests.get(url).text  # html

# html
req_data = BeautifulSoup(r, 'lxml')

average_rating = req_data.find('span', class_="we-customer-ratings__averages__display")
if average_rating:
    print "average_rating:", average_rating.text
else:
    print '不存在average_rating:', average_rating
print '-------------------'

def get_standart_ratings(total_rating):
    if re.search('K$', total_rating):
        total_rating = int(float(total_rating.strip('K')) * 1000)
    else:
        total_rating = int(total_rating)
    return total_rating

raw_total_ratings = req_data.find('div', class_="we-customer-ratings__count small-hide medium-show")
if raw_total_ratings:
    total_result = raw_total_ratings.text.split()[0].decode('string_escape') # 65.4k <str>
    print 'total_ratings:', get_standart_ratings(total_result)
else:
    print '不存在total_ratings:', raw_total_ratings
print '-------------------'

for each_rate in req_data.find_all('div', class_="we-star-bar-graph__bar__foreground-bar"):
    a = each_rate.get('style').split()[1].strip(';').strip('%')
    print int(a)*int(total_result) / 100
