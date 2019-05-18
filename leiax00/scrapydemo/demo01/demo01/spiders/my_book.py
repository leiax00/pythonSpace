# encoding:utf-8
import os
import re

import scrapy.cmdline


class BookSpider(scrapy.Spider):
    name = 'books'

    def __init__(self):
        # super.__init__()
        self.start_urls = ['https://www.tianxiabachang.cn/5_5166/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_biquge)

    def parse_biquge(self, response):
        for book in response.css('body div.box_con div#maininfo'):
            info = book.css('div#info')
            name = info[0].css('h1::text').extract_first()
            author = info[0].css('p')[0].css('p::text').extract_first()
            last_fresh = info[0].css('p')[2].css('p::text').extract_first()
            author = re.split(u'[:：]', author)[1].strip()
            last_fresh = re.split(u'[:：]', last_fresh)[1].strip()
            result = {
                'name': name,
                'author': author,
                'last_fresh': last_fresh,
            }
            print(result)
            yield result


if __name__ == '__main__':
    file_path = os.path.join('..', 'temp', 'books.csv')
    scrapy.cmdline.execute(['scrapy', 'crawl', 'books', '-o', file_path])
