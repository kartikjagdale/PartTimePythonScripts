import urllib2
import re
from pprint import pprint
from bs4 import BeautifulSoup
#connect to a URL
url = 'http://www.codechef.com/problems/easy'
website = urllib2.urlopen(url).read()

soup = BeautifulSoup(website)
#read html code
#html = website.read()

links = soup.find_all('a')

#use re.findall to get all the links
#links = re.findall('"((/problems/).*?)"', html)

pprint(links)
