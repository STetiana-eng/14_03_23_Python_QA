#Створити файл та записати в нього рядок.
#Прочитати створений файл та вивести на консоль вміст файлу
#Додати ще один рядок до створеного файлу.
#Прочитати всі рядки з файлу та вивести на консоль.
#Записати у файл все що користувач введе з консолі. (Якщо хочете більш ніж один рядок спробуйте використати
#while True і перевірку на введений рядок, типу якщо exit тоді це кінець.)
#Завдання 1-4 прошу зробити міксовано щось через Context manager, а щось класично.

#

with open("My_new_file_1.txt", "w") as f:
 f.write("Hi,my name is Tanya\n")

f = open("My_new_file_1.txt","r")
print(f.read())
f.close

with  open("My_new_file_1.txt", "a") as f:
 f.write("It is my first try!")


f = open("My_new_file_1.txt", "r")
print(f.read())
f.close


lines = []
while True:
 line = input()
 if line != "":
  lines.append(line)
  break


with open("input_console_file.txt", "a") as f:
   f.writelines(lines)






