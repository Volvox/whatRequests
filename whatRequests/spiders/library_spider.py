from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from whatRequests.items import WhatItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.utils.response import get_base_url 
import re


class LibraryQuery(BaseSpider):
    name = "bobcat"
    allowed_domains = ["bobcat.library.nyu.edu/"]
    start_urls = [
        "http://bobcat.library.nyu.edu/primo_library/libweb/action/search.do?dscnt=0&vl(378633853UI1)=audio&scp.scps=scope%3A%28NS%29%2Cscope%3A%28CU%29%2Cscope%3A%28%22BHS%22%29%2Cscope%3A%28NYU%29%2Cscope%3A%28%22NYSID%22%29%2Cscope%3A%28%22NYHS%22%29%2Cscope%3A%28GEN%29%2Cscope%3A%28%22NYUAD%22%29&frbg=&tab=all&dstmp=1344970916843&srt=rank&ct=search&mode=Basic&dum=true&vl(212921975UI0)=any&indx=1&vl(1UIStartWith0)=contains&vl(freeText0)=XCD&vid=NYU&fn=search"
    ]

    def parse(self, response):
        x = HtmlXPathSelector(response)
        next_link = (x.select("//div[@class='pagination']/div/a[@class='next']/@href").extract()[0])
        print(next_link + "newgin")

        if not not next_link:

            #crawl pages recursively to scan through all of the requests
            yield Request(next_link, self.parse)
        
        albums = x.select("//h2[@class='title']/a/text()").extract()
        items = []

        for album in albums:
            item = WhatItem()           
            item['name'] = re.sub(r'[\t\n]*','',album)
            item['name'] = re.sub(r'\[[^\]]*\]','',item['name'])
            item['name'] = item['name'].strip()
            items.append(item)
  
        for item in items:  
            yield item
                   
