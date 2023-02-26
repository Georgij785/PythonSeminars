"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "принтер",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json

Dict = {"orders": []}


def write_order_js(a, b, c, d, e, dict):
    dict["orders"].append({"item": a,
                           "quantity": b,
                           "price": c,
                           "buyer": d,
                           "date": e})

    with open("orders.json", "w") as ad:
        ad.write(json.dumps(Dict, sort_keys=True, indent=4))
        ad.write(json.dumps(","))


write_order_js("scaner", 21, 12, "vasa", "2.02.12", Dict)
write_order_js(12, 21, 12, 2, 2, Dict)
write_order_js(12, 21, 12, 2, 2, Dict)
write_order_js(12, 21, 12, 2, 2, Dict)
write_order_js(12, 21, 12, 2, 2, Dict)
