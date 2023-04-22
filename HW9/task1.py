# Напишіть декоратор, який визначає час виконання функції. Заміряйте час іиконання функцій з попереднього ДЗ

import time

def my_decorator(func):

    def _wrapper(*args, **kwargs):
        start =time.time()
        res = main(*args, **kwargs)
        end = time.time() - start
        print(f'Process time {end}')
        return res

    return _wrapper



def main():
    """Docstring function for determination of the season by date"""
    season = check_season()



def check_season():
 result = list(input("enter: "))
 if result[-1] == "1" or result[-1] == "2" or result[-1] == "12":
    print("winter")
 elif result[-1] == "3" or result[-1] == "4" or result[-1] == "5":
    print("spring")
 elif result[-1] == "6"or result[-1] == "7" or result[-1] == "8":
    print("summer")
 elif result[-1] == "9" or result[-1] == "10" or result[-1] == "11":
    print("autumn")
 else:
    print("incorrect date")
 return


wrapped_function = my_decorator(main)
wrapped_function()


