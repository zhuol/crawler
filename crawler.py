#coding=utf-8
import urllib, urllib2
import cookielib, socket
import cgi, re, os

from bs4 import BeautifulSoup

def require_dir(path):
    try:
        os.makedirs(path)
    except OSError, exc:
        if exc.errno != errno.EEXIST:
            raise

def get_request(url):
    socket.setdefaulttimeout(5)
    #可以加入参数  [无参数，使用get，以下这种方式，使用post]
    params = {"wd":"a","b":"2"}
    #可以加入请求头信息，以便识别
    i_headers = {"Cache-Control": "max-age=0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
                #"Referer": "https://www.facebook.com/directory/people/5",
                #"Accept-Encoding": "gzip,deflate,sdch",
                "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6",
                "Cookie": "anonymid=hya84jk0-rdyfh4; depovince=GW; jebecookies=4a123028-6161-442d-8dec-f3e05e38c597|||||; _r01_=1; JSESSIONID=abcivkSRHFSenbUTq-mEu; ick_login=d9dde21d-b94b-4413-a656-ae61d2bb9dfc; _de=FA2A130DEC639DF0C7130199644B203F8ED172744450A224; p=363249d77eefbc4758d31cc12e5306978; t=72748ad88171e87790168a59cac20eb88; societyguester=72748ad88171e87790168a59cac20eb88; id=221066188; xnsid=7302ad67; XNESSESSIONID=fc0a4e74551f; jebe_key=c18d7966-c20a-4dde-b422-bd9daf5e35a1%7C0c104c03d08f7c6ea4196aff1129018b%7C1406828212711%7C1%7C1406828258105; vip=1; loginfrom=null; feedType=221066188_hot"
                }
    #use post,have some params post to server,if not support ,will throw exception
    #req = urllib2.Request(url, data=urllib.urlencode(params), headers=i_headers)
    req = urllib2.Request(url, headers=i_headers)

    #创建request后，还可以进行其他添加,若是key重复，后者生效
    #request.add_header('Accept','application/json')
    #可以指定提交方式
    #request.get_method = lambda: 'PUT'
    try:
        page = urllib2.urlopen(req)
        '''_, params = cgi.parse_header(page.headers.get('Content-Type', ''))
        encoding = params.get('charset', 'utf-8')
        html = page.info()
        print len(html)'''
        html = page.read()
        #print html

        soup = BeautifulSoup(html)        
        imglist = [image["src"] for image in soup.findAll("img")]#, {"class" : "pf_headalbum"})]
        #imglist = soup.findAll('img', class_="profilePic img")
        '''if len(imglist)==0:
            imglist = imglistRe'''
        print len(imglist)
        #print imglist

        '''if len(imglist)>0:
            try:
                os.makedirs(path)
            except OSError, exc:
                if exc.errno != errno.EEXIST:
                    raise'''

        username = soup.find("h1", {"class" : "username lively-user"}).contents[0]
        print username

        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), username)
        require_dir(directory)

        x = 0    
        for imgurl in imglist:
            filename = os.path.join(directory, str(x))
            if ".jpg" in imgurl:
                urllib.urlretrieve(imgurl,'%s.jpg' % filename)
                x+=1
            if ".png" in imgurl:
                urllib.urlretrieve(imgurl,'%s.png' % filename)
                x+=1

        #like get
        #url_params = urllib.urlencode({"a":"1", "b":"2"})
        #final_url = url + "?" + url_params
        #print final_url
        #data = urllib2.urlopen(final_url).read()
        #print "Method:get ", len(data)
    except urllib2.HTTPError, e:
        print "Error Code:", e.code
    except urllib2.URLError, e:
        print "Error Reason:", e.reason

#TODO: Recursively crawling facebook users 
def getHtml(url):
    page = urllib2.urlopen(url)
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

    re.findall('([-\w]+\.(?:jpg|gif|png)$)', html):

    soup = BeautifulSoup(html_doc)
    page_images = [image["src"] for image in soup.findAll("img")]'''

    '''#Should only on <img>
    imglistRe = re.findall('src="(.+?)"', html)
    print imglistRe'''

    # Need login session...Damn
    soup = BeautifulSoup(html)
    imglist = [image["src"] for image in soup.findAll("img", class_="pf_headalbum")]
    #imglist = soup.findAll('img', class_="profilePic img")
    '''if len(imglist)==0:
        imglist = imglistRe'''
    print len(imglist)
    print imglist

    x = 0    
    for imgurl in imglist:
    	if ".jpg" in imgurl:
    		urllib.urlretrieve(imgurl,'%s.jpg' % x)
    		x+=1
    	if ".png" in imgurl:
    		urllib.urlretrieve(imgurl,'%s.png' % x)
            #x+=1

    #TODO: Load location if possible
    #..

#html = getHtml("https://www.facebook.com/directory")
#print html
#print getInfo(html)

##################
To be added, get para by argv[1]..
##################

s1 = "https://www.facebook.com/katrina.dunlop"
s2 = "http://www.renren.com/335829717/profile?ref=hotnewsfeed&sfet=701&fin=24&fid=25590484812&ff_id=335829717&platform=0&expose_time=1406826740"
s3 = "http://www.renren.com/224196932/profile"
s4 = "http://www.renren.com/486740329/profile?ref=hotnewsfeed&sfet=103&fin=4&fid=25589788121&ff_id=486740329&platform=0&expose_time=1406828503"
url = s4
get_request(url)
'''html = getHtml(url)
getInfo(html)'''
