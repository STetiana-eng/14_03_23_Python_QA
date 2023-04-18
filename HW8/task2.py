#Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи і строковий,
#який відповідає за операцію між ними (+ - / *). Функція повинна повертати значення відповідної операції
#(додавання, віднімання, ділення, множення), інші операції не допускаються.
#Якщо функція оримала невірний тип данних для операції (не числа) або неприпустимий (невідомий)
#тип операції вона повинна повернути None і вивести повідомлення "Невірний тип даних" або "Операція не підтримується"
#відповідно.




def main():
    firstNumber = getNumber1()
    operator = getOperator()
    secondNumber = getNumber2()
    operatorIsValid = validateOperator(operator)
    if firstNumber is None:
        print("incorrect data for first number!")
        return
    if secondNumber is None:
        print("Incorrect data for second number")
        return
    if operatorIsValid is False:
        print("Incorrect data for operator")
        return
    result = check_first_number_type(firstNumber,secondNumber,operator)





def getNumber1():
    """Docstring function get first number"""
    try:
        return int(input("Enter first number: "))
    except ValueError:
        return



def getNumber2():
    try:
        return int(input("Enter second number: "))
    except ValueError:
        return



def getOperator():
    return input("Enter operator: ")



def validateOperator(operator):
        return operator in ('+', '-', '*', '/')


def  check_first_number_type(firstNumber,secondNumber,operator):
           if operator == "+":
             print(firstNumber + secondNumber)
           elif operator  == "-":
             print(firstNumber-secondNumber)
           elif operator == "/":
             print(firstNumber/secondNumber)
           elif operator == "*":
             print(firstNumber*secondNumber)
           else:
             print("Incorrect action")



main()
