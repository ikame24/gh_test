#-*- coding:utf-8 -*-

'''
Created on 2016年11月4日

@author: cy002
'''

import re

def getName(content):
    name = ''
    
    # 将正则表达式编译成Pattern对象 
    pattern = re.compile(r'《(.+)》')
     
    # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None 
    # 这个例子中使用match()无法成功匹配 
    match = pattern.search(content) 
     
    if match: 
        # 使用Match获得分组信息 
        name = match.group(1)
        
    print 'content=%s, name=%s' % (content, name)
    return name  


