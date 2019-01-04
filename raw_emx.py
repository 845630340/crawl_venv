#!/usr/bin/python
# -*- coding:utf8 -*-

import requests
import pandas
from datetime import data

'''
抓取过程：
    1.登录
    2.发送参数，获取report_id
    3.根据report_id生成data_url,抓取数据，保存成csv格式
'''

s = requests.session()
url1 = 'https://console.appnexus.com/login'
params = {}
params['username'] = 'lexieihandyBRT'
params['password'] = 'YYA#gRxaIw5L$n*'
response = s.post(url1,data = params)      # already login


headers = {
    'origin': 'https://console.appnexus.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'accept': 'application/json',
    'referer': 'https://console.appnexus.com/report/publisher/run-report/16',
    'authority': 'console.appnexus.com',
}

null = None
data = {"query":" mutation runReport($reportRequest: ReportRequestInput) { createReport(reportRequest: $reportRequest) { reportId isDuplicate errors { code message } } } ",\
"variables":{"reportRequest":{"reportType":"16","section":"publisher","sectionPath":"publisher","userType":"publisher","memberId":null,"publisherIds":[1163366],"advertiserIds":null,"id":"16","timeInterval":"187","timeGranularity":"daily","timezone":"PST8PDT","metrics":[797,800,802,801,805],"deliveryOptions":{"runType":"RUN_NOW","emailAddresses":null,"format":"csv","saveAsTemplate":null,"reportName":null,"schedule":{"emailAddresses":"bingfang.zou@ihandysoft.com"}},"metricModifiers":{},"provisionalModifiers":null,"filters":[{"columnId":"818","values":[1163366]}],"timeIntervalRange":{"start":"2018-11-23","end":"2018-11-23"},"dimensions":786}}}


# to get the report_id
response1 = s.post('https://console.appnexus.com/report/graphql',headers = headers,json = data)
print response1.text
report_id = response1.json()["data"]["createReport"]['reportId']


# the url of data
data_url = 'https://console.appnexus.com/report/data/{}.json?dataOnly=true&num_elements=500'.format(report_id)
the_r = s.get(data_url).json()['data']
alist = []
for each in the_r:
    alist.append(each)

# to save the format of csv
df=pandas.DataFrame(alist)
df.to_csv('data3.csv',encoding='utf_8_sig')
