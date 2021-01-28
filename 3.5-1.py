#В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
#Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
#Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
#Пример запроса к интересному числу:
#http://numbersapi.com/31/math?json=true
#Пример запроса к скучному числу:
#http://numbersapi.com/999/math?json=true
#Пример входного файла:
#31
#999
#1024
#502
﻿#Пример выходного файла:
#Interesting
#Boring
#Interesting
#Boring




import requests
#api_url = 'http://numbersapi.com'
#num = int(input())

#params = {
#    'number': num,
#    'type': 'math',
#    'json': 'true'
#}
#template = 'http://numbersapi.com/992,960,930,964,967,904,953,906,912,913,914,919,985,955,956/math?json=true'
with open('dataset_24476_3.txt','r') as f:
    for num in f.read().splitlines():
#    num = f.readline().rstrip();
        res = requests.get(f'http://numbersapi.com/{num}/math?json=true')
        data = res.json()
        if data["found"]: print('Interesting')
        else: print('Boring')
 #   print(res.text)

#template = 'Current temperature in {} is {}'
#print(template.format(city, data["main"]["temp"]))
