# -*- coding: utf-8 -*- 

from datetime import date,datetime
import time



dt = datetime.now()
print time.localtime()[2]

print time.localtime()[3]
print time.localtime()

print "---------------------------------------"

print dt.strftime('%H:%M')  
print 'date.max:', date.max
print 'date.min:', date.min
print 'date.today():', date.today()
print 'date.fromtimestamp():', date.fromtimestamp(time.time())

print "---------------------------------------"

print time.strftime("%Y-%m-%d %X", time.localtime())


# 08/22/2015 11:00:00 AM
t1 = time.strptime('08/22/2015 11:00:00 PM', '%m/%d/%Y %I:%M:%S %p')

print t1[0:3]
t = time.strptime("2009 - 08 - 08", "%Y - %m - %d")
y,m,d = t[0:3]
print datetime(y,m,d)


# # ---- 结果 ----
# date.max: 9999-12-31
# date.min: 0001-01-01
# date.today(): 2010-04-06
# date.fromtimestamp(): 2010-04-06