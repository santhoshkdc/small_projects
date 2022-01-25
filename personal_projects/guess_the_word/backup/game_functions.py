"""This module will contain the functions necessary for the guess game_play.
Pick a random word, not a number, from a text.
In the Console describe the random word,
using the the total letters in it,
explicitly telling a few letters and their places, etc.,
A total of 3 guess to find the word
"""
import random

class Guess_The_Word():
    def __init__(self):
        self.new_string = ""
        self.result = []

    def list_words(self):
        with open("text.txt") as f:
            f_obj = f.read()

        for i in f_obj:
            if i.isalpha() or i.isspace():
                self.new_string = self.new_string + i.lower()

        self.new_string = self.new_string.strip()
        self.result = self.new_string.split()

    def random_word(self):
        Guess_The_Word.list_words(self)
        word = random.choice(self.result)
        return word


class The_Game:
    game_play = Guess_The_Word()
    game_play.list_words()
    right_word = game_play.random_word().lower()

    def dash_the_word(self):
        word_list = list([i for i in The_Game.right_word])
        length = len(word_list)

        for i in range(int(length / 2)):
            word_list[random.randint(0, (length - 1))] = "_"
        word = "".join(word_list)
        return word
