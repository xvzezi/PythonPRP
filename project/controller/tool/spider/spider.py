# -*- coding: utf-8 -*-
import requests
import urllib
import urllib2
from bs4 import BeautifulSoup
from PIL import Image
#import pytesseract

def spider(user,password):

    #获取信息
    res = urllib.urlopen("http://i.jwc.sjtu.edu.cn/JALogin_G.aspx")
    soup = BeautifulSoup(res,"html.parser")
    hidden = soup.find(attrs = {"id":"form-input"})
    sid = (hidden.find(attrs = {"name":"sid"})).attrs[u'value']
    returl = (hidden.find(attrs = {"name":"returl"})).attrs[u'value']
    se = (hidden.find(attrs = {"name":"se"})).attrs[u'value']
    v = (hidden.find(attrs = {"name":"v"})).attrs[u'value']
    img = 'https://jaccount.sjtu.edu.cn/jaccount/'+(hidden.img).attrs[u'src']
    request = urllib2.Request('https://jaccount.sjtu.edu.cn/jaccount/captcha?15317457941930.261783271618375')
    png = requests.get('https://jaccount.sjtu.edu.cn/jaccount/captcha?15317457941930.261783271618375')
    response = urllib2.urlopen(request)
    with open('D:\\a.png','wb') as f:
        f.write(png.content)

    image = Image.open('D:/a.png')
    captcha = pytesseract.image_to_string(image)

    #登录界面
    url = "http://i.jwc.sjtu.edu.cn/JALogin_G.aspx"
    header = {"Accept":"text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN",
    "Cache-Control":"max-age=0",
    "Connection":"Keep-Alive",
    "Content-Length":"220",
    "Content-Type":"application/x-www-form-urlencoded",
    #"Cookie":"JSESSIONID=FE1F46BB2051DCA4628CF9D050EEA2A6.jaccount106; JAVisitedSites=CB/cTmE14KsWK4mRMpA940Zwum9yBLCphyZ9laKtM4YGz4sdBXa6Ga4=; _gid=GA1.3.1280142806.1531721174; _ga=GA1.3.1527640857.1531447335; JACCOUNT=jaccount.jaccount106",
    "Host":"jaccount.sjtu.edu.cn",
    "Referer":"https://jaccount.sjtu.edu.cn/jaccount/jalogin?sid=%s&returl=%s&se=%s&v=%s"%(sid,returl,se,v),
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    }
    body = {"captcha":captcha,"pass":password,"returl":returl,"se":se,"sid":sid,"user":user,"v":v }
    r = requests.post(url,data = body,headers = header,allow_redirects=False)
    aspid = r.headers["Set-Cookie"]
    print r.status_code
    url = "http://i.jwc.sjtu.edu.cn/Face/SJTUJW/Main1.aspx"
    header = {"Accept":"text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
    "Accept-Encoding":"gzip,deflate,br",
    "Accept-Language":"zh-CN",
    "Cache-Control":"max-age=0",
    "Connection":"Keep-Alive",
    "Referer":"https://jaccount.sjtu.edu.cn/jaccount/jalogin?sid=%s&returl=%s&se=%s&v=%s"%(sid,returl,se,v),
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Cookie" : aspid
    }
    r = requests.get(url=url,headers=header)
    print r.status_code
    print r.text
