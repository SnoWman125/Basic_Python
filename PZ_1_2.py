lst = [number**3 for number in range(1, 1001) if number % 2 != 0]
final_sum = 0
for num in lst:
    sum = 0
    for i in str(num):
        sum += int(i)
    if sum % 7 == 0:
        final_sum += num
print('Итоговая сумма = {}'.format(final_sum))

# Добавление к каждому элементу списка 17 и получение суммы
final_sum = 0
for num in lst:
    num += 17
    sum = 0
    for i in str(num):
        sum += int(i)
    if sum % 7 == 0:
        final_sum += num
print('Итоговая сумма = {}'.format(final_sum))
