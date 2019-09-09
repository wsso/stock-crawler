# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockdataItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    data = scrapy.Field()
    # date = scrapy.Field() # 日期
    # closingPrice = scrapy.Field() # 收盘价
    # topPrice = scrapy.Field() # 最高价
    # bottomPrice = scrapy.Field() # 最低价
    # openingPrice = scrapy.Field() # 开盘价
    # BeforeClosing = scrapy.Field() # 前收盘
    # changeAmount = scrapy.Field() # 涨跌额
    # change = scrapy.Field() # 涨跌幅
    # turnoverRate = scrapy.Field() # 换手率
    # turnover = scrapy.Field() # 成交量
    # amount = scrapy.Field() # 成交金额
    # totalValue = scrapy.Field() # 总市值
    # circulationMarketValue = scrapy.Field() # 流通市值
    # fixtureNumber = scrapy.Field() # 成交笔数