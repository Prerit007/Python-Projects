import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    lives = 4
    print("You have 4 lives")
    while guess != random_number:
        guess = int(input(f"Guess Number between 1 and {x}:"))
        if guess < random_number:
            print("Sorry Wrong Guess. Too Low")
            lives = lives - 1
            print('You have ' + str(lives) + ' remaining')
        elif guess > random_number:
            print("Sorry Wrong Guess. Too High")
            lives = lives - 1
            print('You have ' + str(lives) + ' remaining')

    if lives == 0:
        print('Game Over')


    print(f"Correct Guess!! You guessed {random_number}")



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else :
            guess = low
        feedback = input(f"If {guess}  too high (H), too low (L), Correct (C) ??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print("Ok! The computer guessed, {guess}, correctly")

guess(10)
