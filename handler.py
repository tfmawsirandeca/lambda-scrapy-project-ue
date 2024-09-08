import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from scrapy import signals
from scrapy_project.scrapy_project.spiders.aceite_oliva_spider import AceiteOlivaSpider
from scrapy_project.scrapy_project.spiders.calamar_spider import CalamarSpiderSpider
from scrapy_project.scrapy_project.spiders.camaron_spider import CamaronSpiderSpider
from scrapy_project.scrapy_project.spiders.pimiento_spider import PimientoSpiderSpider
from scrapy_project.scrapy_project.spiders.tomate_spider import TomateSpiderSpider

def lambda_handler(event, context):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(dict(item))

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(AceiteOlivaSpider)
    process.crawl(CalamarSpiderSpider)
    process.crawl(CamaronSpiderSpider)
    process.start()

    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
