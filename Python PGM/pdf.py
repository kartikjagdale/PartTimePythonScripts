#Data mining

#import os
#from bs4 import BeautifulSoup
import urllib
#import requests

url = 'http://guidetodatamining.com/guide/ch'
print 'downloading'
for i in range(4,9):
        urllib.urlretrieve(url+str(i)+'/DataMining-ch'+str(i)+'.pdf','C:\Users\Hebi\Desktop\Data_mining\DataMining-ch'+str(i)+'.pdf')
        print 'dowloaded',i

print '\n Download Finished\nHappy Coding!!!'
