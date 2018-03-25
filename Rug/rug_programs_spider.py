import scrapy
import os

class RugSpider(scrapy.Spider):
    name = 'Rugspider'
    start_urls = ['https://www.rug.nl/ocasys/rug/main/browseByFaculty']

    def parse(self, response):
        for title in response.css('ul li a#nodeNotSelected'):
            yield { 'link' : title.css('a').extract() }