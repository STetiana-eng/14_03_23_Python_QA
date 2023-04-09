#Напишіть функцію, яка приймає два аргументи.
#Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
#Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
#В будь-якому іншому випадку - функція повертає кортеж з двох агрументів

def math_functon (arg1=None,arg2=None):
    result = arg1,arg2
    if type(arg1) is int and type(arg2) is int:
        result = (arg1*arg2)
    elif type(arg1) is str and type(arg2) is str:
         result = (arg1+arg2)
    return result

main_result = math_functon(arg1="dsd", arg2="gfgf")
print(main_result)







