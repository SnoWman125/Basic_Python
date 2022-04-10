# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import json

#Можно указать директорию
dir = os.getcwd()
count_dict = {}
num = [0, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
for i in range(len(num) - 1):
    count = 0
    ext = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if num[i] < os.stat(os.path.join(root, file)).st_size < num[i + 1]:
                count += 1
                f_ext = file.rsplit('.')[-1].lower()
                if f_ext not in ext:
                    ext.append(f_ext)
            count_dict[num[i + 1]] = count, ext
print(count_dict)
save_dir = f'{os.getcwd()}_{os.stat(os.getcwd()).st_size}'
with open(f'{save_dir.rsplit("/")[-1]}.json', 'w') as f:
    json.dump(count_dict, f)


