__author__ = 'nrot'

# -*- coding: utf-8 -*-

import random

import requests
import lxml


def Zastavki(LogFile, Options):

    adr = 'http://www.zastavki.com/rus/Anime/'

    try:
        res = requests.get('http://www.zastavki.com/rus/Anime/')
        parsed_body = lxml.html.fromstring(res.text)
        page_info = parsed_body.xpath('//td[@id="at-all-info"]/*')
        max_page = int(page_info[1].text)
        now_page = random.randint(1, max_page-1)
        adr = adr + str(now_page) + '/'
        LogFile.write(text=adr)
    except:
        LogFile.write(aType='connect', text=adr, aTime=int(Options.TimeToSleep/60))
        return 'Error connect'

    res = requests.get(adr)
    parsed_body = lxml.html.fromstring(res.text)

    now_image = random.randint(0, 10)

    chose_img = parsed_body.xpath('//a[@class="img-wrap"]')

    LogFile.write(text=chose_img[now_image].attrib['href'])

    img_html = 'http://www.zastavki.com' + chose_img[now_image].attrib['href']
    res = requests.get(img_html)
    parsed_body = lxml.html.fromstring(res.text)

    pre_end_link = parsed_body.xpath('//a[@class="original-link"]')
    end_link = 'http://www.zastavki.com/' + pre_end_link[0].attrib['href']
    cache = pre_end_link[0].attrib['href']
    LogFile.write(text=end_link)

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
