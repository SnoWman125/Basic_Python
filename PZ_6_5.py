# Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта

import sys
users = []
hobby = []
u, h, u_h = sys.argv[1:]
with open(u, encoding='utf-8') as user:
    with open(h, encoding='utf-8') as hobbyes:
        [users.append(line.replace(',', ' ') and line.replace('\n', '')) for line in user]
        [hobby.append(line.replace('\n', ' ')) for line in hobbyes]
if len(users) < len(hobby):
    exit(1)
else:
    for i in range(len(hobby)+1, len(users)+1, 1):
        hobby.append(None)
with open(u_h, 'w') as file:
    for i in range(len(users)):
        file.writelines(f'{users[i]}: {hobby[i]}\n')
