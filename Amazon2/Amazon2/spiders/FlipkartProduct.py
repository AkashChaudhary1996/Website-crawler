# -*- coding: utf-8 -*-
import scrapy
from Amazon2.items import Amazon2Item

class FlipkartProductSpider(scrapy.Spider):
  name = "FlipkartDeals"
  allowed_domains = ["flipkart.com"]
  
  #Use working product URL below
  start_urls = [
     "https://www.flipkart.com/apple-iphone-7-black-128-gb/p/itmen6daqhtbuzhj?pid=MOBEMK62E7YZEVZ8&srno=s_1_14&otracker=search&lid=LSTMOBEMK62E7YZEVZ8A5YBOS&fm=SEARCH&iid=fbe17cfb-379d-4e42-9e7a-6e81d6950d36.MOBEMK62E7YZEVZ8.SEARCH&qH=5d05ddab4536111a"
     ]
 
  def parse(self, response):
      items = Amazon2Item()
      title = response.xpath('//h1[@class="_3eAQiD"]/text()').extract()
      sale_price = response.xpath('//div[@class="_1vC4OE _37U4_g"]/text()').extract()
      category = response.xpath('//a[@class="_1KHd47"]/text()').extract()
    #  availability = response.xpath('//div[@id="availability"]//text()').extract()
      items['product_name'] = ''.join(title).strip()
      items['product_sale_price'] = ''.join(sale_price).strip()
      items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
     # items['product_availability'] = ''.join(availability).strip()
      yield items
