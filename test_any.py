#!/usr/bin/python
# -*- coding:utf8 -*
'''
import os
LOG_FILE_PATH = os.getcwd()

dir = LOG_FILE_PATH + '/data_hello'
with open(dir,'a') as f:
    f.write('The weather is so good!')
'''
'''
class CustomError(Exception):
    def __init__(self,ErrorInfo):
        super(CustomError,self).__init__(self)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return '%s: the error is  %s' % (,self.errorinfo)

try:
    raise CustomError('客户端错误!')
except CustomError as e:
    print e
'''
'''
class Student(object):

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        self._score = value
    @property
    def smart(self):
        return self._score + 100

s = Student()
s.score = 100
print s.score
print s.smart
'''
'''
from datetime import datetime

data = datetime.now().strftime('%Y-%m-%d')

print data
print type(data)
'''
'''
import os
from datetime import datetime

path = os.getcwd()
print path
doc_path = path + '/document_test'
if not os.path.exists(doc_path):
    os.mkdir(doc_path)

data = datetime.now().strftime('%Y-%m-%d')
last_path = '{}/{}_test'.format(doc_path,data)
with open(last_path,'w') as f:
    f.write('This is a test script!')
'''
'''
s = raw_input()
first, second = 0, 0
index_tup = None
max_span = 0
i = 0
while i < len(s):
    if s[i].isdigit():
        first = i
        while i < len(s) and s[i].isdigit():
            i += 1
        second = i
        if second - first > max_span:
            max_span = second - first
            index_tup = (first, second)
    else:
        i += 1
start, end = index_tup[0], index_tup[1]
print s[start:end]
'''
from datetime import datetime,timedelta

def split_date_range(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    date_list = []
    while end_date >= start_date:
        date_list.append(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)
    return date_list

print split_date_range('2018-12-11', '2018-12-14')


adview_account = {
    "username": "ads.network@ihandysoft.com",
    "site_name": "mkt_adview_dev",

    "form": {
        "token": "reh4fq9sjm8b96q05cf92ban27tunurb",
        "userId": "ads.network@ihandysoft.com",
        "BankInfo": "HN_HSBC"
    },

    "folder": "Shared-MKT-Dev"
}

emx_account = {
    "username": "lexieihandyBRT",
    "site_name": "mkt_brealtime_emx_dev",
    "form": {"BankInfo": "HN_HSBC"},
    "url": "https://console.appnexus.com/login",
    "folder": "Shared-MKT-Dev",
    "password": "YYA#gRxaIw5L$n*"
}















