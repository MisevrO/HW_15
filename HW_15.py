# Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ),
# отримайте курс валют
# і запишіть його в текстовий файл такому форматі (список):
#  "[дата створення запиту]"
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
#
#
# P.S.не забувайте про DRY, KISS, SRP та перевірки
import pprint

import requests
import datetime

try:
    response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
except Exception as e:
    print(e)

response.ok
response.raise_for_status()
try:
    res_json = response.json()
except:
    print('Exception')

with open("example.txt", 'a', encoding='utf-8') as file:
    file.write(str(datetime.datetime.now())+'\n')
    number = 1
    for i in res_json:
        file.write(f"{number} {i['txt']} {i['rate']}"+'\n')
        number += 1



