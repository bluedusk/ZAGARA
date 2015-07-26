from scrapy.spiders import Spider
from scrapy.selector import Selector

from zagara.items import CityAQI


class AqiSpider(Spider):
    name = "aqi"
    allowed_domains = ["aqicn.org"]
    start_urls = [
        "http://aqicn.org/city/beijing/en/",
       # "http://aqicn.org/city/shanghai/en/",
        #"http://aqicn.org/city/guangzhou/en/",
        #"http://aqicn.org/city/chengdu/en/",

    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//div[@class="aqivalue"][1]')
        city = sel.xpath('//title')
        url = response.url
        url = url[22:len(url)-4]
        items = []

        for site in sites:
            item = CityAQI()
            item['value'] = site.xpath('text()').extract()
            item['city'] = url

            items.append(item)
        return items
