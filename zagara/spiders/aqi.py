from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import datetime

from zagara.items import CityAQI


class AqiSpider(Spider):
    name = "aqi"
    allowed_domains = ["aqicn.org"]
    start_urls = [
        "http://aqicn.org/city/beijing/en/",
        "http://aqicn.org/city/shanghai/en/",
        "http://aqicn.org/city/guangzhou/en/",
        "http://aqicn.org/city/chengdu/en/",

    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        updateTime = sel.xpath('//div[@style="font-size:16px;font-weight:light;;"][1]/text()').extract()
        updateTime = updateTime[0].split()[3]

        sites = sel.xpath('//div[@class="aqivalue"][1]')
        city = sel.xpath('//title')

        url = response.url
        url = url[22:len(url)-4]

        dt = datetime.now()  


        items = []

        for site in sites:
            item = CityAQI()
            item['value'] = site.xpath('text()').extract()[0]
            item['city'] = url
            item['updateTime'] = updateTime
            item['crawlTime'] = dt.strftime('%H:%M') 
            item['date'] = dt.strftime('%Y-%m-%d') 
            items.append(item)
        return items
