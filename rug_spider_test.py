import scrapy
import os

class RugSpider(scrapy.Spider):
    name = 'Rugspider'
    start_urls = ['http://localhost/MEGA/rug.html']

    def parse(self, response):
        for title in response.css('.body > table.userTable tbody tr'):
            yield {
                'periode': title.css('td:nth-child(1) ::text').extract(),
                'type': title.css('td:nth-child(2) ::text').extract(),
                'code': title.css('td:nth-child(3) ::text').extract(),
                'naam': title.css('td:nth-child(4) ::text').extract()
                }