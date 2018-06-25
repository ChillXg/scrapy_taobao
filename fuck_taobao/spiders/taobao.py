# -*- coding: utf-8 -*-
import scrapy
import re
from fuck_taobao.items import FuckTaobaoItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com', 's.taobao.com','detail.tmall.com','item.taobao.com']
    url = 'https://s.taobao.com/search?q=t%E6%81%A4&bcoffset=0&ntoffset=0&s='
    taobao_detail_url = 'https://item.taobao.com/item.htm?id='
    tmall_detail_url = 'detail.tmall.com/item.htm?id='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        body = response.body.decode('utf-8', 'ignore')
        pattern = re.compile('"nid":"(.*?)"')
        ids = pattern.findall(body, re.S)
        for id in ids:
            url = self.taobao_detail_url + str(id)
            yield scrapy.Request(url, callback=self.detail_parse)

    def detail_parse(self, response):
        if 'taobao' in str(response):
            body = response.body.decode('gbk', 'ignore')
            print(body)
            shop_name = re.compile("shopName")


