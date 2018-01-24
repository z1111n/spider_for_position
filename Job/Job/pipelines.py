# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class JobPipeline(object):
    def __init__(self):
        self.file=open('position_list.json','w',encoding='UTF-8')

    def process_item(self, item, spider):
        content=json.dumps(dict(item),ensure_ascii=False)
        self.file.write(content)

        return item

    def close_spide(self,item,spider):
        self,file.close()