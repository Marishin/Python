#Вам дано описание наследования классов в формате JSON.
#Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#Пример:
#[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.
#Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
#<имя класса> : <количество потомков>
#Выводить классы следует в лексикографическом порядке.

import json
data = [{"name": "DH", "parents": ["D", "BF", "DE", "AE"]}, {"name": "D", "parents": ["AE"]}, {"name": "B", "parents": []}, {"name": "AE", "parents": ["F"]}, {"name": "BG", "parents": ["H", "CH"]}, {"name": "H", "parents": []}, {"name": "E", "parents": ["CG", "B"]}, {"name": "BH", "parents": ["CG"]}, {"name": "CE", "parents": []}, {"name": "CH", "parents": ["E"]}, {"name": "C", "parents": ["CE"]}, {"name": "A", "parents": []}, {"name": "DE", "parents": ["BH"]}, {"name": "F", "parents": []}, {"name": "CG", "parents": ["C", "G"]}, {"name": "G", "parents": []}, {"name": "BF", "parents": ["F"]}]
data_json = json.dumps(data, indent=4)
data_again = json.loads(data_json)
P_CH = {}
for i in data_again:
    P_CH[i.get("name")] = []
for i in data_again:
    for j in i.get("parents"):
        P_CH[j].append(i.get("name"))
def rec(k, v):
    for i in v:
        s = P_CH.get(i)
        if s != []:
            P_CH[k] = list(set(P_CH.get(k) + s))
            rec(k, s)
for k, v in P_CH.items():
    rec(k, v)
for k, v in sorted(P_CH.items()):
    print(k, ":", len(v)+1)
