import sys
import random

def main(*args, **kargs):
    highest_num = args[0] if args[0] is not None else 20

    turns = 0

    player = raw_input("Name: ")

    number = random.randint(1, highest_num)

    print('Well, ' + player + ', I am thinking of a number between 1 and ' + str(highest_num) + '.')

    max_turns = args[1] if args[1] is not None else 6

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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        highest = sys.argv[1]
        main(highest, 5)
    else:
        main(15, 5)