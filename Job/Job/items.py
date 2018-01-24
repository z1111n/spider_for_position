# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_desc = scrapy.Field()
    position_link=scrapy.Field()
    company_name = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    post_time = scrapy.Field()
