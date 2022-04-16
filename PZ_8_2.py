import re
import requests

link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
logs = requests.get(link).text
#Проверка на одной строке
#address = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
str = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - (.[0-9]{,2}/\w+/[0-9]{,4}:(?:[0-9]{,2}:){2}[0-9]{2} .[0-9]{4}.) .(\w+) (.\w+.\w+) \w+.\d.\d. (\d+) (\d+)')
for i in str.findall(logs):
            ip_addr, date, method, source, code, resolve = i
            print(ip_addr, date, method, source, code, resolve)