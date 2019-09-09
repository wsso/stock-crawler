# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
from scrapy.conf import settings

class StocklistPipeline(object):

    # redis连接池
    pool = redis.ConnectionPool(host=settings['REDIS_HOST'], port=settings['REDIS_PORT'], decode_responses=True)

    def __init__(self):
        print('StocklistPipeline __init__')

    def process_item(self, item, spider):
        try:
            R = redis.Redis(connection_pool=self.pool)
            R.sadd('stock:code_list', item['code'])
            R.sadd('stock:download_url',item['download_url'])
        except Exception as e:
            print(e)

        return item
