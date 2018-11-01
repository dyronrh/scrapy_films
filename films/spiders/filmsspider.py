# -*- coding: utf-8 -*-
import scrapy 
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

class FilmsspiderSpider(scrapy.Spider):
    name = 'filmsspider'
    allowed_domains = ['www.afi.com','catalog.afi.com']
    start_urls = ['http://www.afi.com/100Years/movies10.aspx']

    def parse(self, response):
    	catalog_url = "http://catalog.afi.com/Catalog/moviedetails/"
    	films = response.xpath('//*[@id="subcontent"]/div/div/div/div/a/@href').extract()
    	for film in films:
    		film = film.replace('http://www.afi.com/members/catalog/DetailView.aspx?s=&Movie=', catalog_url)
    		absolute_url = response.urljoin(film)
    		print("Bsolute: "+absolute_url)
    		yield Request(absolute_url, callback=self.parse_film)
   

    def parse_film(self, response):
    	title = response.xpath('//*[@id="headerBackground"]/div/div/h1/span/text()').extract_first()
    	year  = response.xpath('//*[@id="headerBackground"]/div/div/h1/span/a/text()').extract_first()
    	synopsis =  response.xpath('//*[@id="limsummary"]/div/p/text()').extract_first()

    	yield ({'title':title,
    		    'year': year,
    		    'synopsis': synopsis})

