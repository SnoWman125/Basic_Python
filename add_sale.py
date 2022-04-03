import sys

price = sys.argv[1]
bakery = []
with open('bakery.csv', 'a', encoding='utf-8') as bakery:
        bakery.write(f'{price}\n')

