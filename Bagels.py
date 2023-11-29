# Write your code here :-)
import random
NUM_DIGITS = 3 #this should be 1 to 9 as the digits in the list below are upto 9 only. if you want to increase length add more numbers.
MAX_GUESSES = 10 #this number can be anything. it just limits the no of guesses.

def main():
    print('''Bagels, a deductive logic game.
    Actual game by Al Sweigart. implemented here by Shanmuk.
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.

    For example, if secret number was 729 and your guess was 928, the clues would be
    Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secretNum = getSecretNum()#if we replace this with a number it leads to a type error saying int is non subscriptable.
        print(' I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1#its absence leads to unbound local error. variable being referenced before assignment.
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess)!=NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):

    if guess == secretNum:
        return 'You got it'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:

            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

#If the program is run (instead of imported), run the game:

if __name__ == '__main__':
    main()

