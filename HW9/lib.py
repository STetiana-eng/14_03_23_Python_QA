#Напишіть функцію, яка визначає сезон за датою. Функція отримує стрінг у форматі "[день].[місяць]"
#(наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з відповідним сезоном,
#до якого відноситься ця дата ("літо", "осінь", "зима", "весна")

def main():
    """Docstring function for determination of the season by date"""
    seasone = check_season()


def check_season():
  result = list(input("enter: "))
  if __name__== "__main__":
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


main()