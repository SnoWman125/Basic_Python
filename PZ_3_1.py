def num_translate_adv(num):
    num_list = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if num.istitle():
        num_low = num.lower()
        return num_list.get(num_low, 'Некорректный ввод').capitalize()
    else:
        return num_list.get(num, 'Некорректный ввод')

number = input('Введите число прописью')
print(num_translate_adv(number))