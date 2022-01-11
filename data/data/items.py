# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataItem(scrapy.Item):
    p_name = scrapy.Field()
    brand = scrapy.Field()
    s_name = scrapy.Field()
    price = scrapy.Field()
    positive_rating = scrapy.Field()
    p_fee = scrapy.Field()
