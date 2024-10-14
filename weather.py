# -*- coding: utf-8 -*-
# @Author   : Vicent
# @Date     : 2024/10/14
# @Software : PyCharm
# @version  ：Python 3.9
# @File     : weather.py


import requests
from urllib.parse import quote
import re
from bs4 import BeautifulSoup


class WeatherReport:
    def __init__(self, city):
        self.quote_city = quote(city, encoding='utf-8')
        self.result_info = []

    def get_city_code(self):
        r = requests.get('http://toy1.weather.com.cn/search?cityname=%s' % self.quote_city).text
        try:
            response = eval(r)[0].get('ref')
            print(response)
            print(re.search('[0-9]+', response).group())
            return re.search('[0-9]+', response).group()
        except:
            return None

    def get_weather(self, code):
        r = requests.get('https://www.weather.com.cn/weather/%s.shtml' % code)
        r.encoding = 'utf-8'
        bs4 = BeautifulSoup(r.text, 'lxml')

        days = bs4.find('div', {'id': '7d'}).find('ul', {"class": "t clearfix"}).findAll('li')
        for day in days:
            date = day.h1.text
            weather = day.find('p', {"class": "wea"}).text
            tmp = day.find('p', {"class": 'tem'}).text.strip()
            self.result_info.append("%s: %s %s" %(date,weather, tmp))
        return self.result_info
