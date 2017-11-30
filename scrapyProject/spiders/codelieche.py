# -*- coding: utf-8 -*-
import scrapy
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from selenium import webdriver


class CodeliecheSpider(scrapy.Spider):
    name = 'codelieche'
    allowed_domains = ['codelieche.com']
    start_urls = ['http://codelieche.com/']

    def __init__(self):
        # 当爬虫实例化的时候，打开个浏览器，当爬虫执行完毕的时候，通过信号关闭浏览器
        self.browser = webdriver.Chrome()
        super(CodeliecheSpider, self).__init__()

        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def spider_closed(self, spider):
        # 当爬虫退出的时候，关闭浏览器
        print("spider closed: ", spider.name)
        self.browser.quit()

    def parse(self, response):
        pass
