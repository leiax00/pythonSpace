# encoding:utf-8
import os
from abc import ABC

import scrapy.cmdline


class Book3Spider(scrapy.Spider, ABC):
    name = 'books'

    def __init__(self):
        # super.__init__()
        root = 'https://www.haotxt.com'
        self.start_urls = ['%s/xiaoshuo/26/26975/' % root]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_biquge)

    def parse_biquge(self, response):
        for page in response.css('td.ccss a'):
            page = page.css('a::attr(href)').extract_first()
            print('page_url:', page)
            yield {'url': page}


if __name__ == '__main__':
    file_path = os.path.join('..', 'temp', 'books.csv')
    scrapy.cmdline.execute(['scrapy', 'crawl', 'books', '-o', file_path])
