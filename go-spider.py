from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_new.spiders.flipkart import FlipkartProductSpider

process = CrawlerProcess(get_project_settings())
process.crawl(FlipkartProductSpider)
process.start()
