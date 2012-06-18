from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from whatRequests.items import WhatItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.utils.response import get_base_url 
import re
import json 


class LibraryQuery(BaseSpider):
    name = "bobcat"
    allowed_domains = ["aleph.library.nyu.edu/"]
    start_urls = [
        "http://aleph.library.nyu.edu/F/BHQBVPL8VSSSX6S67YQ9NBRIJGBF3BMLHXANI6PF7FI3N9DTQ2-00297?func=scan-ind-continue&code=ALL&find_scan_code=ALL&filing_text=xcd!"
    ]


    def parse(self, response):
        print("newgin")
        x = HtmlXPathSelector(response)
        n=1
        n += 1
        num = 20 * n
        next_link = "http://aleph.library.nyu.edu/F/BHQBVPL8VSSSX6S67YQ9NBRIJGBF3BMLHXANI6PF7FI3N9DTQ2-01107?func=scan-ind-continue&code=ALL&find_scan_code=ALL&filing_text=xcd!" + str(num)
        
        if not not next_link:

            #crawl pages recursively to scan through all of the requests
            yield Request(next_link, self.parse)
        
        albums = x.select("//form/fieldset/h3/strong/text()").extract()
        items = []
        for album in albums:
            item = WhatItem()
            item['name'] = album 
            items.append(item)
                
        for item in items:  
            yield item
                   
