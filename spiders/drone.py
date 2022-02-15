# -*- coding: utf-8 -*-
import scrapy


class DroneSpider(scrapy.Spider):
    name = 'drone'
    allowed_domains = ['https://www.jessops.com/drones']
    start_urls = ['http://https://www.jessops.com/drones/']

    def parse(self, response):
        pass
