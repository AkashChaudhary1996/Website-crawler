# -*- coding: utf-8 -*-
import scrapy
from Amazon2.items import Amazon2Item

class SnapdealProductSpider(scrapy.Spider):
  name = "PaytmDeals"
  allowed_domains = ["paytm.com"]
  
  #Use working product URL below
  start_urls = [
     "https://paytmmall.com/apple-iphone-7-32-gb-black-CMPLXMOBAPPLE-IPHONEDUMM14169CBA1E1-pdp?src=grid&tracker=%7C%7C%7C%7C%2Fg%2Fmobile-accessories%2Fmobiles/reco-v2%7C6224%7C3%7C%7C0000000161DA4E2F9421FE7AE9A1F285179DA9FC%7C"
     ]
 
  def parse(self, response):
      items = Amazon2Item()
      title = response.xpath('//h1[@class="NZJI"]/text()').extract()
      sale_price = response.xpath('//span[@class="_1y_y"]/text()').extract()
      category = response.xpath('//a[@class="Tk9i_2mNr"]/span/text()').extract()
    #  availability = response.xpath('//div[@id="availability"]//text()').extract()
      items['product_name'] = ''.join(title).strip()
      items['product_sale_price'] = ''.join(sale_price).strip()
      items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
     # items['product_availability'] = ''.join(availability).strip()
      yield items
