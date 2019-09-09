# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
import json
from StockList.items import StocklistItem


class StocklistSpider(RedisSpider):
    name = 'stocklist'

    # sadd stock:start_url http://94.push2.eastmoney.com/api/qt/clist/get?&pn=1&pz=20&po=1&np=2&fltt=2&fid=f3&fs=m:1+t:2&fields=f12,f14
    # sadd stock:start_url http://2.push2.eastmoney.com/api/qt/clist/get?&pn=1&pz=20&po=1&np=2&fltt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80&fields=f12,f14

    redis_key = 'stock:start_url'

    # 股票下载历史数据URL片段
    download_url_piece = 'http://quotes.money.163.com/service/chddata.html?code='

    def parse(self, response):
        item = StocklistItem()
        try:
            if response.status == 200:
                resultJson = json.loads(response.body.decode('utf-8'))
                diff = resultJson['data']['diff']  # 股票代码在 diff 字段中
                # print(diff)
                if str(response.url) == 'http://94.push2.eastmoney.com/api/qt/clist/get?&pn=1&pz=20&po=1&np=2&fltt=2&fid=f3&fs=m:1+t:2&fields=f12,f14':
                    # self.shStock(diff)
                    print('开始解析上海股票代码！')
                    for i in diff:
                        code = diff[str(i)]['f12']  # 取出代码
                        # self.R.sadd('stock:code_list', code)
                        item['code'] = code

                        sh_download_url = self.download_url_piece + '0' + code

                        item['download_url'] = sh_download_url

                        yield item
                else:
                    # self.szStock(diff)
                    # print('=' * 40)
                    item = StocklistItem()
                    print('开始解析深圳股票代码！')
                    for i in diff:
                        code = diff[str(i)]['f12']  # 取出代码
                        # self.R.sadd('stock:code_list', code)
                        item['code'] = code

                        sz_download_url = self.download_url_piece + '1' + code
                        item['download_url'] = sz_download_url

                        print(sz_download_url)

                        yield item
        except Exception as e:
            print(e)
