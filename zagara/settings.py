# Scrapy settings for dirbot project

SPIDER_MODULES = ['zagara.spiders']
NEWSPIDER_MODULE = 'zagara.spiders'
DEFAULT_ITEM_CLASS = 'zagara.items.Website'

#ITEM_PIPELINES = {'zagara.pipelines.FilterWordsPipeline': 1}
