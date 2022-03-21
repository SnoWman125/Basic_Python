import requests
from datetime import datetime

def currency_rates(val):
    dict = {}
    lst_chars = []
    lst_val = []
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    [lst_chars.append(i.split("</CharCode>")[0]) for i in r.split('<CharCode>')[1:]]
    [lst_val.append(i.split("</Value>")[0]) for i in r.split('<Value>')[1:]]
    for i in lst_chars:
        dict[i] = lst_val[lst_chars.index(i)]
    d = r.find('Date')
    date = datetime.strptime(r[d+6:d+16], "%d.%m.%Y")
    print('Дата:', date.date())
    if val in dict:
        print(f'{val} = {dict[val]}')
    else:
        print('Код валюты некорректен')
    
if __name__ == '__main__':
    char = input('Введите код валюты')
    currency_rates(char)