from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "newscraper"
    start_urls = [
        'https://www.novinky.cz/sekce/domaci-13',
        'https://domaci.hn.cz/',
        'https://www.ceskenoviny.cz/cr/',
        'https://zvedavec.news/regiony/cr/',
        'https://protiproud.info/',
        'https://www.ac24.cz/',
        'https://www.parlamentnilisty.cz/'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')