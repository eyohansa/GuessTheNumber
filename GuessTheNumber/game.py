import random

turns = 0

player = raw_input("Name: ")

number = random.randint(1, 100)

print('Well, ' + player + ', I am thinking of a number between 1 and 100.')

while turns < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    turns += 1

    if guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        break

if guess == number:
    turns = str(turns)
    print('Well played, ' + player + '! You guessed my number in ' + turns + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope, the number I was thinking of was ' + number)
