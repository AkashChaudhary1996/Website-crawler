# -*- coding: utf-8 -*-
import scrapy
from Amazon2.items import Amazon2Item

class AmazonProductSpider(scrapy.Spider):
  name = "AmazonDeals"
  allowed_domains = ["amazon.com"]
  
  #Use working product URL below
  start_urls = [
     "http://www.amazon.in/gp/product/B01LZKSVRB"
     , "http://www.amazon.in/gp/product/B01MXHYFGM"
     , "http://www.amazon.in/gp/product/B01NAKTR2H"
     ]
 
  def parse(self, response):
      items = Amazon2Item()
      title = response.xpath('//h1[@id="title"]/span/text()').extract()
      sale_price = response.xpath('//span[contains(@id,"priceblock_ourprice") or contains(@id,"saleprice")]/text()').extract()
      category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
      availability = response.xpath('//div[@id="availability"]//text()').extract()
      items['product_name'] = ''.join(title).strip()
      items['product_sale_price'] = ''.join(sale_price).strip()
      items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
      items['product_availability'] = ''.join(availability).strip()
      yield items
