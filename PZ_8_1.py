import re

address = input('Input e`mail address: ')
mail = re.compile(r'([0-9_a-zA-Z0-9]*)@([a-z0-9]*.[a-z]*)')
if mail.match(address):
    data = mail.findall(address)
    login, domain = data[0]
    dict = {'username': login, 'domain': domain}
else:
    print('e`mail not valid')
print(dict)
