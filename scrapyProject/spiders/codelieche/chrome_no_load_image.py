# -*- coding: utf-8 -*-
"""
这个spider是通过chrome打开网页下载内容
同时设置不加载图片!!!!
注意点：
1. chromedriver：需要是Chrome对应的版本【一般推荐最新】否则会无效
2. http://chromedriver.storage.googleapis.com/index.html
3. 下载器中间件，需要实现process_request方法，并且需要返回个scrapy.http.HtmlResponse对象
4. ChromeMiddleware需要配置在：scrapyProject.settings.py的DOWNLOADER_MIDDLEWARES中
"""
import time

import scrapy
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from selenium import webdriver


class CodeliecheSpider02(scrapy.Spider):
    name = 'codelieche_chrome_no_load_image'
    allowed_domains = ['codelieche.com']
    start_urls = ['http://codelieche.com/']

    def __init__(self):
        # 当爬虫实例化的时候，打开个浏览器，当爬虫执行完毕的时候，通过信号关闭浏览器
        chrome_options = webdriver.ChromeOptions()
        # 设置不加载图片
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super(CodeliecheSpider02, self).__init__()

        # 通过信号触发,closed事件
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def spider_closed(self, spider):
        # 当爬虫退出的时候，关闭浏览器
        print("spider closed: ", spider.name)
        time.sleep(30)
        self.browser.quit()

    def parse(self, response):
        print("默认的parse:处理页面{}".format(response.url))
        time.sleep(5)
        pass
