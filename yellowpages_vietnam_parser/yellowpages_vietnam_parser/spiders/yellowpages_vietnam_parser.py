import scrapy
from ..items import YellowpagesVietnamParserItem
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "yellowpages_vietnam_parser"

    def start_requests(self):
        url = 'https://www.yellowpages.vnn.vn/psrch/vi%E1%BB%87t_nam/' + str(self.product) + '.html'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for href in response.xpath('//a[@class="buttonMoreDetails"]/@href').getall():
            yield response.follow(href, self.parse_company_products)
        next_page = response.xpath('//div[@id="paging"]/a[@class="page_active"][3]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_company_products(self, response):
        item = YellowpagesVietnamParserItem()
        products = response.xpath('//div[@class="div_sanphamdichvu"]/p/a/text()').getall()
        phone = response.xpath('//div[@id="detail_diachi_box"]/p[@class="diachi_box_p"]/span[@class="span_mathoai"]/text()').get()
        name = response.xpath('//h1[@id="company_name_h1"]/text()').get()
        email = response.xpath('//div[@id="detail_diachi_box"]/p[@class="diachi_box_p"]/a/text()').get()
        website = response.xpath('//div[@id="detail_diachi_box"]/p[@class="diachi_box_p"]/a[@class="a_link"]/@href').get()
        date_and_time = datetime.now().strftime('%d-%m %H:%M')
        item['name'] = name
        item['phone'] = phone
        item['email'] = email
        item['website'] = website
        item['products'] = products
        item['product'] = str(self.product)
        item['hs_code'] = self.hs_code
        item['source'] = 'https://www.yellowpages.vnn.vn'
        item['date_and_time'] = date_and_time
        yield item
