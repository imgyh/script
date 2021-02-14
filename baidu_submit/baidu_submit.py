#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re


baidu_submit_url = r'http://data.zz.baidu.com/urls?site=https://www.imgyh.com&token=bRAFATrCdbjNx0Xi'

baidusitemap_url = r"https://www.imgyh.com/baidusitemap.xml"

def get_urls():
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
        }

    res=requests.get(baidusitemap_url,headers)
    baidusitemap=res.content.decode("utf-8")
    
    urls=re.findall("<loc>(.*?)</loc>",baidusitemap)
    
    return urls

def post_url(urls):
    data="\n".join(urls)
    print(data)
    res=requests.post(baidu_submit_url,data)
    print(res.text)


if __name__ == '__main__':
    urls=get_urls()
    post_url(urls)