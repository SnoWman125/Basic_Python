duration = int(input('Введите количество секунд'))
days = duration // 86400
duration %= 86400
hours = duration // 3600
duration %= 3600
minutes = duration // 60
seconds = duration % 60

if days:
    print('{} дн {} час {} мин {} сек'.format(days, hours, minutes, seconds))
elif hours:
    print('{} час {} мин {} сек'.format(hours, minutes, seconds))
elif minutes:
    print('{} мин {} сек'.format(minutes, seconds))
else:
    print('{} сек'.format(seconds))


