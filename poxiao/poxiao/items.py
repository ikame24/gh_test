# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PoxiaoItem(Item):
    
    name = Field();
    
    alias = Field();
    
    url = Field();
    
    poster = Field();
    
    directors = Field();
    
    actors = Field();
    
    types = Field();
    
    areas = Field();
    
    year = Field();
    
    release_time = Field();
    
    duration = Field();
    
    score = Field();
    
    desc = Field();
    
    download_url = Field();
    
    update_time = Field();
    
    pass
