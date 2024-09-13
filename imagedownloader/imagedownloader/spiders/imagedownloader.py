import scrapy

from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from config import yurl


class ImageSpider(scrapy.Spider):
    name = "image_spider"
    start_urls = [yurl]  # Replace with your target URL

    def parse(self, response):
        # Extract image URLs
        image_urls = response.css('img::attr(src)').getall()
        # Make the URLs absolute
        image_urls = [response.urljoin(url) for url in image_urls]
        # Yield a dictionary containing the image URLs
        yield {'image_urls': image_urls}

