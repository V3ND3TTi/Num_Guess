# Number Guessing Game
import random

def get_guess() -> int:
    while True:
        try:
            return int(input('Enter your guess: '))
        except ValueError:
            print('Please try again. Enter a number this time.')

def play_game():
    secret_num: int = random.randint(1, 100)
    max_guesses: int = 6

    print('You will have 6 trys to guess the secret number between 1 and 100.')

    while max_guesses > 0:
        user_guess: int = get_guess()

        if user_guess == secret_num:
            print('Congrats! You guessed the secret number!')
            break
        elif user_guess > secret_num:
            print('Too High!')
            max_guesses -= 1
        else:
            print('Too Low!')
            max_guesses -= 1

    if max_guesses == 0:
        print('Sorry, you ran out of guesses. Better luck next time!')

play_game()