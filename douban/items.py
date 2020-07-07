# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # add:爬起内容
    #序号
    serial_number = scrapy.Field()
    #电影名称
    movie_name = scrapy.Field()
    #电影介绍
    introduce = scrapy.Field()
    #星级
    star = scrapy.Field()
    #电影评论
    evaluate = scrapy.Field()
    #电影描述
    describe = scrapy.Field()

