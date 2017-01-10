# -*- coding: utf-8 -*-

import httplib

conn = httplib.HTTPConnection("127.0.0.1")
conn.request("GET", "/uploads/1.jpeg")
r1 = conn.getresponse()

test = 'OK' if r1.status == 200 else 'ERROR'
print ('uploads ' + str(r1.status) + ' ' + test)

data1 = r1.read()

conn.request("GET", "/img/1.jpeg")
r2 = conn.getresponse()

test = 'OK' if r2.status == 200 else 'ERROR'
print ('public ' + str(r2.status) + ' ' + test)

data2 = r2.read()

conn.request("GET", "/question/123")
r3 = conn.getresponse()

test = 'OK' if r3.status == 404 else 'ERROR'
print ('w/o extention ' + str(r3.status) + ' ' + test)

data3 = r3.read()

conn.close()
