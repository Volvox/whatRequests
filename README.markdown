recursive web crawler that scrapes request titles on what.cd and CD titles at a school library to check for matches. 


**make sure the mongodb server is running!**

to run the what.cd scraper, go into the outer **what_crawler** directory and run
```bash
scrapy crawl what.cd
```

to run the library scraper, go into the outer **library_crawler** directory and run
```bash
scrapy crawl bobcat
```

after all of the titles have been scraped, run 
```bash
mongo localhost:27017/whatRequests --quiet aggregator.js
```

To change the scraper to run on a different library catalog, **library-spider.py** will need to modified.
Changes will need to be made to allowed_domains, start_urls, and the two XPaths, which can be found using the firebug copy XPath feature or using the XPath chrome extension.

If you're using windows, you will need to download [pywin32](http://sourceforge.net/projects/pywin32/) because of a bug in Twisted.
