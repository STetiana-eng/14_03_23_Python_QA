#Створити конструкції try-except для арифметичної операції, роботи з колекціями.

try:
    my_list = [40,60,70,"a"]
    for number in my_list:
        result = number/10
        print(result)
except Exception:
 print( "This action is incorrect ")



#second case

x = 6.0

try:
    for y in range(1,10000):
        new_number = x**y
except ArithmeticError as e:
    print(f"{e}")
finally:
    print("If you have some mistakes try to change number")




