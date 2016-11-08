# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import *
from scrapy import log, signals
from scrapy.exceptions import DropItem
from scrapy.http import Request
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import datetime
import os
import sys
import time

  
class PoxiaoPipeline(object):
    def __init__(self):
        db_name = 'movies'
        user_name = 'root'
        user_pwd = 'root'
        db_host = '192.168.1.106'
        
        self.dbpool = adbapi.ConnectionPool("MySQLdb",
                                            db=db_name ,
                                            user=user_name,
                                            passwd=user_pwd,
                                            host=db_host,
                                            cursorclass=MySQLdb.cursors.DictCursor ,
                                            charset='utf8' ,
                                            use_unicode=False 
                                            )
    
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        
        return item  ;
    
    def _conditional_insert(self, tx, item):
        insert_sql = "INSERT INTO h_movies(name, url, poster, directors, actors, areas, types, \
        year, descr, download_url, update_time) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        r = tx.execute(insert_sql, (item['name'], item['url'], item['poster'], item['directors'],
                                    item['actors'], item['areas'], item['types'], item['year'], item['desc'], item['download_url'], item['update_time']))
        
        log.msg('添加电影: ' + item['name'] + ', 结果: ' + str(r))


    def handle_error(self, e):
        print str(e)
        log.err(str(e))





