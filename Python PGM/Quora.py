#Downlaod All answers for a question from Quora to pdf

import os
import requests
import json
import urllib2

url = raw_input("Please enter url:")

page = urllib2.urlopen(url).read()
with open('page_content.htm','w+') as fid:
    fid.write(page)
print type(page)


