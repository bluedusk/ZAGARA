from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import datetime
import time

from zagara.items import CityAQI


class AqiUSSpider(Spider):
    name = "aqius"
    allowed_domains = ["www.stateair.net"]
    start_urls = [
        "http://www.stateair.net/web/rss/1/1.xml"
        ,"http://www.stateair.net/web/rss/1/2.xml"
        ,"http://www.stateair.net/web/rss/1/3.xml"
        ,"http://www.stateair.net/web/rss/1/4.xml"
    

    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        aqis = sel.xpath('//item')
        aqi = sel.xpath('//item[1]')
        #aqis.extract()
        url = response.url
        city = sel.xpath('//channel/title/text()').extract()
        city = city[0].split(" ")[4].lower()

        
        dt = datetime.now() 
        items = []

        item = CityAQI()
        item['value'] = int(aqi.xpath('.//AQI/text()').extract()[0])
        item['city'] = city
        item['updateTime'] = aqi.xpath('.//ReadingDateTime/text()').extract()[0]
        t = time.strptime(item['updateTime'], '%m/%d/%Y %I:%M:%S %p')
        item['year'] = t[0]
        item['month'] = t[1]
        item['day'] = t[2]
        item['hour'] = t[3]
        item['crawlTime'] = dt.strftime('%H:%M') 
        item['date'] = dt.strftime('%Y-%m-%d') 
        return item 

"""
        for aqi in aqis:
            item = CityAQI()
            item['value'] = aqi.xpath('.//AQI/text()').extract()
            item['city'] = city
            item['updateTime'] = aqi.xpath('.//ReadingDateTime/text()').extract()
            item['crawlTime'] = dt.strftime('%H:%M') 
            item['date'] = dt.strftime('%Y-%m-%d') 
            items.append(item)
        return items
"""