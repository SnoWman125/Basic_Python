# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
data = []
with open('nginx_logs.txt', 'r') as logs:
        for line in logs:
            ip = line[0:line.find(' ')]
            req_type = line[line.find('"')+1:line.find('"')+4]
            res = line[line.find('GET', line.find('/'))+4:line.find('HTTP')-1]
            data.append((ip, req_type, res))
print(data)
#Найти IP адрес спамера и количество отправленных им запросов по данным файла
#логов из предыдущего задания
count_dict = {}
for i in data:
    if i[0] in count_dict:d
            count_dict[i[0]] += 1
    else:
        count_dict[i[0]] = 1
max_count = max(count_dict.values())
spammer = {k:v for k,v in count_dict.items() if v == max_count}
print(spammer)


