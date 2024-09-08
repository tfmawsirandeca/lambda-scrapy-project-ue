import scrapy
from scrapy_project.scrapy_project.items import ProductScraperItem


class ExampleSpiderSpider(scrapy.Spider):
    name = "example_spider"
    allowed_domains = ["delicatessenspain.es"]
    start_urls = ["https://delicatessenspain.es/es/23-aceite-de-oliva?q=Capacidad-1+l."]

    def parse(self, response):
        products = response.xpath('//section[@id="products"]//article[contains(@class, "product-miniature")]')

        for product in products:
            item = ProductScraperItem()
            item['name'] = product.xpath('.//h1[contains(@class, "product-title")]/a/text()').get()
            item['price'] = product.xpath('.//div[contains(@class, "product-price-and-shipping")]/span[@itemprop="price"]/text()').get()
            yield item