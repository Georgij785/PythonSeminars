"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

DICT_TO_YAML = {"1": [1, 2, 3],
                "2": 3,
                "3": {"1": "£",
                      "2": "🌖",
                      "3": "◯"}}

with open("file.yaml", "w") as f_n:
    yaml.dump(DICT_TO_YAML, f_n, default_flow_style=False)
with open('file.yaml') as f_n:
    F_N_CONTENT = yaml.load(f_n, Loader=yaml.FullLoader)
print(F_N_CONTENT)
