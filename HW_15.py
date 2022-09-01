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
try:
    response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
except Exception as e:
    print(e)

# print(response.status_code)
# print(response.headers)
else:
    if content := response.headers.get('Content-Type'):
      if content == 'application/json':
          with open('example.html', 'wt') as file:
            file.write(response.text)

response.ok
response.raise_for_status()

try:
    res_json = response.json()
except:
    print('Exception')

pprint.pprint(res_json)





