import random

def set_number():
    return input("Player 1, set the multi-digit number for Player 2 to guess: ")

def get_guess():
    return input("Player 2, enter your guess: ")

def give_hint(number, guess):
    hint = ""
    for i in range(len(number)):
        if guess[i] == number[i]:
            hint += guess[i]
        else:
            hint += "_"
    return hint

def play_mastermind():
    number = set_number()
    attempts = 0
    
    while True:
        guess = get_guess()
        attempts += 1
        if guess == number:
            print(f"Correct! Player 2 guessed the number in {attempts} attempts.")
            break
        else:
            print(f"Hint: {give_hint(number, guess)}")
    
    return attempts

# Player 1's turn to set the number
print("Player 1's turn:")
player1_attempts = play_mastermind()

# Player 2's turn to set the number
print("\nPlayer 2's turn:")
number = set_number()
attempts = 0

while True:
    guess = input("Player 1, enter your guess: ")
    attempts += 1
    if guess == number:
        print(f"Correct! Player 1 guessed the number in {attempts} attempts.")
        break
    else:
        print(f"Hint: {give_hint(number, guess)}")

if attempts < player1_attempts:
    print("Player 1 wins and is crowned Mastermind!")
else:
    print("Player 2 wins and is crowned Mastermind!")
