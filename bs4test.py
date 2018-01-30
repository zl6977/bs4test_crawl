#coding:utf-8

from bs4 import BeautifulSoup
import urllib.request
import os,sys,time

#url="http://bj.cityhouse.cn/" # 要爬取的网络地址
cities=['北京','上海','广州','九江','南京','无锡(含江阴)','镇江','安庆','钦州','梧州','柳州']
urls=[
'http://bj.cityhouse.cn/lease/',
'http://sh.cityhouse.cn/lease/',
'http://gz.cityhouse.cn/lease/',
'http://jj.cityhouse.cn/lease/',
'http://nj.cityhouse.cn/lease/',
'http://wx.cityhouse.cn/lease/',
'http://zhenjiang.cityhouse.cn/lease/',
'http://aq.cityhouse.cn/lease/',
'http://qinzhou.cityhouse.cn/lease/',
'http://wuzhou.cityhouse.cn/lease/',
'http://liuzhou.cityhouse.cn/lease/']
cdate=time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
f = open(sys.path[0]+'/'+cdate+'.txt','w')
f.write('城市'+'\t'+'租金(元/㎡)'+'\n') 
    
for index in range(len(urls)):
	htmlTmp=urllib.request.urlopen(urls[index]).read()
	soup = BeautifulSoup(htmlTmp, 'html.parser')
	print(cities[index],soupTmp[0].string)
f.close()  
