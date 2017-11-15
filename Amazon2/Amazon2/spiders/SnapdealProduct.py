# -*- coding: utf-8 -*-
import scrapy
from Amazon2.items import Amazon2Item

class SnapdealProductSpider(scrapy.Spider):
  name = "SnapdealDeals"
  allowed_domains = ["snapdeal.com"]
  
  #Use working product URL below
  start_urls = [
     "https://www.snapdeal.com/product/apple-iphone-7-32gb-gold/5764608149132713628"
     ]
 
  def parse(self, response):
      items = Amazon2Item()
      title = response.xpath('//h1[@class="pdp-e-i-head"]/text()').extract()
      sale_price = response.xpath('//div[@class="pdpCutPrice"]/span[@class="pdp-final-price"]/span[@class="payBlkBig"]/text()').extract()
      category = response.xpath('//a[@class="bCrumbOmniTrack"]/span/text()').extract()
    #  availability = response.xpath('//div[@id="availability"]//text()').extract()
      items['product_name'] = ''.join(title).strip()
      items['product_sale_price'] = ''.join(sale_price).strip()
      items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
     # items['product_availability'] = ''.join(availability).strip()
      yield items
