#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який
#свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Зауважте, що lst1 не є
#статичним і може формуватися динамічно від запуску до запуску.


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for list_elements in lst1:
    if isinstance(list_elements, str):
        lst2.append(list_elements)
print(lst2)
