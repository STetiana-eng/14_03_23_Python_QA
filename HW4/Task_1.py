#Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
#Напишіть код, який видалить (не створить новий, а саме видалить!) з нього всі числа, які менше 21 і більше 74.


set1 = set([11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44])
list2 = list(set1)
for number in set1:
    if number > 74:
        list2.remove(number)
for number in set1:
    if number < 21:
        list2.remove(number)
print(list2)


