import json

from scrapy import Request, Spider
from ..items import TierarztItem


def get_score(item):
    total = int(item['score_4_int']) + int(item['score_3_int']) + int(
        item['score_2_int']) + int(item['score_1_int']) + int(
        item['score_overall_int'])
    return total / 5


class ZooplusSpider(Spider):
    name = 'zooplus'
    start_urls = ['https://www.zooplus.de/tierarzt/api/v2/token?'
                  'debug=authReduxMiddleware-tokenIsExpired']

    def parse(self, response):
        token = 'Bearer ' + json.loads(response.text)['token']
        for i in range(1, 4):
            yield Request(f'https://www.zooplus.de/tierarzt/api/v2/results?'
                          f'animal_99=true&page={i}&from=0&size=20',
                          self.parse_page, headers={'authorization': token})

    def parse_page(self, response):
        item = TierarztItem()
        results = json.loads(response.text)['results']
        for result in results:
            item['name'] = result['name']
            item['subtitle'] = 'None'
            if 'subtitle' in result:
                item['subtitle'] = result['subtitle']
            item['open_time'] = result['open_time']
            item['address'] = (f"{result['address']}, {result['zip']} ,"
                               f"{result['city']}")
            item['score'] = get_score(result['reviews_nest'][0])
            item['comments'] = len(result['reviews_nest'])
            yield item
