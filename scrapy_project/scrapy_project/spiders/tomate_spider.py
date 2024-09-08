import scrapy
from scrapy_project.scrapy_project.items import ProductScraperItem


class TomateSpiderSpider(scrapy.Spider):
    name = "tomate_spider"
    allowed_domains = ["juntadeandalucia.es"]
    start_urls = ["https://www.juntadeandalucia.es/agriculturaypesca/observatorio/servlet/FrontController?ec=default"]

    def parse(self, response):
            amount = response.xpath('//*[@id="myCarousel"]/div/div[5]/div[2]/a/div/div[4]/div[1]/text()').get().replace(' €', '').replace(',', '.')
            item = ProductScraperItem()
            item['name'] = 'TOMATE'
            item['price'] = str(float(amount)*100)
            item['description'] = '500'
            item['unit_measurement'] = 'g'
            yield item