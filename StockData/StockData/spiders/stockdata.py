# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy import log
import re
from StockData.items import StockdataItem
import datetime


class StockdataSpider(RedisSpider):
    name = 'stockdata'

    download_delay = 2  # 延时 2s

    redis_key = 'stock:download_url'

    # hdfs_info = 'http://192.168.1.11:50070'

    def parse(self, response):

        item = StockdataItem()

        self.log('响应编码： ' + response.encoding, level=log.INFO)
        self.log('解析开始！', level=log.INFO)
        self.log('响应URL： ' + str(response.url), level=log.INFO)

        # 正则取出code 上海0XXXXXX 深圳1XXXXXX
        pattern0 = re.compile('.*?code=0(\d+).*?')
        pattern1 = re.compile('.*?code=1(\d+).*?')

        # 挨个取，挨个判断
        sh_code = ''.join(pattern0.findall(response.url))  # list转string
        sz_code = ''.join(pattern1.findall(response.url))

        code = sh_code + sz_code
        item['code'] = code
        alldata = str(response.body,encoding='gbk').split("\r\n") # 切分数据，转为列表
        # 删除第一个标签元素和最后一个空元素
        alldata.pop(0)
        alldata.pop(-1)
        item['data'] = alldata
        yield item
