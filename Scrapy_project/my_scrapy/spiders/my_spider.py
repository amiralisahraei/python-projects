import scrapy
from my_scrapy.items import MyScrapyItem


class MySider(scrapy.Spider):

    name = "new_spider"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for article in response.xpath("//small[@class='author']/text()").extract():
            item = MyScrapyItem()
            item["author"] = article
            yield item
