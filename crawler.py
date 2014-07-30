#coding=utf-8
import urllib
import re

#TODO: Recursively crawling facebook users 
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#TODO: Loading Photo-Name-Location
def getInfo(html):
	#TODO: Load name
	#..

	#Photo is always in jpg format??
    '''reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)

    re.findall('([-\w]+\.(?:jpg|gif|png))', html):'''

    imglist = re.findall('src="(.+?)"', html)
    print imglist

    x = 0    
    for imgurl in imglist:
    	if ".jpg" in imgurl:
    		urllib.urlretrieve(imgurl,'%s.jpg' % x)
    		#break
    	if ".png" in imgurl:
    		urllib.urlretrieve(imgurl,'%s.png' % x)
    		#break
    	if ".gif" in imgurl:
    		urllib.urlretrieve(imgurl,'%s.gif' % x)
    		#break
        x+=1

    #TODO: Load location if possible
    #..

#html = getHtml("https://www.facebook.com/directory")
#print html
#print getInfo(html)

html = getHtml("https://www.facebook.com/juan.sotomarin.5/about?section=contact-info")
getInfo(html)
