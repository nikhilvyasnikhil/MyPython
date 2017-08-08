# -*- coding: utf-8 -*-

import bs4
#from lxml import html
from bs4 import BeautifulSoup as soup
from urllib import urlopen as urlreq
# program on web scrapping - testing
#Nikihl Vyas
print('om namah shivay')
page = urlreq("http://www.amazon.in/TVs/b/ref=nav_shopall_sbc_tvelec_television?ie=UTF8&node=1389396031")
pageread  = page.read()
page.close()    
page_soup = soup(pageread,"html.parser")
containers = page_soup.findAll("div",{"class":"acswidget acswidget-carousel celwidget a-spacing-base acswidget-carousel--shoveler acswidget-carousel--default"})
container = containers[0]
for container in containers:
    brand = container.div.div.div.div.ol.li.div.a["title"]
    print brand