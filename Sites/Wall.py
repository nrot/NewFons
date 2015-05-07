__author__ = 'nrot'

# -*- coding: utf-8 -*-

import random
import re
import requests
from lxml import html


def Wall(LogFile, Options):
    adr = 'http://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page='
    try:
        res = requests.get('http://wall.alphacoders.com/by_category.php?id=3')
        parsed_body = html.fromstring(res.text)
        page_info = parsed_body.xpath('//div[@class="hidden-xs visible-sm"]/ul[@class="pagination pagination"]/*')[9].getchildren()
        max_page = int(page_info[0].text)
        now_page = random.randint(1, max_page-1)
        adr += str(now_page)
        LogFile.write(text=adr)
        LogFile.write(text=adr)
    except:
        LogFile.write(aType='connect', text=adr, aTime=int(Options.TimeToSleep/60))
        return 'Error connect'

    res = requests.get(adr)
    parsed_body = html.fromstring(res.text)

    now_image = random.randint(0, 29)

    chose_img = parsed_body.xpath('//a[starts-with(@href, "big.php?i=")]')

    img_html = 'http://wall.alphacoders.com/' + str(chose_img[now_image].attrib['href'])

    LogFile.write(text=img_html)
    ReExp = re.compile('([0-9]+)$')
    img_name = ReExp.search(img_html)
    img_name = img_name.group() + '.jpg'
    
    res = requests.get(img_html)
    parsed_body = html.fromstring(res.text)

    pre_end_link = parsed_body.xpath('//span[@class="btn btn-success download-button"]')
    end_link = pre_end_link[0].attrib['data-href']

    LogFile.write(text=end_link)

    LogFile.write(text=img_name)

    return (requests.get(end_link, stream=True), img_name)
