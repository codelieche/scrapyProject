# -*- coding:utf-8 -*-
"""
codelieche爬取数据用到的中间件
"""
import time

from selenium import webdriver
from scrapy.http import HtmlResponse


class ChromeMiddlewware(object):
    """
    使用chrome去打开网页的中间件
    打开网页后获取页面的源码
    需要配置在scrapyProject.settings.py的DOWNLOADER_MIDDLEWARES中
    """

    def __init__(self):
        # 注意把webdriver加入到path中
        # self.browser = webdriver.Chrome()
        super(ChromeMiddlewware, self).__init__()

    # 通过chrome请求动态网页
    def process_request(self, request, spider):
        # 当爬虫的名字含有chrome，那么我们就使用spider.browser打开网页
        # 当然也可以指定name == xxx才使用browser打开页面
        if spider.name.find("chrome") >= 0:
            spider.browser.get(url=request.url)
            print("访问：{}".format(request.url))
            time.sleep(5)

            # 用浏览器访问后，就不需要再去下载器下载一遍了，要不就重复了
            # 返回个HtmlResponse的实例，就不会再去下载器下载了
            # 不同站点，不同网页编码可能不是utf-8的，自己注意处理
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source,
                                encoding="utf-8", request=request)

