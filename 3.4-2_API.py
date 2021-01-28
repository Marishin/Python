# В этой задаче вам необходимо воспользоваться API сайта https://developers.artsy.net/v2/start
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке

import requests
import json

client_id = 'e3203dbdfa06a8b85ef5'
client_secret = 'c3ef9086fe4690320d1637138d45681b'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
l = []
with open('dataset_24476_4.txt','r') as f:
    for num in f.read().splitlines():
        # инициируем запрос с заголовком
        r = requests.get(f"https://api.artsy.net/api/artists/{num}", headers=headers)
        r.encoding = 'utf-8'
        # разбираем ответ сервера
        j = json.loads(r.text)
        l = l + ([j["birthday"] + " " + j["sortable_name"]])
        l.sort()
    for i in l: print(i[5:])
