num = int(input('Введите N'))
#Генератор нечётных чисел от 1 до n (включительно), с использованием ключевого слова yield
def gen(number):
    for i in range(1, number+1, 2):
        yield i
gen_1 = gen(num)
print(*gen_1, sep=' ')

#Генератор нечётных чисел от 1 до n (включительно), с использованием ключевого слова yield
gen_2 = (e for e in range(1, num+1, 2))
print(*gen_2, sep=' ')
