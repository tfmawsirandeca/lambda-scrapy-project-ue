import scrapy
from scrapy_project.scrapy_project.items import ProductScraperItem


class PimientoSpiderSpider(scrapy.Spider):
    name = "pimiento_spider"
    allowed_domains = ["juntadeandalucia.es"]
    start_urls = ["https://www.juntadeandalucia.es/agriculturaypesca/observatorio/servlet/FrontController?ec=default"]

    def parse(self, response):
            amount = response.xpath('/html/body/div[2]/div/div[2]/div/div/div/div[4]/div[3]/a/div/div[4]/div[1]').get()
            print('PIMIENTO')
            print(amount)
            item = ProductScraperItem()
            item['name'] = 'PIMIENTO'
            item['price'] = str(float(amount)*100)
            item['description'] = '1'
            item['unit_measurement'] = 'kg'
            yield item