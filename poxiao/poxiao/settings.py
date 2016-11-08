# Scrapy settings for poxiao project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'poxiao'

SPIDER_MODULES = ['poxiao.spiders']
NEWSPIDER_MODULE = 'poxiao.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'souhumovie (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['poxiao.pipelines.PoxiaoPipeline']

CONCURRENT_ITEMS = 32
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32

DEFAULT_REQUEST_HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                           'Accept-Encoding': 'gzip,deflate,sdch',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
                           }

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = 'D:\work_spaces\python_space\j2ee_workspace\poxiaos\poxiao\logs\px.log'
LOG_LEVEL='INFO'


#delag 250ms
DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 10

