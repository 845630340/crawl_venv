#!/usr/bin/python
# -*- coding:utf8 -*-

import requests
import pandas
from datetime import date
from time_test import _request
import json

def login(username="lexieihandyBRT",password="YYA#gRxaIw5L$n*"):
    # log in and stay status
    s = requests.session()
    login_url = "https://console.appnexus.com/login"
    login_param = {
        "username": username,
        "password": password
    }
    s.request('post', login_url, data=login_param)
    print 'log in successfully!'
    return s


def login_crawling(Range = "Today",Interval = "Cumulative",Timezone = "US/Eastern",**Demensions):
    '''
    :param username:   required
    :param password:   required
    :param Range:      default
    :param Interval:   default
    :param Timezone:   default
    :param Demensions: the key is arbitrary,the form of value is the same as in the page.
    :return:csv file
    '''
    s = login()

    # pass param to the payload of 'data'
    today = str(date.today())
    d = {
        "today":today,

        # Range
        "Current Hour":"182",
        "Last Hour":"183",
        "Today":"185",
        "Yesterday":"186",
        "Last 48 Hours":"184",
        "Last 7 Days":"187",
        "Month To Date":"188",
        "Month To Yesterday":"194",
        "Last 30 Days":"193",
        "Last Month":"190",
        "Quarter To Date":"189",
        "Lifetime":"191",

        # Interval
        "Hourly":"hourly",
        "Daily":"daily",
        "Monthly":"monthly",
        "Cumulative":"cumulative",

        # Timezone
        "US/Eastern":"EST5EDT",
        "US/Central":"CST6CDT",
        "US/Mountain":"MST7MDT",
        "US/Pacific":"PST8PDT",
        "CET":"CET",
        "UTC / GMT":"UTC",
        "BRT (Brasilia Time)":"BRT",
        "Africa/Cairo":"Africa/Cairo",
        "America/Argentina/Buenos Aires":"America/Argentina/Buenos_Aires",
        "America/Chicago":"America/Chicago",
        "America/Denver":"America/Denver",
        "America/Halifax":"America/Halifax",
        "America/Juneau":"America/Juneau",
        
        # demensions
        "Deal":"2997",
        "Placement Group":"2596",
        "Placement":"791",
        "Media Type":"5543",
        "Publisher Currency":"947",
        "Size":"790",
        "Filtered Request Reason":"4447",
        "Country":"788"
    }
    demension_id = ["786"]
    for each in Demensions.values():
        id = d[each]
        demension_id.append(id)

    headers = {
        "origin": "https://console.appnexus.com",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "accept": "application/json",
        "referer": "https://console.appnexus.com/report/publisher/run-report/16",
        "authority": "console.appnexus.com",
    }

    # the payload of request to get report_id
    null = None
    data = {
        "query": " mutation runReport($reportRequest: ReportRequestInput) { createReport(reportRequest: $reportRequest) { reportId isDuplicate errors { code message } } } ",
        "variables": {"reportRequest": {"reportType": "16", "section": "publisher", "sectionPath": "publisher",
                                        "userType": "publisher", "memberId": null, "publisherIds": [1163366],
                                        "advertiserIds": null, "id": "16", "timeInterval": "999999",
                                        "timeGranularity":"daily", "timezone": "PST8PDT",
                                        "metrics": [4854,3773,797,800,802,801],
                                        "deliveryOptions": {"runType": "RUN_NOW", "emailAddresses": null,
                                                            "format": "csv", "saveAsTemplate": null, "reportName": null,
                                                            "schedule": {
                                                                "emailAddresses": "bingfang.zou@ihandysoft.com"}},
                                        "metricModifiers": {}, "provisionalModifiers": null,
                                        "filters": [{"columnId": "818", "values": [1163366]}],
                                        "timeIntervalRange": {"start":"2018-11-01", "end": "2018-11-01"},
                                        "dimensions": ["786","791","788"]}}}

    # to get the report_id
    response_run_report = s.post("https://console.appnexus.com/report/graphql", headers=headers, json=data)
    report_id = response_run_report.json()["data"]["createReport"]["reportId"]
    print 'get the report_id successfully!'

    # the url of data
    data_url = "https://console.appnexus.com/report/data/{}.json?dataOnly=true&num_elements==500".format(report_id)
    data_json = s.get(data_url).json()["data"]
    info_json = s.get(data_url).json()['info']

    data_list = [info_json]
    for oneline in data_json:
        data_list.append(oneline)

    # to save the format of csv
    df = pandas.DataFrame(data_list)
    df.to_csv("data11.csv", encoding="utf_8_sig")

    print "Complete data crawl!"


# run function
login_crawling()


