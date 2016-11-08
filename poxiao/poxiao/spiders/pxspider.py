#-*- coding:utf-8 -*-

'''
Created on 2016年11月4日

@author: cy002
'''
import scrapy
from scrapy import log
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
import re
import time
import urllib
import urllib2
import sys  
from poxiao.items import PoxiaoItem
reload(sys)  
sys.setdefaultencoding('utf8')


class pxSpider(CrawlSpider):
    name = 'poxiao'
    
    # allowed_domains = ['poxiao.com', 'baidu.com']
    start_urls = ['http://www.poxiao.com']
    
    def __init__(self, isall=''):
        CrawlSpider.__init__(self)
    
    def parse(self, response):
        hxs = Selector(response)
        
        rootDivs = hxs.xpath('//div[@id="indextopleft"]')
        if rootDivs :
            div = rootDivs[0]
            
            lis = div.xpath('.//div/ul/li')
            
            for li in lis:
                item = PoxiaoItem()
                
                ## 名称
                namestr = li.xpath('.//a[2]/text()').extract()[0]
                start = namestr.find("《") + 1
                end = namestr.find("》")
                name = namestr[start:end]
                item['name'] = name
                
                ## 详情地址
                href = li.xpath('.//a[2]/@href').extract()[0]
                item['url'] = 'http://www.poxiao.com/' + href
                
                ## 更新日期
                datestr = li.xpath('.//span[@class="date"]/text()').extract()
                update = ''
                if datestr :
                    update = datestr[0]
                    
                    if update == '':
                        datestr = li.xpath('.//span[@class="date"]/font/text()').extract()
                        if datestr :
                            update = datestr[0]
                item['update_time'] = update
                
                if item['name'] and item['url'] :
                    yield Request(url=item['url'], meta={'item':item}, callback=self.parse_details, errback=self.get_err)
                else :
                    log.msg('名称或者详情地址为空：' + item['name'] + ', ' + item['url'])

                
    def get_err(self, fail):
        print '=' * 30
        
        print str(fail.printDetailedTraceback())
        print fail.value
        
                        
    def parse_details(self, response):
        res = Selector(response)
        item = response.meta['item']
        
        divs = res.xpath('//div[@id="film"]')
        if divs :
            div = divs[0]
            
            ## 海报
            imgs = div.xpath('.//div[@class="detail_pic"]/span/img/@src').extract()
            if imgs :
                item['poster'] = imgs[0]
            
            infos = div.xpath('.//div[@class="detail_intro"]/table/tr')
            
            if infos :
                ## 导演
                directors = infos[0].xpath('.//td[2]/a/@title').extract()
                director = ''
                for d in directors:
                    director = director + ',' + d
                if len(director) > 1:
                    director = director[1:]
                item['directors'] = director
                
                ## 演员
                actors = infos[1].xpath('.//td[2]/a/@title').extract()
                actor = ''
                if actors :
                    for a in actors:
                        actor += ',' + a
                if len(actor) > 1:
                    actor = actor[1:]
                item['actors'] = actor
                    
                ## 国家/地区
                areas = infos[2].xpath('.//td[2]/text()').extract()
                print '==' + areas[0]
                area = ''
                if areas :
                    for a in areas :
                        area += ',' + a
                if len(area) > 1:
                    area = area[1:]
                item['areas'] = area

                ## 类型
                types = infos[3].xpath('.//td[2]/text()').extract()
                typ = ''
                if types :
                    for t in types:
                        typ += ',' + t
                if len(typ) > 1:
                    typ = typ[1:]
                item['types'] = typ
                
                ## 年代
                years = infos[4].xpath('.//td[2]/text()').extract()
                year = ''
                if years :
                    for y in years:
                        year += ',' + y
                if len(year) > 1:
                    year = year[1:]
                item['year'] = year
        
        ## 描述
        desc = ''
        descrs = res.xpath('//div[@class="filmcontents"]/p[2]/text()').extract()
        if descrs :
            desc = descrs[0].rstrip()
            
        if desc == '':
            descrs = res.xpath('//div[@class="filmcontents"]/p/text()').extract()
            if descrs :
                desc = descrs[0]
        item['desc'] = desc
        
        ## 下载地址
        downs = res.xpath('//div[@class="resourcesmain"]/tables/tbody/tr/td/a/@thunderhref').extract()
        down = ''
        if downs :
            item['download_url'] = downs[0]
            down = downs[0]
        item['download_url'] = down
        
        yield item
            
            

            
            
                
        
            


            
    
            
        
        
        
        
        
        
                
                
                
                
                
                

        
            
            
            

          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        pass
