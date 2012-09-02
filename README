recursive web crawler that scrapes request titles on what.cd and CD titles at a school library to check for matches. 


**make sure the mongodb server is running**

to run the what.cd scraper, go into the outer **what-crawler** directory and run
```bash
scrapy crawl what.cd
```

to run the library scraper, go into the outer **library-crawler** directory and run
```bash
scrapy crawl bobcat


after all of the titles have been scraped, run 
```bash
mongo localhost:27017/whatRequests --quiet aggregator.js
```