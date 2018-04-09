# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    review_rating = scrapy.Field()       #评价等级，1-5星
    review_num = scrapy.Field()          #评价数量
    upc = scrapy.Field()                 #产品编码
    stock = scrapy.Field()               #库存量
