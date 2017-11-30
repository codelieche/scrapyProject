# -*- coding: utf-8 -*-
"""
这个spider是通过chrome打开网页下载内容
注意点：
1. 下载器中间件，需要实现process_request方法，并且需要返回个scrapy.http.HtmlResponse对象
2. ChromeMiddleware需要配置在：scrapyProject.settings.py的DOWNLOADER_MIDDLEWARES中
"""
import scrapy
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from selenium import webdriver


class CodeliecheSpider(scrapy.Spider):
    name = 'codelieche_chrome'
    allowed_domains = ['codelieche.com']
    start_urls = ['http://codelieche.com/']

    def __init__(self):
        # 当爬虫实例化的时候，打开个浏览器，当爬虫执行完毕的时候，通过信号关闭浏览器
        self.browser = webdriver.Chrome()
        super(CodeliecheSpider, self).__init__()

        # 通过信号触发,closed事件
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def spider_closed(self, spider):
        # 当爬虫退出的时候，关闭浏览器
        print("spider closed: ", spider.name)
        self.browser.quit()

    def parse(self, response):
        pass
