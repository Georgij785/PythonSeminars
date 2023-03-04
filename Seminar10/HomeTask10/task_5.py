"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


ARGS_1 = ['ping',"youtube.com"]
YA_PING_1 = subprocess.Popen(ARGS_1, stdout=subprocess.PIPE)
for line_0 in YA_PING_1.stdout:
    result_1 = chardet.detect(line_0)
    line_1 = line_0.decode(result_1['encoding']).encode('utf-8')
    print(line_1.decode())