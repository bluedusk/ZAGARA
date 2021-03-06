from scrapy.item import Item, Field


class CityAQI(Item):

    value = Field()
    city = Field()
    updateTime = Field()
    crawlTime = Field()
    date = Field()
    year = Field()
    month = Field()
    day = Field()
    hour = Field()
    _id = Field() #error if without _id

