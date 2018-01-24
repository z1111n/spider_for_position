# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Job.items import JobItem


class JobSpider(CrawlSpider):
    name = 'job'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E5%B7%9E&kw=python&sm=0&p=1']

    rules = (
        Rule(LinkExtractor(allow=r'http://sou.zhaopin.com/jobs/searchresult.ashx\?.+(p=\d+)$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item=JobItem()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
        node_list=response.xpath("//table[@class='newlist']")
        for node in node_list:
            item['position_desc']=response.xpath(".//td[@class='zwmc']/div/a/text()").extract()[0]
            item['position_link']=response.xpath(".//td[@class='zwmc']/div/a/@href").extract()[0]
            item['company_name']=response.xpath(".//td[@class='gsmc']/a[1]/text()").extract()[0]
            item['salary']=response.xpath(".//td[@class='zwyx']/text()").extract()[0]
            item['location']=response.xpath(".//td[@class='gzdd']/text()").extract()[0]
            try:
                item['post_time']=response.xpath(".//td[@class='gxsj']/span/text()").extract()[0]
            except:
                item['post_time']='none'

        yield item
