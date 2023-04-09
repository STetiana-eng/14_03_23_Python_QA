
from random import randint

def set_number_attempts():
    while True:
        try:
            return int(input('Enter the number of attempts: '))
        except ValueError:
            print('Number please!')



def get_ai_number():
    number = randint(1, 10)
    print(f'AI: {number}')
    return number


def get_user_number():

    while True:
        try:
            return int(input('Enter the number (int): '))
        except ValueError:
            print('Number please!')


def check_numbers(ai_number, user_number):
    if ai_number-user_number > 10:
        print("Cold")
    if ai_number-user_number in range(5, 10):
        print("Worm")
    elif ai_number-user_number in range(1, 4):
        print("Hot")
    return ai_number == user_number


def check_attempts(count_of_attempts, number_attempts):
     result = count_of_attempts == number_attempts
     return result

def game_guess_number():
    print('Game begins!')
    number_attempts = set_number_attempts()
    ai_number = get_ai_number()
    count_of_attempts = 0




    while True:

        user_number = get_user_number()
        count_of_attempts += 1
        is_game_end = check_numbers(ai_number, user_number)
        game_is_over = check_attempts(number_attempts, count_of_attempts)

        if is_game_end or game_is_over:
            break
        print()


    print("Game over")


game_guess_number()

