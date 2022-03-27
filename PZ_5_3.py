tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
# Количество генерируемых кортежей не должно быть больше длины списка 'tutors'
# Eсли в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None)

if len(tutors)>len(klasses):
    for i in range(len(klasses)+1, len(tutors)+1,1):
        klasses.append(None)
    gen_2 = ((tutors[i], klasses[i]) for i in range(len(tutors)))
    print(gen_2)
    print(*gen_2)
else:
    print('Список "klasses" больше списка "tutors"')