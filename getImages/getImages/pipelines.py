# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

class GetimagesPipeline(ImagesPipeline):

    pass

class StoreItemsPipeline():
    pass
    #def process_item(self, item):
    #    print item['addID']
    #    return item
