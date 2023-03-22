#Сформуйте стрінг, в якому міститься інформація про певне слово. 
#"Word [тут слово] has [тут довжина слова, отримайте з самого слова] letters",
#наприклад "Word 'Python' has 6 letters".
#Для отримання слова для аналізу скористайтеся константою або функцією  input().

my_input = input("")
my_string = "Word \"{} \" has {} letters".format(my_input, len(my_input))
print(my_string)

# Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести
# свій вік (можно використати константу або функцію input(), на екран має бути 
# виведено лише одне повідомлення, також подумайте над варіантами, коли введені невірні дані).
# якщо користувачу менше 7 - вивести повідомлення "Де твої батьки?"
# якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
# якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
# у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"


age = input("Будь-ласка введіть свій вік:")
if not age.isdigit():
 print("Тільки цифри")
elif age.find("7") > -1:
 print("Вам сьогодні пощастить!")
elif int(age) > 0 and int(age) < 7:
 print("Де твої батьки?")
elif int(age)  >= 7 and int(age) < 16:
 print("Це фільм для дорослих!")
elif int(age) >= 65:
 print("Покажіть пенсійне посвідчення!")
else:
 print("А білетів вже немає!")