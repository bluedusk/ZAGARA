from scrapy.item import Item, Field


class CityAQI(Item):

    value = Field()
    city = Field()

