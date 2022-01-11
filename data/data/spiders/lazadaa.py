import scrapy
from ..items import DataItem
from selenium import webdriver
from scrapy.utils.project import get_project_settings


class LazadaaSpider(scrapy.Spider):
    name = 'lazadaa'
    def start_requests(self):
        settings= get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options= webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get('https://www.lazada.vn/ba-lo-nam/?q=balo&from=input')
        link_elements = driver.find_elements_by_xpath(
            '//*[@data-qa-locator="product-item"]//a[text()]'
        )
        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)
        driver.quit()

        

    def parse(self, response):
        p_name= response.xpath('//h1[@class="pdp-mod-product-badge-title"]//text()').get()
        brand = response.xpath('//a[@class="pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link"]/text()').get()
        s_name = response.xpath('//a[@class="pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name"]/text()').get()
        price = response.xpath('//span[@class="pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]//text()').get()
        positive_rating =  response.xpath('//div[@class="seller-info-value rating-positive "]/text()').get()
        p_fee = response.xpath( '//div[@class="delivery-option-item__shipping-fee no-subtitle"]/text()').get()
        
       
        item= DataItem()
        item['p_name']= p_name
        item['brand']= brand
        item['s_name']= s_name
        item['price']=price
        item['positive_rating']=positive_rating
        item['p_fee'] = p_fee
        yield item
