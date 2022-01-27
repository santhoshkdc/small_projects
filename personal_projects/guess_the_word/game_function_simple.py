import random
import requests
import json
import os
import datetime


class Game_Functions:

    length = 0
    correct_word = 'XXXX'
    dict_ = {}
    masked_word = []
    idx = []

    def get_correct_word(self):
        with open("word_list.json", 'r', encoding='UTF-8') as f:
            words = json.load(f)
        correct_word = random.choice(words)
        return correct_word

    def clue_synonyms(self):
        synonyms = Game_Functions.dict_['meta']['syns'][0][0]
        return synonyms

    def clue_unmask_a_letter(self):
        idx = Game_Functions().idx
        word = list(Game_Functions().correct_word)
        random.shuffle(idx)
        idx.pop(-1)
        for i in idx:
            word[i] = '_'
        print(''.join(word))

    def clue_definition(self):
        definition = Game_Functions().dict_[
            'meanings'][0]['definitions'][0]['definition']
        return definition

    def get_response(self, length):
        while True:
            Game_Functions.correct_word = Game_Functions().get_correct_word()
            if len(Game_Functions.correct_word) in Game_Functions.length:
                pass
            else:
                continue
            print(Game_Functions.correct_word)
            start = datetime.datetime.now()
            t_api_key = os.environ.get('dictionary_api_thesaurus')
            url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{self.correct_word}"
            params = {'key': t_api_key}
            response = requests.get(url, params=params)
            stop = datetime.datetime.now()
            print((stop-start).total_seconds())
            try:
                if type(response.json()[0]) == str:
                    continue
                else:
                    pass
            except KeyError:
                continue
            try:
                Game_Functions.dict_ = response.json()[0]
            except KeyError:
                continue
            break

    def mask_the_word(self):
        word = list(Game_Functions.correct_word)
        l = len(word)
        idx = list(range(l))
        random.shuffle(idx)
        chunk = l//2
        idx = idx[:chunk]
        for i in idx:
            word[i] = '_'
        Game_Functions.masked_word = ''.join(word)
        Game_Functions.idx = idx
        pass

    def print_game_description():
        body = """
        Hi welcome to 'Guess The Word', a text based game built using
        Python. It is a simple game where you have to guess a word correctly 
        within 4 attempts. 
        
        You will be given a word depending on the chosen
        difficulty level. Some of the characters of the word will be removed 
        when displayed. You have to guess the wordand input to check if you're
        right. 
        
        If you are correct in  in the very first attempt, HURRY! You guessed it
        right! You will be given full points. 
        
        If not, don't worry you still have three chance with one clue each to 
        guess the word correctly. And yeah, the points will be given accordingly.
        """
        print(body)

    def print_rules():
        rules = """
        Here are the rules of the game.
        
        The game has three difficulty levels.
        1) In Easy level you will be given 4 to 7 lettered word
        2) In Moderate level you will be given 8 to 11 lettered word
        3) In Hard level you will be given 12 to 16 lettered word
        
        You will be given a dashed word to guess correctly. The points will be 
        given based on the number of attempts that you take to guess the word
        correctly.
        
        Attempt #1 --> 10 Points & No Additional Clue
        Attempt #2 --> 8 Points & A Synonym of the word
        Attempt #3 --> 5 Points & one dashed word reappears
        Attempt #4 --> 2 Points & A definition of the word
        
        Any more attempt would be that you have lost the game :/
        """
        print(rules)

    def main_function(self):
        print("It is time to start the game!")
        while True:
            print("Please choose the difficulty level.\n\n*Easy or 1\n*Moderate\
or 2\n*Hard or 3")
            response = input(">> ").lower()
            correct_responses = {
                'e': [3, 4, 5, 6], 'm': [7, 8, 9, 10],
                'h': [11, 12, 13, 14, 15], '1': [3, 4, 5, 6],
                '2': [7, 8, 9, 10], '3': [11, 12, 13, 14, 15]
            }
            if response.startswith(('e', 'm', 'h')):
                Game_Functions.length = correct_responses[response[0]]
            elif response.isdecimal() and int(response.lower()) in [1, 2, 3]:
                Game_Functions.length = correct_responses[response]
            else:
                continue
            break
        length = self.length
        Game_Functions().get_response(length)
        Game_Functions().mask_the_word()
        print("Here is you word to guess:\n>  ", end='')
        print(Game_Functions.masked_word)
        response = input('>  ')
        if response == Game_Functions.correct_word:
            print(
                f"You guessed it right! Congrats\nThe correct word is '{Game_Functions.correct_word}'")
        else:
            print("Maybe second time is the charm!? Anyways, here is you next clue,")
            synonym = Game_Functions().clue_synonyms()
            print(f"A synonym of the correct word is: {synonym}")
            response = input('\nMake a guess.\n>  ')
            if response == Game_Functions.correct_word:
                print(f"You guessed it right! Maybe second time is the charm!\nThe correct\
 word is '{Game_Functions.correct_word}'")
            else:
                print("You still have two more chances before I could call you a \
dummy. So the next clue here,\n")
                Game_Functions().clue_unmask_a_letter()
                if response == Game_Functions.correct_word:
                    print(
                        f"You are not a total dummy after all.\nThe correct word is '{Game_Functions.correct_word}'")
                else:
                    print(
                        "You are testing my patience here. OK, you have one last clue! Take it,")
                    print(
                        f"\nA meaning of the word is, '{Game_Functions().clue_definition()}'")
                    response = input("\nWhat's you guess:  ")
                    if response == Game_Functions.correct_word:
                        print(
                            f"AT LAST! Yeah, the correct answer is {Game_Functions.correct_word}")
                    else:
                        print("The only think that stop me from calling you a dummy\
is the fact that I don't have a lot of user. OK, lets forget this. Want to start over!?")


g = Game_Functions()
g.main_function()
