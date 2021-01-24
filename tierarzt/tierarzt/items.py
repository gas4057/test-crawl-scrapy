import scrapy


class TierarztItem(scrapy.Item):
    name = scrapy.Field()
    subtitle = scrapy.Field()
    open_time = scrapy.Field()
    address = scrapy.Field()
    score = scrapy.Field()
    comments = scrapy.Field()
    pass
