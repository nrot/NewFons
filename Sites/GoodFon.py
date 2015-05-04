__author__ = 'nrot'

# -*- coding: utf-8 -*-

import random

import requests
from lxml import html


def GoodFon(LogFile, Options):

    try:
        res = requests.get('http://www.goodfon.ru/catalog/anime/index-1.html')
        parsed_body = html.fromstring(res.text)
        page_info = parsed_body.xpath('//div[@class="pageinfo"]/div')
        max_page = int(page_info[0].text)
        adr = 'http://www.goodfon.ru/catalog/anime/index-'
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
    end_link = pre_end_link[3].attrib['href']
    end_link = 'http://www.goodfon.ru' + end_link

    LogFile.write(text=end_link)

    res = requests.get(end_link)
    parsed_body = html.fromstring(res.text)
    img_link = parsed_body.xpath('//a[@id="im"]')
    cache = img_link[0].attrib['href']

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

    return (requests.get(cache, stream=True), img_name)
