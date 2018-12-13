from urllib import request,parse

#1.
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/60.0.3112.90 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_java?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=',
}
data= {
    'first': False,
    'pn':1,
    'kd': 'java',
}

#2.
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('UTF-8'),method='POST')
response = request.urlopen(req)
r = response.read().decode('UTF-8')
