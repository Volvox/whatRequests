from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from whatCrawler.items import WhatItem
from scrapy.utils.response import get_base_url 
import re


class RequestSpider(BaseSpider):
    name = "what.cd"
    allowed_domains = ["what.cd"]
    start_urls = [
        "http://www.what.cd/login.php"
    ]
  
    def parse(self, response):
        name = raw_input("username > ")
        passw = raw_input("password > ")
        return [FormRequest.from_response(response,
                    formdata={'username': name, 'password': passw},
                    callback=self.after_login)]


    def after_login(self, response):

        if "login" in response.body:
            print("Login failed")
            return
        else:
            return Request(url="http://what.cd/requests.php", callback=self.parse_requests)
    
    
    def parse_requests(self, response):
        x = HtmlXPathSelector(response)
        next_link = ("http://what.cd/" + x.select("//div[@class='linkbox']/a[@class='pager_next']/@href").extract()[0])

        if not not next_link:

            #crawl pages recursively to scan through all of the requests
            yield Request(next_link, self.parse_requests)

        albums = x.select("//tr[@class='rowb']/td/a/text()").extract()
        items = []
       

        for album in albums:
            item = WhatItem()

            #regular expression for identifying links which incl. bracketed dates.
            p1 = re.compile('\[[^\]]*\]') 
            p2 = re.compile('\[[2012\]]*\]') 

            # find links with [date]
            date = p1.search(album) 

             # find links with [2012] release date and exclude from results because library will not have new releases
            d2012 = p2.search(album)

            #store all of the links that are titles and were not released in 2012
            if date != None and d2012 == None:
                item['name'] = re.sub('\[[^\]]*\]','',album) #get rid of [date]
                item['name'] = item['name'].strip()
                items.append(item)
           
        
        for item in items:  
            yield item