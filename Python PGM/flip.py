import urllib2
import re

a = 0
r = open("flipkart_price_data.txt","w+")
lst = r.readlines()
if(len(lst)!=0):
	a = lst[len(lst)-1]
r.close()
url = raw_input("Enter URL : ")
response = urllib2.urlopen(url)
web_page = response.read()
pattern = "(\<span class\=\"fk-font-verybig pprice vmiddle fk-bold\"\>).([^\n]*)"
m = re.search(pattern, web_page)
text = m.group(0)
if(text == None):
	print "Error"
	exit()
pattern = '(Rs\.).([0-9]+\.?[0-9]*)'
amount = re.search(pattern, text)
if(amount == None):
	print "Error"
	exit()
amt = amount.group(0)
#if(amt < a):
#Do something
#print(amt)
g = open("flipkart_price_data.txt","a")
g.write(amt+"\n")
g.close()
