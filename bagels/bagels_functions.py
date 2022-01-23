# the class for the bagle game
import sys
from random import shuffle


class Bagel:
    def __init__(self, NUM_DIGITS=3, GUESSES_LIST=10):
        self.number = []
        self.NUM_DIGITS = NUM_DIGITS  # number of digits
        self.GUESSES_LIST = GUESSES_LIST  # number of turns

    def get_number(self):
        # to get a shuffled number
        self.number =[]
        sorted_list = list([str(i) for i in range(0,10)])
        shuffle(sorted_list)
        for i in range(self.NUM_DIGITS):
            self.number.append(sorted_list[i])
        answer = "".join(self.number)
        return answer

    def game_display(self):  # displays the rules and describes the gameplay
        print("""\n\nBagels - A Deductive Logic Game.
        
The rules are simple and as follows:
You'll be given ten chances to guess the 3 digits correctly.
At any given time you have to enter three numbers and the clues you'll get are,
Clues:         What that means:\n
Pico           One digit is correct but in wrong position.
Fermi          One digit is correct and in right position.
Bagels         No digit is correct.\n
So I have thought up a number.
Enter your best guess.""")

    def replay_game(self):
        self.number = []
        replay = input("Want to play again?  y/n\n")
        if replay.lower() == 'y':
            Bagel.get_number(self)
            Bagel.game_display(self)
            Bagel.gameplay(self)
        elif replay.lower() == 'n':
            print("Thanks for playing. Please come again." )
            sys.exit()
        elif replay.lower() != 'y' or 'n':
            print("nah. You didn't enter the right words")
            Bagel.replay_game(self)

    def gameplay(self):
        answer = Bagel.get_number(self)
        answer_list = list(str(i) for i in answer)
        for i in range(1,self.GUESSES_LIST+2):
            if i == self.GUESSES_LIST+1:
                print(f"Alas, your turns are over! The answer is {answer}.")
                Bagel.replay_game(self)
            character = chr(9829)
            guess = ''
            while len(guess) != self.NUM_DIGITS or not guess.isdigit():
                print(f"\nPlease enter only {self.NUM_DIGITS} digit number.")
                guess = input(f"Guess #{i}\n>")
                if guess.lower() == 'q':
                    print("Do come again!")
                    sys.exit()
            guess_list = list(str(i) for i in guess)
            clues = []
            if guess == answer:
                print(f"Congrats, you have guessed it right. The answer in {answer}!\n{character}{character}{character}"
                      f"\n\n")
                Bagel.replay_game(self)
            else:
                for j in range(self.NUM_DIGITS):
                    if guess_list[j] == answer_list[j]:
                        clues.append("Fermi")
                    elif guess_list[j] in answer_list:
                        clues.append("Pico")
                if len(clues) == 0:
                    print("Bagels")
                else:
                    clues.sort()
                    clue = ' '.join(clues)
                    print(clue)
