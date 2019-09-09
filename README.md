### 东方财富网沪深A股分布式爬虫

**实际是两个爬虫：**

StockList部分用于爬取股票数据下载链接存入redis

StockData部分从redis中获取下载链接并将数据存入MongoDB

**主要的依赖库：**

```
Python-3.5

scrapy-1.5.1

scrapy-redis-0.6.8

pymongo==3.8.0

```

具体可查看conda环境配置文件：[environment.yaml](./environment.yaml)

**已经实现的功能：**

- 分布式爬取

- 随机用户代理

- 爬取完成自动停止

**待完善的功能：**

- 随机IP

- Zookeeper集群监控

- 邮件提醒




