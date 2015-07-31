# -*- coding: utf-8 -*- 

from datetime import date,datetime
import time


url = "http://aqicn.org/city/chengdu/en/"

print(url[22:len(url)-4])


dt = datetime.now()

print dt.strftime('%H:%M')  
print 'date.max:', date.max
print 'date.min:', date.min
print 'date.today():', date.today()
print 'date.fromtimestamp():', date.fromtimestamp(time.time())

# # ---- 结果 ----
# date.max: 9999-12-31
# date.min: 0001-01-01
# date.today(): 2010-04-06
# date.fromtimestamp(): 2010-04-06