# -*- coding:utf-8 -*-
"""
运行scrapy的脚本
主要是为了用于调试
"""
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# 1. codelie的相关爬虫
# 1-1：使用chrome的中间件打开网页，获取page_soource
# execute(["scrapy", "crawl", "codelieche_chrome"])

# 1-2: 使用chrome的中间件打开网页，同时不加载图片
execute(["scrapy", "crawl", "codelieche_chrome_no_load_image"])
