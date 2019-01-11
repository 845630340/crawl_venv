# -*- coding:utf8 -*-
from crawl_data_to_mongo import crawl_web

name_list = ['Toutiao']
for name in name_list:
    one_class = getattr(crawl_web, '{}Crawl'.format(name))
    instance = one_class()
    print instance.name

# ven_cls = crawl_web.ToutiaoCrawl()
# ven_cls.print_name()
'''
import gevent
from gevent import monkey
from gevent import pool

gevent_pool = pool.Pool(10)

gl = gevent.spawn(run, nm, vendor)
gevent_pool.add(gl)

gevent_pool.join()
'''
