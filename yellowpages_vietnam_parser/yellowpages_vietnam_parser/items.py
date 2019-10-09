# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YellowpagesVietnamParserItem(scrapy.Item):
    name = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    products = scrapy.Field()
    product = scrapy.Field()
    website = scrapy.Field()
    hs_code = scrapy.Field()
    date_and_time = scrapy.Field()
    source = scrapy.Field()
