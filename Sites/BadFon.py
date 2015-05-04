__author__ = 'nrot'

# -*- coding: utf-8 -*-

import random

import requests
from lxml import html


def BadFon(LogFile, Options):

    try:
        res = requests.get('http://www.badfon.ru/catalog/anime/index-1.html')
        parsed_body = html.fromstring(res.text)
        page_info = parsed_body.xpath('//div[@class="pageinfo"]/div')
        max_page = int(page_info[0].text)
        adr = 'http://www.badfon.ru/catalog/anime/index-'
        now_page = random.randint(1, max_page-1)
        adr = adr + str(now_page) + '.html'
        LogFile.write(text=adr)
    except:
        LogFile.write(aType='connect', text=adr, time=int(Options.TimeToSleep/60))
        return 'Error connect'

    res = requests.get(adr)
    parsed_body = html.fromstring(res.text)

    now_image = random.randint(0, 23)

    chose_img = parsed_body.xpath('//a[@itemprop="url"]')

    LogFile.write(text=chose_img[now_image].attrib['href'])

    img_html = chose_img[now_image].attrib['href']
    res = requests.get(img_html)
    parsed_body = html.fromstring(res.text)

    pre_end_link = parsed_body.xpath('//a[@target="_blank"]')
    end_link = pre_end_link[0].attrib['href']
    end_link = end_link

    LogFile.write(text=end_link)

    cache = end_link

    LogFile.write(text=cache)

    i = len(cache) - 1
    while cache[i] != '/':
        i -= 1
    i += 1
    img_name = ''
    while i <= len(cache)-1:
        img_name = img_name +cache[i]
        i += 1

    LogFile.write(text=img_name)

    return (requests.get(end_link, stream=True), img_name)
