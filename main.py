# -*- coding:utf-8 -*-
"""
运行scrapy的脚本
主要是为了用于调试
"""
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "crawl", "codelieche_chrome"])
