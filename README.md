### 东方财富网沪深A股分布式爬虫

实际是两个爬虫：

- StockList部分用于爬取股票数据下载链接存入redis

- StockData部分从redis中获取下载链接并将数据存入MongoDB

运行环境：

[environment.yaml](./environment.yaml)

@


