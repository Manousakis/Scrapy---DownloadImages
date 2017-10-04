#!/usr/bin/python
# coding=utf-8

from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from getImages.items import GetimagesItem

class img(CrawlSpider):

    name = "img"
    download_delay = 2
    allowed_domains = ["xe.gr"]

    start_urls = ["http://www.xe.gr/property/search?System.item_type=re_land&Transaction.type_channel=117518&Geo.area_id_new__hierarchy=82206&Item.city_plan=31887"]

    rules = (Rule(LxmlLinkExtractor(allow_domains = ('xe.gr'), restrict_xpaths = ("//a[@class='white_button right']")), callback='parse_start_url', follow=True),)

    def parse_start_url(self, response):
        return self.parse_items(response)

    def parse_items(self, response):
        for sel in response.xpath("//div[contains(@class,'r_desc')]/h2/a"):
            link = "http://www.xe.gr"+sel.xpath("@href").extract_first()+"?mode=spec"
            yield Request(link, callback=self.parse2)

    def parse2(self, response):
        #Creating an empty item
        item = GetimagesItem()
        item['url'] = response.url
        try:
            item['addID'] = int(response.xpath('//*[@id="breadcrumb"]/li[4]/span[2]').extract_first().strip(u'<span style="color: #aaa;">με κωδικό').strip(u'</'))
        except:
            print "critical error"
        item['image_urls'] = ['http://www.xe.gr/property/phoneimg?sys_id='+str(item['addID'])+'rev1',
        'http://www.xe.gr/property/phoneimg?sys_id='+str(item['addID'])+'rev2',
        'http://www.xe.gr/property/phoneimg?sys_id='+str(item['addID'])+'rev3',
        'http://www.xe.gr/property/phoneimg?sys_id='+str(item['addID'])+'rev4',
        'http://www.xe.gr/property/phoneimg?sys_id='+str(item['addID'])+'rev5']
        yield item
